"""English interface overlay: complete catalog, no Chinese left on screen, persistent switch. Never opens USB."""
import ast
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
from PySide6 import QtWidgets as W
from desktopapp import completion, i18n, reloadguide
from desktopapp.locale_en import EN

ROOT = Path(__file__).resolve().parents[2]
GUI_MODULES = ('window', 'lookeditor', 'reloadguide', 'completion', 'connectionguide', 'zadigguide', 'lookguide', 'disclaimer',
               'shutterguide')
CJK = re.compile('[\u4e00-\u9fff]')
# Matched against raw worker errors, never displayed.
NOT_DISPLAYED = {'未完成'}


def source_strings():
    for name in GUI_MODULES:
        tree = ast.parse((ROOT / 'src/desktopapp' / (name + '.py')).read_text(encoding='utf-8'))
        docs = {id(node.body[0].value) for node in ast.walk(tree)
                if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)) and node.body
                and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant)}
        for node in ast.walk(tree):
            if (isinstance(node, ast.Constant) and isinstance(node.value, str) and CJK.search(node.value)
                    and id(node) not in docs and node.value not in NOT_DISPLAYED):
                yield name, node.value


class English(unittest.TestCase):
    def setUp(self):
        i18n.set_language('en')
        self.addCleanup(i18n.set_language, i18n.DEFAULT)


class CatalogTests(English):
    def test_every_interface_string_translates_with_same_placeholders(self):
        missing = [(name, text[:40]) for name, text in source_strings() if CJK.search(i18n.translate(text))]
        self.assertEqual(missing, [])
        for chinese, english in EN.items():
            if not isinstance(chinese, str):
                continue
            self.assertFalse(CJK.search(english), chinese[:40])
            self.assertEqual(i18n.PLACEHOLDER.findall(chinese), i18n.PLACEHOLDER.findall(english), chinese[:40])

    def test_pinned_module_texts_still_match_their_source(self):
        self.assertEqual([key for key in EN if not isinstance(key, str)], [])

    def test_composed_text_translates_through_templates_and_fragments(self):
        self.assertEqual(i18n.translate('本次更改 3 个槽位：2 项写入 · 1 项恢复'),
                         EN['本次更改 %d 个槽位：%d 项写入 · %d 项恢复'].replace('%d', '3', 1).replace('%d', '2', 1).replace('%d', '1', 1))
        self.assertEqual(i18n.translate('请为自订 ' + '、'.join(['2', '5']) + ' 选择 A7Look 文件。'),
                         EN['请为自订 '] + '2' + EN['、'] + '5' + EN[' 选择 A7Look 文件。'])
        summary = i18n.translate(completion.text({'phase': 'COMPLETE', 'options': {
            'sound': False, 'looks': [{'slot': 2, 'name': 'CC'}, {'slot': 5}]}}))
        self.assertNotRegex(summary, CJK)
        self.assertIn(EN['  自订 %s：%s'] % (5, EN['沿用文件名称']), summary.splitlines())
        self.assertIn('Next: ', i18n.translate(reloadguide.text(mode='fl23_enable')))
        self.assertNotRegex(i18n.translate(reloadguide.text(setup=True)), CJK)

    def test_partly_covered_text_stays_original_and_chinese_default_is_identity(self):
        partial = '自订 3：' + '用户自己的名字'
        self.assertEqual(i18n.translate(partial), partial)
        i18n.set_language(i18n.DEFAULT)
        self.assertEqual(i18n.translate('固件版本'), '固件版本')


class LanguageWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = W.QApplication.instance() or W.QApplication([])

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.data = Path(temporary.name) / 'app'
        env = patch.dict(os.environ, {'A7C2_DESKTOP_DATA': str(self.data)}); env.start(); self.addCleanup(env.stop)
        # Language and Qt entry points are process state; later tests expect the stock GUI.
        self.addCleanup(i18n.set_language, i18n.DEFAULT)
        self.addCleanup(i18n.uninstall)

    def window(self, saved=None):
        if saved is not None:
            self.data.mkdir(parents=True)
            (self.data / 'desktop.json').write_text(json.dumps(saved), encoding='utf-8')
        i18n.install()
        from desktopapp.window import Window
        value = Window(); value.timer.stop(); value.show()
        self.addCleanup(value.close)
        return value

    def visible_texts(self, window):
        texts = [window.windowTitle()]
        for widget in window.findChildren(W.QWidget):
            for getter in ('text', 'title', 'placeholderText', 'toolTip'):
                value = getattr(widget, getter, None)
                if callable(value):
                    result = value()
                    if isinstance(result, str):texts.append(result)
            if isinstance(widget, W.QComboBox):
                texts.extend(widget.itemText(i) for i in range(widget.count()))
            if isinstance(widget, W.QListWidget):
                texts.extend(widget.item(i).text() for i in range(widget.count()))
        return texts

    def test_saved_english_choice_leaves_no_chinese_except_language_name(self):
        window = self.window({'language': 'en'})
        window.look_editor.add_row()
        leftovers = [t for t in self.visible_texts(window) if CJK.search(t) and t != '简体中文']
        self.assertEqual(leftovers, [])
        self.assertEqual(window._language_picker.currentData(), 'en')

    def test_startup_notice_and_full_statement_are_english(self):
        self.window({'language': 'en'})
        from desktopapp.disclaimer import ConsentDialog, TermsDialog
        consent = ConsentDialog(); self.addCleanup(consent.close)
        texts = self.visible_texts(consent) + [consent.summary.toPlainText(), consent.summary.accessibleName()]
        self.assertEqual([t for t in texts if CJK.search(t)], [])
        self.assertIn('may be bricked', consent.summary.toPlainText())
        terms = TermsDialog(); self.addCleanup(terms.close)
        full = terms.body.toPlainText()
        self.assertTrue(full.startswith('Risk notice and use statement'), full[:60])
        self.assertFalse(CJK.search(full + terms.windowTitle()))

    def test_full_statement_stays_chinese_without_its_english_section(self):
        i18n.set_language('en')
        chinese = '## 风险告知与使用声明\n\n正文'
        with patch.object(i18n, 'DOCUMENTS', (('## 风险告知与使用声明', 'docs/en/notices.md', '## Missing heading'),)):
            self.assertEqual(i18n._document(chinese), chinese)

    def test_run_log_translates_each_covered_line_and_keeps_the_rest(self):
        window = self.window({'language': 'en'})
        window.log.appendPlainText('一键安装：PREPARED\n'
                                   '认证后相机未进入服务模式（期间出现的 Sony USB 身份：0e8a、0d68）。\n'
                                   'RuntimeError: 未找到相机 USB 连接。请拔插 USB 并选择海量存储后重试；尚未进行服务认证或声音写入。\n'
                                   '相机返回：打开任务目录')
        self.assertEqual(window.log.toPlainText().splitlines()[-4:], [
            'One-click install: PREPARED',
            'After authentication the camera did not enter service mode (Sony USB identities seen meanwhile: 0e8a, 0d68).',
            'RuntimeError: No camera USB connection found. Replug USB, choose Mass Storage and retry; '
            'no service authentication or sound write happened.',
            '相机返回：打开任务目录'])

    def test_saved_worker_output_keeps_original_text(self):
        window = self.window({'language': 'en'})
        window.current_job = self.data / 'job'; window.current_job.mkdir(parents=True)
        output = '服务连接成功，驱动准备结束。\n'
        window.process = type('Process', (), {'readAllStandardOutput': lambda self: output.encode('utf-8')})()
        self.addCleanup(setattr, window, 'process', None)
        window.process_output()
        self.assertEqual((window.current_job / 'process.log').read_text(encoding='utf-8'), output)
        self.assertEqual(window.log.toPlainText().splitlines()[-1], 'Service connection succeeded; driver preparation finished.')

    def test_switch_persists_and_rebuilds_without_running_job(self):
        window = self.window()
        self.assertEqual(window.nav.item(0).text(), '首页 · 一键安装')
        window.nav.setCurrentRow(4)
        window._language_picker.setCurrentIndex(1)
        replacement = i18n._windows[-1]
        self.addCleanup(replacement.close)
        self.assertIsNot(replacement, window)
        self.assertEqual(replacement.nav.item(0).text(), 'Home · One-click install')
        self.assertEqual(replacement.nav.currentRow(), 4)
        self.assertEqual(replacement._language_picker.currentData(), 'en')
        saved = json.loads((self.data / 'desktop.json').read_text(encoding='utf-8'))
        self.assertEqual(saved['language'], 'en')

    def test_switch_is_refused_while_a_task_runs(self):
        window = self.window()
        window.process = object()
        self.addCleanup(setattr, window, 'process', None)
        with patch.object(W.QMessageBox, 'information') as notice:
            window._language_picker.setCurrentIndex(1)
        notice.assert_called_once()
        self.assertEqual(window._language_picker.currentData(), 'zh-CN')
        self.assertEqual(i18n.language(), 'zh-CN')
        self.assertFalse((self.data / 'desktop.json').exists())

    def test_uninstall_restores_stock_qt_entry_points(self):
        stock = W.QLabel.setText, W.QMessageBox.information, W.QMainWindow.show
        i18n.install()
        self.assertNotEqual((W.QLabel.setText, W.QMessageBox.information, W.QMainWindow.show), stock)
        i18n.uninstall()
        self.assertEqual((W.QLabel.setText, W.QMessageBox.information, W.QMainWindow.show), stock)
        self.assertNotIn('setText', W.QPushButton.__dict__)
