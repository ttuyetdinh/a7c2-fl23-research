"""Optional English interface layered over the Chinese desktop GUI.

The GUI modules keep their Chinese literals unchanged. install() wraps the Qt
text entry points they call, so every string reaching the screen passes through
translate(). This keeps the layer free of edits to upstream GUI code: a new or
reworded Chinese string stays Chinese until locale_en.py gains an entry.

A translation is all-or-nothing: if any Chinese remains after catalog,
template and fragment matching, the original text is shown unchanged rather
than a mixture. The run log is translated line by line on screen only; the
saved worker.log/process.log and diagnostic bundles keep the original text.
"""
import re

LANGUAGES = (('zh-CN', '简体中文'), ('en', 'English'))
DEFAULT = 'zh-CN'
ANCHOR = '固件版本'  # The language picker goes before the firmware selector.
HAN = re.compile('[\u3400-\u9fff]')
PLACEHOLDER = re.compile(r'%[-\d.]*[sdf]')
_language = DEFAULT
_compiled = None
# Chinese punctuation left between translated pieces of a composed message.
_PUNCTUATION = str.maketrans({'：': ': ', '，': ', ', '；': '; ', '（': ' (', '）': ')', '。': '. ', '、': ', ',
                              '！': '! ', '？': '? ', '“': '"', '”': '"', '「': '"', '」': '"', '／': ' / '})
_saved = []
_MISSING = object()
_windows = []  # Rebuilt windows stay referenced while shown.
# Long documents shown from the Chinese docs: (start of the Chinese text, English
# document, its matching heading). The English section is read from the
# author's own translation; if that heading is gone, the Chinese stays.
DOCUMENTS = (('## 风险告知与使用声明', 'docs/en/notices.md', '## Risk notice and use statement'),)


def language():
    return _language


def set_language(code):
    global _language
    if code not in dict(LANGUAGES):
        raise ValueError('Unknown interface language: ' + str(code))
    _language = code


def load(settings):
    """Apply the saved choice; an unknown saved value falls back to Chinese."""
    code = settings.get('language', DEFAULT)
    set_language(code if code in dict(LANGUAGES) else DEFAULT)


def _placeholder_pattern(token, last):
    if token.endswith('d'):
        return r'(\d+)'
    if token.endswith('f'):
        return r'(\d+(?:\.\d+)?)'
    return r'(.*)' if last else r'(.+?)'


def _compile():
    global _compiled
    if _compiled is None:
        from .locale_en import EN
        catalog = {key: value for key, value in EN.items() if isinstance(key, str)}
        # Lines of multi-line entries also match on their own, because the run
        # log receives text line by line and messages are composed from pieces.
        for key, value in list(catalog.items()):
            chinese, english = key.split('\n'), value.split('\n')
            if len(chinese) > 1 and len(chinese) == len(english):
                for piece, translation in zip(chinese, english):
                    if HAN.search(piece) and piece not in catalog:
                        catalog[piece] = translation
        templates, fragments = [], []
        for key in sorted(catalog, key=len, reverse=True):
            tokens = PLACEHOLDER.findall(key)
            if not tokens:
                fragments.append(re.escape(key))
                continue
            parts = PLACEHOLDER.split(key)
            pattern = re.escape(parts[0])
            for index, token in enumerate(tokens):
                pattern += _placeholder_pattern(token, index == len(tokens) - 1 and not parts[index + 1])
                pattern += re.escape(parts[index + 1])
            templates.append((re.compile(pattern), catalog[key]))
        _compiled = catalog, templates, re.compile('|'.join(fragments))
    return _compiled


def _fill(english, values):
    values = iter(values)
    return PLACEHOLDER.sub(lambda _: next(values), english)


def translate(text):
    """English for Chinese interface text; anything not fully covered is unchanged."""
    if _language == DEFAULT or not isinstance(text, str) or not HAN.search(text):
        return text
    catalog, templates, fragments = _compile()
    if text in catalog:
        return catalog[text]
    result = text
    for pattern, english in templates:
        result = pattern.sub(lambda match: _fill(english, (translate(value) for value in match.groups())), result)
    result = fragments.sub(lambda match: catalog[match.group(0)], result)
    return text if HAN.search(result) else _tidy(result)


def _tidy(text):
    text = text.translate(_PUNCTUATION)
    text = re.sub(r'(?<=\S) {2,}', ' ', text)  # Leading indentation (JSON) stays.
    text = re.sub(r'\( ', '(', text)
    text = re.sub(r'(?<=[a-z)][.;!?])(?=[A-Z])', ' ', text)  # Sentences joined in the source.
    return re.sub(r' +(?=[,.;:)!?]|$)', '', text, flags=re.M)


tr = translate


def _log(text):
    """Run-log chunk: whole text first, then each line on its own."""
    if _language == DEFAULT or not isinstance(text, str) or not HAN.search(text):
        return text
    whole = translate(text)
    return whole if whole != text else '\n'.join(translate(line) for line in text.split('\n'))


def _document(text):
    if _language == DEFAULT or not isinstance(text, str):
        return text
    for chinese, path, heading in DOCUMENTS:
        if text.startswith(chinese):
            from .paths import ROOT
            try:
                english = (ROOT / path).read_text(encoding='utf-8')
            except OSError:
                return text
            start = english.find('\n' + heading + '\n')
            return text if start < 0 else english[start + 1:]
    return translate(text)


def _patch(owner, name, wrapper):
    _saved.append((owner, name, owner.__dict__.get(name, _MISSING)))
    setattr(owner, name, wrapper)


def _method(owner, name, position, convert=translate):
    original = getattr(owner, name)

    def wrapper(self, *args, **kwargs):
        if len(args) > position:
            args = list(args)
            args[position] = convert(args[position])
        return original(self, *args, **kwargs)
    _patch(owner, name, wrapper)


def _items(owner, name):
    original = getattr(owner, name)
    _patch(owner, name, lambda self, items, *args: original(self, [translate(item) for item in items], *args))


def _static(owner, name, positions):
    original = getattr(owner, name)

    def wrapper(*args, **kwargs):
        args = [translate(value) if index in positions else value for index, value in enumerate(args)]
        return original(*args, **kwargs)
    _patch(owner, name, staticmethod(wrapper))


def install():
    """Route Qt interface text through translate() and add the language picker."""
    if _saved:
        return
    from PySide6 import QtWidgets as W
    from .paths import load_settings
    load(load_settings())
    for owner, name, position in (
            (W.QLabel, '__init__', 0), (W.QLabel, 'setText', 0),
            (W.QAbstractButton, 'setText', 0), (W.QPushButton, '__init__', 0),
            (W.QCheckBox, '__init__', 0), (W.QRadioButton, '__init__', 0),
            (W.QGroupBox, '__init__', 0), (W.QGroupBox, 'setTitle', 0),
            (W.QWidget, 'setWindowTitle', 0), (W.QWidget, 'setToolTip', 0),
            (W.QMessageBox, 'setWindowTitle', 0), (W.QMessageBox, 'setText', 0),
            (W.QMessageBox, 'setInformativeText', 0), (W.QMessageBox, 'addButton', 0),
            (W.QLineEdit, 'setPlaceholderText', 0), (W.QPlainTextEdit, 'setPlaceholderText', 0),
            (W.QTextEdit, 'setPlainText', 0), (W.QTextEdit, 'setHtml', 0),
            (W.QWidget, 'setAccessibleName', 0), (W.QComboBox, 'addItem', 0),
            (W.QComboBox, 'insertItem', 1), (W.QListWidget, 'addItem', 0),
            (W.QFormLayout, 'addRow', 0), (W.QFormLayout, 'insertRow', 1)):
        _method(owner, name, position)
    _method(W.QPlainTextEdit, 'appendPlainText', 0, _log)
    _method(W.QTextEdit, 'setMarkdown', 0, _document)
    _items(W.QComboBox, 'addItems')
    _items(W.QListWidget, 'addItems')
    for name in ('information', 'warning', 'question', 'critical'):
        _static(W.QMessageBox, name, (1, 2))
    for name in ('getOpenFileName', 'getSaveFileName', 'getExistingDirectory'):
        _static(W.QFileDialog, name, (1,))
    show = W.QMainWindow.show

    def show_with_picker(window):
        if not getattr(window, '_language_picker', None):
            _add_picker(window)
        return show(window)
    _patch(W.QMainWindow, 'show', show_with_picker)


def uninstall():
    """Restore the original Qt entry points (tests)."""
    while _saved:
        owner, name, original = _saved.pop()
        if original is _MISSING:
            delattr(owner, name)
        else:
            setattr(owner, name, original)


def _add_picker(window):
    from PySide6 import QtWidgets as W
    anchors = [label for label in window.findChildren(W.QLabel) if label.text() in (ANCHOR, translate(ANCHOR))]
    for layout in window.findChildren(W.QBoxLayout) if anchors else ():
        index = layout.indexOf(anchors[0])
        if index < 0:
            continue
        picker = W.QComboBox()
        for code, name in LANGUAGES:
            picker.addItem(name, code)
        picker.setCurrentIndex([code for code, _ in LANGUAGES].index(_language))
        picker.currentIndexChanged.connect(lambda: _switch(window, picker))
        layout.insertSpacing(index, 12)
        layout.insertWidget(index, picker)
        layout.insertWidget(index, W.QLabel('界面语言'))
        window._language_picker = picker
        return


def _switch(window, picker):
    """Save the choice and rebuild the window; never while a task runs."""
    from PySide6 import QtWidgets as W
    from .paths import data_root, load_settings, write_json
    code = picker.currentData()
    if code == _language:
        return
    if getattr(window, 'process', None):
        W.QMessageBox.information(window, '任务仍在运行', '请等待当前任务结束后再切换界面语言。')
        picker.blockSignals(True)
        picker.setCurrentIndex([value for value, _ in LANGUAGES].index(_language))
        picker.blockSignals(False)
        return
    settings = getattr(window, 'settings', None)
    settings = load_settings() if settings is None else settings
    for key, field in getattr(window, 'fields', {}).items():
        settings[key] = field.text()
    settings['language'] = code
    write_json(data_root() / 'desktop.json', settings)
    set_language(code)
    replacement = type(window)(**({'demo': window.demo} if hasattr(window, 'demo') else {}))
    replacement.setGeometry(window.geometry())
    if hasattr(window, 'nav') and hasattr(replacement, 'nav'):
        replacement.nav.setCurrentRow(window.nav.currentRow())
    _windows[:] = [replacement]
    replacement.show()
    window.close()
    window.deleteLater()
