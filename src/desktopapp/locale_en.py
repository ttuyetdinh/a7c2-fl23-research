"""English interface text keyed by the Chinese source string.

Long texts owned by other modules are pinned by a digest of the Chinese they
were translated from. If that text is reworded or removed, the key stops
matching and the interface shows the current Chinese, never stale English.
"""
import hashlib
import importlib
from .locale_en_log import LOG


def _pinned(module, name, digest):
    try:
        text = getattr(importlib.import_module('desktopapp.' + module), name)
    except (ImportError, AttributeError):
        text = None
    if isinstance(text, str) and hashlib.sha256(text.encode()).hexdigest()[:12] == digest:
        return text
    return ('stale', module, name)


EN = {
    # Window frame and navigation
    '首页 · 一键安装': 'Home · One-click install',
    '连接与驱动': 'Connection & drivers',
    '恢复原厂功能': 'Restore factory functions',
    '自定义创意外观': 'Custom Creative Looks',
    '竖屏显示': 'Vertical Display',
    '电子快门声音': 'Electronic shutter sound',
    '界面语言': 'Language',
    '固件版本': 'Firmware',
    'Windows 测试版': 'Windows preview',
    '桌面开发版': 'Desktop development build',
    ' · 一键安装与六个功能入口 · ': ' · One-click install and six feature pages · ',
    '就绪。选择左侧功能；启动软件不会访问相机。': 'Ready. Choose a page on the left; starting the app never accesses the camera.',
    '完整运行日志与原始报错会显示在这里。': 'The complete run log and original error messages appear here.',
    '打开任务目录': 'Open task folder',
    '导出诊断包': 'Export diagnostic bundle',
    '停止离线任务': 'Stop offline task',
    '任务仍在运行': 'A task is still running',
    '请等待当前任务结束后再切换界面语言。': 'Wait for the current task to finish before changing the interface language.',
    '请等待当前任务结束后关闭。相机写入期间不要结束程序或拔线。':
        'Wait for the current task to finish before closing. Do not quit the app or unplug the cable while the camera is being written.',
    '选择…': 'Browse…',
    '选择目录': 'Choose folder',
    '保存文件': 'Save file',
    '选择文件': 'Choose file',
    '关闭': 'Close',
    '、': ', ',
    '；': '; ',

    # Home page
    '一键安装': 'One-click install',
    '六款外观、FL2／FL3、电子快门声及竖屏保存开关合并安装。按提示断电重开后，同一按钮只核对加载；无需逐槽安装。':
        'Installs the six looks, FL2/FL3, electronic shutter sound and the saved Vertical Display switch together. '
        'After the prompted cold reload, the same button only verifies loading; no slot-by-slot installation is needed.',
    '安装内置六款外观（替换自订 1–6，原有创意外观保留）':
        'Install the six built-in looks (replaces Custom 1–6; original Creative Looks are kept)',
    '启用 FL2／FL3': 'Enable FL2/FL3',
    '启用索尼原生电子快门声音': "Enable Sony's native electronic shutter sound",
    '保存开启竖屏拍摄信息显示（重开后自动生效）': 'Save Vertical Display as on (takes effect automatically after restart)',
    '安装 Lightroom 自动识别插件（需要 Lightroom）': 'Install the Lightroom auto-profile plugin (requires Lightroom)',
    '安装尚未结束，请点击“继续安装”，按弹窗完成下一步；需要断电时，接回 USB 后仍点击此按钮。':
        'Installation is not finished. Click "Continue installation" and follow the dialog. '
        'If a cold reload is required, reconnect USB afterwards and click this button again.',
    _pinned('presets', 'SUMMARY', 'ba2af57cec1b'): '1 NC · 2 CC · 3 NN · 4 Astia · 5 GR Positive · 6 GR Negative',
    '本次已保存外观：': 'Looks saved for this installation: ',
    '未选择外观，不会新增六款': 'No looks selected; the six looks will not be added',
    '开始新的一键安装': 'Start a new one-click install',
    '继续安装': 'Continue installation',
    '正在安装…': 'Installing…',
    '查看上次安装结果（不连接相机）': 'View last installation result (no camera access)',
    '改用自己的 A7Look 文件（先取消勾选内置六款）': 'Use your own A7Look files instead (untick the six built-in looks first)',
    '选择 A7Look 文件': 'Choose A7Look files',
    '自订 ': 'Custom ',
    '从 DCP／LUT 生成 A7Look…': 'Create A7Look from DCP/LUT…',
    '恢复出厂、卸载驱动和删除外观不会混入安装流程。自定义声音请在“电子快门声音”中转换后直接保存，试听可选。':
        'Factory restore, driver removal and look removal are never part of installation. '
        'For a custom sound, convert it on the "Electronic shutter sound" page and save it directly; audition is optional.',
    '建议先安装驱动': 'Install drivers first',
    '这台电脑还没有成功连接过相机。建议先到“连接与驱动”页，点“准备两阶段驱动并测试连接”，'
    '看到连接成功后再回来一键安装。':
        'This computer has not connected to the camera successfully yet. Go to the "Connection & drivers" page, '
        'click "Prepare two-stage drivers and test connection", and return for the one-click install after it connects.',
    '一键安装也会自动尝试安装驱动，但驱动失败时排查更麻烦。'
    '驱动反复装不上，可点该页的“用 Zadig 手动安装驱动”，按说明操作。':
        'One-click install also tries to install drivers, but driver failures are harder to troubleshoot there. '
        'If drivers keep failing, use "Install drivers manually with Zadig" on that page and follow the steps.',
    '先去安装驱动': 'Install drivers first',
    '直接一键安装': 'Install now anyway',
    '安装尚未结束': 'Installation not finished',
    '请点首页“继续安装”，按提示完成后续步骤。': 'Click "Continue installation" on the Home page and follow the prompts.',
    '安装完成': 'Installation complete',
    '安装完成。可查看上次安装结果，无需再次刷写。': 'Installation complete. You can view the last result; no further write is needed.',

    # Reload helpers
    '如何断电重开？查看详细步骤': 'How do I do a cold reload? Show detailed steps',
    '已拔 USB、等灯停、关机，取下电池至少 1 分钟后重开；\n已确认':
        'USB unplugged, light stopped, camera off, battery out for at least 1 minute, then restarted;\nconfirmed: ',
    '恢复尚未开始，请断电后重试': 'Restore not started; power-cycle and retry',
    '恢复尚未完成，请重启后核对': 'Restore not finished; restart and verify',
    '试听结果已记录，请断电恢复原声': 'Audition recorded; power-cycle to restore the original sound',
    '读写已结束，请断电重开': 'Reading and writing have ended; do a cold reload',

    # Connection page
    '相机开机并选择“海量存储／Mass Storage”，使用可传数据的 USB 线。一次只连接一台相机。':
        'Turn the camera on and select "Mass Storage". Use a USB cable that carries data. Connect one camera at a time.',
    'USB 连接': 'USB connection',
    '普通连接 · 054C:0E8A': 'Normal connection · 054C:0E8A',
    '服务连接 · 054C:0336': 'Service connection · 054C:0336',
    '驱动目标': 'Driver target',
    'macOS 相机存储卷': 'macOS camera volume',
    '检测相机与驱动': 'Detect camera and drivers',
    '准备两阶段驱动并测试连接（自动）': 'Prepare two-stage drivers and test connection (automatic)',
    '用 Zadig 手动安装驱动（自动失败时）': 'Install drivers manually with Zadig (if automatic fails)',
    '准备 USB 服务连接': 'Prepare USB service connection',
    '单独安装所选身份的驱动（高级）': 'Install driver for the selected identity only (advanced)',
    '检查 USB 访问（macOS 无需 Zadig）': 'Check USB access (macOS needs no Zadig)',
    '推出选中的相机存储卷': 'Eject the selected camera volume',
    '测试服务连接（不写固件）': 'Test service connection (no firmware write)',
    '检测 USB 连接稳定性（只读）': 'Check USB connection stability (read-only)',
    '卸载相机驱动，恢复 Windows 默认连接': 'Uninstall camera drivers and restore the Windows default',
    '连接中断后先查看完整日志。报错不会触发重新刷写或自动重装驱动。':
        'If the connection drops, check the full log first. Errors never trigger a rewrite or an automatic driver reinstall.',
    '\n驱动或连接没有成功：先在“连接与驱动”页卸载驱动后重装；仍不行，'
    '可点该页的“用 Zadig 手动安装驱动”，按说明给 0E8A 和 0336 两个身份分别装 libusbK。':
        '\nDriver or connection failed: uninstall and reinstall drivers on the "Connection & drivers" page. '
        'If it still fails, click "Install drivers manually with Zadig" there and install libusbK for both 0E8A and 0336.',

    # Recovery page
    '已内置本项目修改区域的原厂 2.01 基准。移除已支持的项目修改，六个自订栏位设为 ST 默认，保留机身校准。无需旧备份或下载完整固件；旧配方不找回。':
        "A stock 2.01 reference for every region this project changes is built in. Restoring removes supported project changes, "
        "sets the six custom slots to ST defaults and keeps body calibration. No old backup or full firmware download is needed; "
        "former recipes are not recovered.",
    '按当前相机恢复原厂 2.01 功能（无需旧备份）': 'Restore stock 2.01 functions on this camera (no old backup needed)',
    '恢复写入后必须按弹窗重启，再接回核对；核对通过前不会标记恢复完成。':
        'After the restore write, restart as prompted and reconnect to verify; the restore is not marked complete until verification passes.',
    '上次恢复的核对记录（可选）': 'Verification record of the last restore (optional)',
    '核对事务目录': 'Transaction folder to verify',
    '取景、拍照和回放正常': 'live view, shooting and playback work',
    '重启后核对并完成恢复（恢复写入后必做）': 'Verify after restart and finish restore (required after a restore write)',
    '相机仍需能够进入 USB 服务通信；此操作不是索尼更新器的降级重刷。':
        "The camera must still be able to enter USB service mode; this is not a downgrade through Sony's updater.",
    '导入完整原厂 2.01 参考文件（高级、可选）': 'Import a complete stock 2.01 reference file (advanced, optional)',
    '原厂文件': 'Stock file',
    '准备所选原厂文件（不连接相机）': 'Prepare the selected stock file (no camera access)',
    '使用导入的完整原厂文件恢复': 'Restore using the imported complete stock file',
    '使用旧备份回到过去的状态（可选）': 'Return to an earlier state with an old backup (optional)',
    '上次恢复写入与读回已结束，但核对尚未完成。请按提示重启后使用下方核对按钮；上方恢复按钮始终按当前相机重新规划。':
        'The last restore write and readback finished, but verification is pending. Restart as prompted and use the verify button below; '
        'the restore button above always plans again from the current camera.',
    '上次恢复核对已通过；再次点击恢复会按当前相机重新规划，旧任务不影响本次操作。':
        'The last restore was verified. Restoring again plans from the current camera; old tasks do not affect it.',
    '上次操作未完成或尚未开始，旧记录保留用于诊断。再次恢复会读取当前相机，不要求旧任务成功。':
        'The last operation did not finish or did not start; its record is kept for diagnostics. '
        'Restoring again reads the current camera and does not require the old task to have succeeded.',
    '恢复来源': 'Restore source',
    '备份目录': 'Backup folder',
    '或选择完整备份 ZIP…': 'Or choose a complete backup ZIP…',
    '恢复任务目录': 'Restore task folder',
    '检查所选备份（离线）': 'Check the selected backup (offline)',
    '一键还原：查找并使用最初完整备份': 'One-click restore: find and use the earliest complete backup',
    '恢复所选备份并完整读回': 'Restore the selected backup with full readback',
    '恢复后取景、拍照和回放正常': 'live view, shooting and playback work after the restore',
    '核对旧备份恢复后的加载状态': 'Check loaded state after an old-backup restore',
    '相机需要仍可进入服务通信。此入口使用机身备份；不把官方 BODYDATA.DAT 当作备份刷入。':
        'The camera must still be able to enter service mode. This uses a body backup; the official BODYDATA.DAT is never written as a backup.',

    # FL2/FL3 page and preview trial
    '直接启用／移除，不要求创建备份。移除只关闭 FL2／FL3 的列表入口，保留自定义外观所需的共用色彩代码；之后可以重新启用。':
        'Enable or remove directly; no backup is required. Removing only hides FL2/FL3 from the list and keeps the shared color code '
        'used by custom looks; you can enable them again later.',
    '启用／重新启用 FL2 / FL3': 'Enable / re-enable FL2 / FL3',
    '从列表移除 FL2 / FL3，保留自定义外观': 'Remove FL2 / FL3 from the list, keep custom looks',
    '写入读回后按弹窗断电重开，在相机确认即可使用；无需再接电脑核对。':
        'After write and readback, do the cold reload in the dialog and check on the camera; no computer verification is needed.',
    '加载核对（可选诊断，不是使用前提）': 'Load verification (optional diagnostic, not required)',
    '菜单、拍照和回放正常': 'menus, shooting and playback work',
    '只读核对已加载的版本（可选）': 'Read-only check of the loaded version (optional)',
    '取景器横线＋实时预览：第 3 版候选（等待实机验收）': 'Viewfinder line + live preview: candidate 3 (awaiting hardware acceptance)',
    '第 1 版横线消失，但切槽预览可能停在上一个外观。第 3 版补传未提交的色表，'
    '并修正第 2 版的重复上传问题。应用后按弹窗断电重开，再检查横线和六槽切换。':
        'Candidate 1 removed the line, but preview could stay on the previous look after switching slots. Candidate 3 uploads pending tables '
        'and fixes the repeated uploads of candidate 2. After applying, cold-reload as prompted, then check the line and all six slots.',
    '应用横线＋实时预览修复候选（第 3 版）': 'Apply line + live preview candidate (3)',
    '切回第 1 版：原生刷新（预览可能滞留）': 'Switch back to candidate 1: native refresh (preview may lag)',
    '撤回测试：恢复旧版刷新方式': 'Withdraw test: restore the old refresh method',
    '横线消失、六槽实时切换、拍摄和回放正常': 'the line is gone, all six slots switch live, shooting and playback work',
    '断电重开后只读核对本轮测试': 'Read-only check of this test after the cold reload',

    # Custom looks page
    '按需添加本次要改的槽位；未添加的槽位保持原样。可在同一批操作中写入外观和恢复 ST 默认。':
        'Add the slots you want to change; slots you do not add stay unchanged. One batch can both write looks and reset slots to ST.',
    '添加操作项后继续': 'Add an operation to continue',
    '查看并应用这 %d 项更改': 'Review and apply these %d changes',
    '打开内置 DCP／A7Look 配对库': 'Open paired DCP/A7Look library',
    '安装 LrC 自动识别插件…': 'Install LrC auto-profile plugin…',
    'LUT 格式说明：ST / sRGB，不是 S-Log3…': 'LUT formats: ST / sRGB, not S-Log3…',
    '写入页选择 .a7look；.cube / .dcp 先用上方工具转换。仅更改清单内的槽位。':
        'Choose .a7look files here; convert .cube / .dcp with the tools above first. Only listed slots change.',
    '同一次操作自动检查当前状态、写入并完整读回。结束后按弹窗断电加载，无需单独点击核对。':
        'One operation checks the current state, writes and reads everything back. Afterwards cold-reload as prompted; no separate verify click is needed.',
    '后台任务尚未确认结束，请等待原结果或查看日志，不重复写入。':
        'A background task has not confirmed completion. Wait for its result or check the log; nothing is written again.',
    '上次操作正在等待资源续接，将沿用已保存的清单。': 'The last operation is waiting to continue after resources; the saved list will be reused.',
    '继续槽位更改': 'Continue slot changes',
    '上次在写入前停止，旧记录已保留；可以调整清单后重试。': 'The last attempt stopped before writing; its record is kept. You can adjust the list and retry.',
    '重试本次更改（上次未写入）': 'Retry these changes (nothing was written last time)',
    '上次操作尚未完成；请查看原任务记录，不自动重复写入。': 'The last operation did not finish; review its task record. Nothing is rewritten automatically.',
    '查看未完成任务记录': 'View unfinished task record',
    '上次任务尚未完成': 'Last task not finished',
    '请保留原记录，核对未知结果后再继续。': 'Keep the original record and resolve the unknown result before continuing.',
    '\n任务目录：': '\nTask folder: ',
    '请检查操作清单': 'Check the operation list',

    # Look editor
    '目标槽位': 'Target slot',
    '本次操作': 'Operation',
    '恢复 ST 默认': 'Reset to ST default',
    '写入 A7Look': 'Write A7Look',
    '移除这项': 'Remove',
    '仅移除此操作项，该槽保持原样': 'Removes only this operation; the slot stays unchanged',
    '此槽恢复为 ST 默认；不会找回导入前的旧配方。': 'This slot is reset to the ST default; the recipe from before the import is not recovered.',
    'A7Look 文件': 'A7Look file',
    '机内显示名称': 'Name shown on camera',
    '请选择 .a7look 文件': 'Choose an .a7look file',
    '选择文件…': 'Choose file…',
    '留空沿用文件内名称': 'Leave empty to use the name in the file',
    '+ 添加操作项': '+ Add operation',
    '新增项默认“恢复 ST 默认”，可切换为写入。': 'New operations default to "Reset to ST default"; switch to write if needed.',
    '尚未添加操作项': 'No operations yet',
    '点击“添加操作项”，选择目标槽位和操作。当前六个槽位均保持原样。':
        'Click "Add operation" and choose a slot and an operation. All six slots currently stay unchanged.',
    '同一槽位只能添加一个操作。': 'Each slot can have only one operation.',
    '请为自订 ': 'Choose an A7Look file for Custom ',
    ' 选择 A7Look 文件。': '.',
    '本次更改 %d 个槽位：%d 项写入 · %d 项恢复': 'Changing %d slots: %d writes · %d resets',
    '保持原样：': 'Unchanged: ',
    '无（六个槽位均在本次清单中）': 'none (all six slots are in this list)',

    # Vertical display page
    '竖握相机时，拍摄信息、图标和布局跟随转向。开启会保存原生开关，断电重开后自动生效；不是整个 MENU 转向。':
        'When the camera is held vertically, shooting information, icons and layout rotate. Enabling saves the native switch, '
        'which takes effect after a cold reload; the full MENU does not rotate.',
    '显示任务': 'Display task',
    '任务目录': 'Task folder',
    '开启竖屏显示': 'Enable Vertical Display',
    '关闭竖屏显示': 'Disable Vertical Display',
    '开启会保存竖屏开关并应用当前的 Fn／子菜单显示修正；关闭会先关闭竖屏，再撤销显示修正。两个操作都支持重复覆盖。':
        'Enabling saves the vertical switch and applies the current Fn/submenu display corrections; disabling turns vertical display off first, '
        'then reverts the corrections. Both can be repeated safely.',
    '已知显示问题：竖屏创意外观选择页的外框仍偏粗；刻度已横向显示，但橙色指针朝向尚未修正。':
        'Known display issues: the frame on the vertical Creative Look selection page is still too thick; the scale is now horizontal, '
        'but the orange pointer direction is not yet corrected.',
    '开启／关闭会一次完成所选写入和读回，再统一弹窗提示断电加载。相同状态可重复点击，相同内容不重复写入。':
        'Enable/disable completes the write and readback in one go, then shows one cold-reload prompt. '
        'Clicking again in the same state is safe; identical content is not rewritten.',

    # Sound page
    '独立开关控制电子快门发声分支。音频转换后可直接保存，临时试听可选；写入后按弹窗断电加载。':
        'A separate switch controls the electronic-shutter sound path. A converted clip can be saved directly; temporary audition is optional. '
        'After writing, cold-reload as prompted.',
    '声音工作区': 'Sound workspace',
    '工作目录': 'Work folder',
    '第二份备份': 'Second backup',
    '开启电子快门声': 'Turn electronic shutter sound on',
    '关闭电子快门声': 'Turn electronic shutter sound off',
    '导入音频／视频片段': 'Import an audio/video clip',
    '声音文件': 'Sound file',
    '起点（秒）': 'Start (s)',
    '长度（秒）': 'Length (s)',
    '转换所选片段': 'Convert selected clip',
    '相机内临时试听': 'Temporary audition on camera',
    '音量降低 −3 dB': 'Volume −3 dB',
    '音量提高 +3 dB': 'Volume +3 dB',
    '还原转换时音量': 'Reset to converted volume',
    '先转换片段，再调节音量；仅处理电脑上的音频，不连接相机。达到音量上限会自动限制以避免削波；保存时使用调整后的声音。重新转换会重置音量。':
        'Convert a clip first, then adjust volume; this only processes audio on the computer and does not connect to the camera. '
        'Volume is limited at the maximum to avoid clipping; saving uses the adjusted sound. Converting again resets the volume.',
    '保存当前自定义声音': 'Save current custom sound',
    '转换成功即可直接保存；自动建立工作区并准备电子快门声支援，不必先开启或关联旧任务。试听可选；全部写入完成后按弹窗统一断电加载。':
        'Once converted, you can save directly; the workspace and electronic shutter sound support are prepared automatically, '
        'with no need to enable or link an old task first. Audition is optional; after all writes finish, cold-reload once as prompted.',
    '试听确认与恢复记录（可选，不影响保存）': 'Audition confirmation and recovery records (optional, do not affect saving)',
    '确认试听正确': 'Confirm audition is correct',
    '已断电恢复原声，记录恢复完成': 'Power-cycled and original sound restored; record recovery',
    '声音正确、拍摄和回放正常': 'the sound is correct, shooting and playback work',
    '重开后核对声音': 'Verify sound after restart',
    '恢复原厂音效': 'Restore original sound',
    '声音工作区需要核对': 'Sound workspace needs checking',
    '请先转换片段': 'Convert a clip first',
    '还没有转换好的声音。请先选择声音文件、设置起点和长度，点「转换所选片段」，成功后再试听。':
        'There is no converted sound yet. Choose a sound file, set the start and length, click "Convert selected clip", then audition after it succeeds.',

    # Dialogs
    '打开 Zadig 下载页': 'Open Zadig download page',
    '生成 A7Look': 'Create A7Look',
    'CUBE：输入必须是 Sony ST / sRGB，输出 sRGB；不能直接使用 S-Log3 / S-Gamut3.Cine 或其他 Log LUT。\nDCP：内置离线解析与拟合，不需要 Lightroom、插件或联网。转换 LookTable／色调曲线，机内效果为拟合近似。此工具只生成 .a7look，不写相机。':
        'CUBE: input must be Sony ST / sRGB and output sRGB; S-Log3 / S-Gamut3.Cine or other Log LUTs cannot be used directly.\n'
        'DCP: parsed and fitted offline, with no Lightroom, plugin or network. The LookTable/tone curve is converted; in-camera results are a fitted approximation. '
        'This tool only creates .a7look files and does not write the camera.',
    '支持哪些格式和色彩空间？查看完整说明…': 'Which formats and color spaces are supported? Full guide…',
    '源文件与输出': 'Source and output',
    '外观名称': 'Look name',
    '输出 A7Look': 'Output A7Look',
    '响应文件': 'Response file',
    '开始生成': 'Create',
    '这里没有旧备份恢复记录': 'No old-backup restore record here',
    '“核对旧备份恢复后的加载状态”只用于“使用旧备份回到过去的状态”。\n'
    '用内置原厂基准或固件文件恢复后，应点“重启后核对并完成恢复”。\n现在改为核对原厂恢复？':
        '"Check loaded state after an old-backup restore" is only for "Return to an earlier state with an old backup".\n'
        'After restoring from the built-in reference or a firmware file, use "Verify after restart and finish restore".\n'
        'Verify the factory restore instead now?',
    '卸载相机驱动': 'Uninstall camera drivers',
    '将备份并卸载 Sony 054C:0E8A／0336 的第三方驱动，让 Windows 重新识别相机。\n'
    '完成后可能需要拔插 USB，重新选择海量存储模式。此操作不修改相机固件。\n现在卸载？':
        'Third-party drivers for Sony 054C:0E8A/0336 will be backed up and uninstalled so Windows detects the camera again.\n'
        'Afterwards you may need to replug USB and select Mass Storage again. Camera firmware is not changed.\nUninstall now?',

    # Write confirmation
    '开始相机写入': 'Start camera write',
    '目标：': 'Target: ',
    '首页勾选的功能；替换自订 1–6：': 'Features ticked on Home; replaces Custom 1–6: ',
    '首页勾选的功能及所选 A7Look 槽位': 'Features ticked on Home and the selected A7Look slots',
    '自动选择已连接机身最早可用的完整备份': 'Automatically choose the earliest complete backup for the connected body',
    '取景器与实时预览第三版候选': 'Viewfinder and live preview candidate 3',
    '第一版原生刷新条件': 'Candidate 1 native refresh conditions',
    '测试前的旧版刷新方式': 'Refresh method from before the test',
    '自订 %s → %s': 'Custom %s → %s',
    '写入 ': 'write ',
    '继续已写好名称的外观安装：': 'Continue the look installation whose names are written: ',
    '按当前相机重新恢复原厂 2.01 功能': 'Restore stock 2.01 functions again from the current camera',
    '竖屏显示＋Fn／子菜单线框修正': 'Vertical Display + Fn/submenu frame corrections',
    '关闭竖屏显示并撤销线框修正': 'Disable Vertical Display and revert frame corrections',
    '原厂 2.01 功能': 'Stock 2.01 functions',
    'FL2／FL3：启用': 'FL2/FL3: enable',
    'FL2／FL3：从列表移除': 'FL2/FL3: remove from list',
    '自订 %s：%s': 'Custom %s: %s',
    'ST 默认': 'ST default',
    '仅更改 CP 的 LUT 刷新代码；保留色表、名称、配方和其他功能。写入后完整断电重开，检查横线及切槽刷新。\n':
        'Changes only the CP LUT refresh code; tables, names, recipes and other features are kept. '
        'After writing, do a full cold reload and check the line and slot-switch refresh.\n',
    '一次应用清单内的写入和恢复，未添加的槽位保持原样；保留 FL23、声音和竖屏。写入读回完成后统一提示断电重开。\n':
        'Applies every write and reset in the list at once; slots not listed stay unchanged, and FL23, sound and vertical display are kept. '
        'A single cold-reload prompt follows write and readback.\n',
    '自动准备驱动并安装首页勾选的功能。断电重开必须由你按提示完成；结果不明时停止，不自动重复刷写。\n':
        'Prepares drivers automatically and installs the features ticked on Home. You must do the cold reload when prompted; '
        'an unknown result stops the process and is never rewritten automatically.\n',
    '从当前相机字节重新生成原厂恢复计划；旧记录不影响本次操作，已符合目标的内容不重复写入。\n':
        'Builds a new factory restore plan from the current camera bytes; old records do not affect it, and content already at the target is not rewritten.\n',
    '将移除项目程序修改、将六个自订栏位设为 ST 默认；旧配方不找回。请先在相机选择 ST。\n':
        'Removes project program changes and sets the six custom slots to ST defaults; former recipes are not recovered. Select ST on the camera first.\n',
    '只关闭 FL2／FL3 列表入口，保留 LUT 与共用代码。请先在相机选择 ST。\n':
        'Only hides FL2/FL3 from the list; LUTs and shared code are kept. Select ST on the camera first.\n',
    '将所选自订栏位设为 ST 默认，保留其他栏位。\n': 'Sets the selected custom slot to the ST default and keeps the other slots.\n',
    '\n请确认机身为 ILCE-7CM2、固件 2.01，电量充足（建议至少 50%）。\n'
    '其它项目修改的固件可能与本工具冲突。\n'
    '操作和完整读回期间保持供电、USB 连接，不要关机或拔线。\n确认供电充足并开始？':
        '\nConfirm the body is an ILCE-7CM2 on firmware 2.01 with enough battery (at least 50% recommended).\n'
        'Firmware modified by other projects may conflict with this tool.\n'
        'Keep power and USB connected during the operation and full readback; do not power off or unplug.\n'
        'Power is sufficient; start now?',

    # Running and completion status
    '正在执行：': 'Running: ',
    '。详细日志持续保存。': '. The detailed log is saved continuously.',
    '名称已写好，程序尚未写入。按弹窗断电重开、接回 USB，再点击首页“继续安装”。':
        'Names are written; programs are not yet. Cold-reload as prompted, reconnect USB, then click "Continue installation" on Home.',
    '名称已写好，程序尚未写入。按弹窗断电重开、接回 USB，再点自定义外观页“继续槽位更改”。':
        'Names are written; programs are not yet. Cold-reload as prompted, reconnect USB, then click "Continue slot changes" on the Custom Creative Looks page.',
    '批量外观写入完成，已完整读回；按弹窗统一断电重开即可加载。':
        'Batch look write finished with full readback; cold-reload once as prompted to load it.',
    'FL23 操作完成，写入与完整读回均已结束。重开相机后生效，无需再点核对。':
        'FL23 operation finished; write and full readback have ended. It takes effect after the camera restarts; no verification click is needed.',
    '读写已结束。拔 USB → 等灯停 → 关机并等灯灭 → 取电池至少 1 分钟 → 开机 → 接回 USB → 点击首页“继续安装”。详见弹窗。':
        'Reading and writing have ended. Unplug USB → wait for the light to stop → power off and wait until dark → '
        'remove the battery for at least 1 minute → power on → reconnect USB → click "Continue installation" on Home. See the dialog.',
    '读写已结束。拔 USB → 等灯停 → 关机并等灯灭 → 取电池至少 1 分钟 → 开机；详见弹窗。':
        'Reading and writing have ended. Unplug USB → wait for the light to stop → power off and wait until dark → '
        'remove the battery for at least 1 minute → power on. See the dialog.',
    '名称与只读挂载已确认；程序尚未安装，请点首页“继续安装”。':
        'Names and the read-only mount are confirmed; programs are not installed yet. Click "Continue installation" on Home.',
    '名称与只读挂载已确认；程序尚未安装，请点自定义外观页“继续槽位更改”。':
        'Names and the read-only mount are confirmed; programs are not installed yet. Click "Continue slot changes" on the Custom Creative Looks page.',
    '完成。请按日志提示进行下一步。': 'Done. Follow the log for the next step.',
    '操作停止：': 'Operation stopped: ',
    '进程异常退出，退出码 ': 'the process exited abnormally, exit code ',
    '。请导出诊断包。': '. Please export a diagnostic bundle.',
    '恢复尚未完成：写入和读回已结束，必须断电重启、接回 USB，再点“重启后核对并完成恢复”。':
        'Restore not finished: write and readback have ended. Power-cycle, reconnect USB, then click "Verify after restart and finish restore".',
    '原厂恢复核对通过，旧安装状态已清除。请继续检查机身拍摄和回放；重新安装请点首页“一键安装”。':
        'Factory restore verified and old installation state cleared. Check shooting and playback on the camera; to reinstall, use "One-click install" on Home.',
    '本次恢复尚未写入。按弹窗完整断电、接回 USB，再点“断电后重试恢复”。':
        'This restore has not written anything yet. Do a full power-cycle as prompted, reconnect USB, then click "Retry restore after power-cycle".',
    '原厂恢复已核对通过；已清除旧安装状态。历史诊断日志保留，新安装从头开始。':
        'Factory restore verified; old installation state cleared. Historical diagnostic logs are kept and a new installation starts fresh.',
    '原厂恢复写入已完成；旧的声音记录已停用（文件保留），之后的声音操作不再受它们影响。':
        'Factory restore write finished; old sound records are retired (files kept) and no longer affect later sound actions.',
    'USB 只读检测通过': 'USB read-only check passed',
    '已完成 %d 轮、共 %.1f MB 程序文件只读传输，持续 %.0f 秒，每轮字节一致。\n\n没有写入固件、设置或运行原生写入程序。\n\n%s':
        'Completed %d rounds, %.1f MB of read-only program-file transfer over %.0f seconds; every round matched byte for byte.\n\n'
        'No firmware or settings were written and no native write program ran.\n\n%s',
    '请查看日志并换线后重测。': 'Check the log, change the cable and test again.',
    'USB 连接检测未完成': 'USB connection check incomplete',
    'USB 连接检测未通过': 'USB connection check failed',
    '导出失败': 'Export failed',

    # Completion summary
    '上次安装尚未结束，请使用“继续安装”。': 'The last installation has not finished; use "Continue installation".',
    '本次所选操作已完成，程序与设置核对通过。': 'The selected operations are complete; programs and settings were verified.',
    '请在机身检查预览、拍摄和回放。': 'Check preview, shooting and playback on the camera.',
    'FL2／FL3：': 'FL2/FL3: ',
    '已启用': 'enabled',
    '本次未改动': 'unchanged this time',
    '自定义外观：已写入': 'Custom looks: written',
    '  自订 %s：%s': '  Custom %s: %s',
    '沿用文件名称': 'name from file',
    '自定义外观：本次未改动': 'Custom looks: unchanged this time',
    '电子快门声：': 'Electronic shutter sound: ',
    '已启用支持，请检查机身音频信号设置': 'support enabled; check the camera Audio signals setting',
    '本次未选择': 'not selected this time',
    'Lightroom 插件：已安装，请在插件管理器中启用': 'Lightroom plugin: installed; enable it in the Plug-in Manager',
    '竖屏拍摄信息：已保存开启，并已核对重开后的运行状态；无需每次连接电脑开启。':
        'Vertical shooting information: saved as on and verified after restart; no need to enable it from the computer each time.',
    '竖屏拍摄信息：旧版仅开启本次运行。': 'Vertical shooting information: the old version enabled it for this session only.',
    '旧任务未保存为开机默认；可在新版“竖屏显示”页保存开启。':
        'The old task did not save it as the startup default; save it as on from the "Vertical Display" page.',
    '竖屏拍摄信息：本次未改动': 'Vertical shooting information: unchanged this time',
    '本次安装已结束，无需为了查看结果再次刷写。': 'This installation is finished; no rewrite is needed to view the result.',

    # Reload guide
    _pinned('reloadguide', 'STEPS', 'cdb0d55fdb83'):
        'Act only after the app clearly shows "Reading and writing have ended".\n\n'
        '1. Unplug the camera USB cable and disconnect any other external power.\n'
        '2. Wait for the camera access light to stop blinking; do not remove the battery while it blinks.\n'
        '3. Switch the camera OFF and wait until the screen and access light are completely dark.\n'
        '4. Remove the battery and leave the camera without battery, USB or other power for at least 1 minute.\n'
        '5. Put the battery back and switch the camera on.',
    '本轮 LUT 刷新候选的写入和完整读回已结束，尚未证明横线与实时预览问题已修复。\n\n':
        'Write and full readback of this LUT refresh candidate have ended; this does not yet prove the line and live preview problems are fixed.\n\n',
    '\n\n下一步：保持原先能复现横线的帧率和拍摄模式，检查高刷新率取景器、背屏及录像；'
    '在 ST 与六个自定义槽之间反复切换，确认预览及时变化，再拍照并回放。\n\n'
    '接回 USB 后，在本测试区域点击“断电重开后只读核对本轮测试”。'
    '只在完成机身检查后勾选验收；磁盘读回和 AP 加载核对不等于 CP RAM 或屏幕时序验证。'
    '\n\n若切换后色彩不更新或出现新异常，保留日志，可用本测试区域的“撤回测试：恢复旧版刷新方式”撤回本轮候选。':
        '\n\nNext: keep the frame rate and shooting mode that reproduced the line; check the high-refresh viewfinder, rear screen and recording. '
        'Switch repeatedly between ST and the six custom slots, confirm the preview changes promptly, then shoot and play back.\n\n'
        'After reconnecting USB, click "Read-only check of this test after the cold reload" in this test area. '
        'Tick acceptance only after checking the camera; disk readback and AP load checks are not CP RAM or display timing verification.'
        '\n\nIf colors do not update after switching or a new problem appears, keep the log and use "Withdraw test: restore the old refresh method" here.',
    '本次恢复尚未开始写入，连接操作已结束。相机里有同名临时工作文件，'
    '无法仅凭文件名确定它由哪次操作留下；本次没有覆盖它，也没有标记恢复完成。\n\n'
    '先完整断电，让临时服务状态退出，再重新读取当前相机并生成恢复计划。\n\n':
        'This restore has not started writing and the connection has ended. The camera holds a temporary work file with the same name, '
        'and its origin cannot be determined from the name alone; it was not overwritten and the restore is not marked complete.\n\n'
        'Do a full power-cycle so the temporary service state exits, then read the current camera again and build a new restore plan.\n\n',
    '\n\n下一步：接回 USB 海量存储，点击恢复页“断电后重试恢复（本次尚未写入）”。'
    '工具会重新读取当前程序、设置和名称，从现况恢复原厂功能，不需要旧 LUT 任务。'
    '如果仍提示临时文件冲突，请导出新的诊断包；不要手动删除相机文件。'
    '\n\n这是恢复写入前的重试步骤，不是“恢复完成”或“重启后核对”。':
        '\n\nNext: reconnect USB in Mass Storage and click "Retry restore after power-cycle (nothing written yet)" on the restore page. '
        'The tool reads the current programs, settings and names again and restores factory functions from the current state; no old LUT task is needed. '
        'If the temporary file conflict persists, export a new diagnostic bundle; do not delete camera files by hand.'
        '\n\nThis is a retry before the restore write, not "restore complete" or "verify after restart".',
    '恢复尚未完成：本次写入和完整读回已结束，还必须重启后核对相机实际加载状态。\n\n':
        'Restore not finished: write and full readback have ended, and the actual loaded state must still be verified after a restart.\n\n',
    '\n\n下一步：确认相机能正常取景，接回 USB 海量存储，点击恢复页上方'
    '“重启后核对并完成恢复”，或下方“重启后核对并完成恢复（恢复写入后必做）”。\n\n'
    '只有核对通过才显示恢复完成。核对失败时保留日志，不要把写入结束当成恢复完成。'
    '弹窗“确定”只关闭说明，不会自动完成核对。':
        '\n\nNext: confirm live view works, reconnect USB in Mass Storage, then click "Verify after restart and finish restore" '
        'on the restore page.\n\n'
        'The restore is shown as complete only after verification passes. If verification fails, keep the log; a finished write is not a finished restore. '
        'OK only closes this dialog and does not complete verification.',
    '名称阶段已完成，程序尚未写入。旧资源仍被相机占用，只读挂载尚未恢复；需要先释放旧资源，再继续剩余安装。\n\n':
        'The name stage is complete; programs are not written yet. Old resources are still in use and the read-only mount has not returned; '
        'they must be released before the rest of the installation continues.\n\n',
    '\n\n开机后先不用拍照。接回 USB 海量存储，再点': '\n\nNo need to shoot after power-on. Reconnect USB in Mass Storage, then click ',
    '首页“继续安装”': '"Continue installation" on Home',
    '自定义外观页“继续槽位更改”': '"Continue slot changes" on the Custom Creative Looks page',
    '。工具会核对新的冷启动和只读挂载，然后继续剩余程序，不重复写名称、不重装驱动。\n\n程序写完后还会提示最终重开，让新功能生效。点确定只关闭说明。':
        '. The tool verifies the new cold boot and read-only mount, then continues with the remaining programs without rewriting names or reinstalling drivers.\n\n'
        'After the programs are written you will be asked for a final restart so the new features take effect. OK only closes this dialog.',
    '\n\n这次“启用 FL2／FL3”已写入程序文件。此前恢复原厂后的重开只加载了原厂状态；本次新的修改需要再次重开才能生效。':
        '\n\n"Enable FL2/FL3" has written the program files. The restart after the earlier factory restore loaded only the stock state; '
        'this new change needs another restart to take effect.',
    '接回 USB，选择海量存储，再点首页“继续安装”。工具先核对加载，不重复刷写。':
        'Reconnect USB, select Mass Storage, then click "Continue installation" on Home. The tool verifies loading first and does not rewrite.',
    '在相机中确认 FL2／FL3 能选择、拍摄及回放，即可使用。不必再接电脑点击核对；如需排查，可使用 FL23 页的可选诊断。':
        'Check on the camera that FL2/FL3 can be selected, shot and played back, and you are done. No computer verification is needed; '
        'for troubleshooting, use the optional diagnostic on the FL2 / FL3 page.',
    '此次断电仅用于清除临时试听、恢复原声，不是保存声音的前置条件。开机确认原声、拍摄及回放正常，可点声音页“已断电恢复原声，记录恢复完成”。保存当前转换片段不需要先执行这一步。':
        'This power-cycle only clears the temporary audition and restores the original sound; it is not required before saving. '
        'After power-on, confirm the original sound, shooting and playback, then you may click "Power-cycled and original sound restored; record recovery" on the sound page. '
        'Saving the current converted clip does not need this step.',
    '开机后用电子快门拍摄，检查声音、音量及拍摄／回放。保存自定义声音后，可在声音页核对加载状态。':
        'After power-on, shoot with the electronic shutter and check the sound, volume, shooting and playback. '
        'After saving a custom sound, you can verify the loaded state on the sound page.',
    '竖屏开关和线框引用已保存。重开后先横握检查 Fn 网格和右移选择，再分别左右竖握检查 Fn、创意外观等子菜单边框；最后检查拍摄和回放。已知问题：竖屏创意外观选择页的外框仍偏粗；刻度已横向显示，但橙色指针朝向尚未修正。':
        'The vertical switch and frame references are saved. After restarting, first hold the camera horizontally and check the Fn grid and moving the selection right, '
        'then hold it vertically to the left and right and check Fn, Creative Look and other submenu frames; finally check shooting and playback. '
        'Known issues: the frame on the vertical Creative Look selection page is still too thick; the scale is horizontal, but the orange pointer direction is not yet corrected.',
    '竖屏已先关闭，原线框引用与资源索引已恢复，辅助别名已移除。如果当前运行仍引用追加图片，会暂时保留少量图片尾部数据，避免破坏当前显示；这不影响关闭效果，也不需要再点按钮。重开后确认横握／竖握显示及拍摄正常。':
        'Vertical display was turned off first, the original frame references and resource indexes are restored, and helper aliases are removed. '
        'If the running camera still references appended images, a small image tail is kept temporarily to avoid breaking the current display; '
        'this does not affect disabling and needs no further click. After restarting, confirm horizontal/vertical display and shooting work.',
    '在 ST 与修改的槽位间随机切换，确认实时预览立即更新，再拍照并回放。单独外观写入无需接电脑另点核对；若名称阶段提示尚未写程序，请接回并点“继续槽位更改”。':
        'Switch randomly between ST and the changed slots, confirm the live preview updates immediately, then shoot and play back. '
        'A standalone look write needs no separate computer verification; if the name stage reports programs are not written yet, reconnect and click "Continue slot changes".',
    '确认能正常取景，检查菜单／外观预览，并拍照、回放。若本页显示待核对，请接回 USB 后点击该页明确列出的核对按钮。':
        'Confirm live view works, check the menus and look preview, then shoot and play back. '
        'If this page shows a pending verification, reconnect USB and click the verify button listed on that page.',
    '加载核对只读取状态，不会再刷一次。': 'Load verification only reads state and never writes again. ',
    '\n\n下一步：': '\n\nNext: ',
    '点“确定”只关闭说明，不会自动断电或代替你确认测试。': 'OK only closes this dialog; it does not power-cycle the camera or confirm the test for you.',
    '试听已准备好，请保持相机开机': 'Audition ready; keep the camera on',
    '试听已准备好。拔 USB 并保持开机，试拍后接回即可直接保存。':
        'Audition ready. Unplug USB and keep the camera on; after a test shot, reconnect and you can save directly.',
    '相机读写已结束。当前声音只供临时试听，尚未永久保存。\n\n'
    '1. 拔掉 USB，保持相机开机；不要关机、取下电池或更改音频信号设置。\n'
    '2. 使用电子快门拍一张，检查声音内容、音量、音调／速度，以及拍摄和回放是否正常。\n'
    '3. 接回 USB 海量存储，点击“保存当前自定义声音”。可以直接保存，无需先恢复原声。\n'
    '4. 保存写入完成后，再按弹窗完整断电重开，检查是否永久生效。\n\n'
    '“确认试听正确”只记录试听结果，是可选步骤。\n'
    '本弹窗的“确定”只关闭说明，不代表已确认试听正确。':
        'Camera reading and writing have ended. The current sound is a temporary audition and is not saved permanently.\n\n'
        '1. Unplug USB and keep the camera on; do not power off, remove the battery or change the Audio signals setting.\n'
        '2. Take a shot with the electronic shutter and check the sound content, volume, pitch/speed, shooting and playback.\n'
        '3. Reconnect USB in Mass Storage and click "Save current custom sound". You can save directly without restoring the original sound first.\n'
        '4. After the save write finishes, do a full cold reload as prompted and check that it is permanent.\n\n'
        '"Confirm audition is correct" only records the audition result and is optional.\n'
        'OK in this dialog only closes it and does not confirm the audition.',
    '试听结果已记录': 'Audition result recorded',
    '试听记录已保存；可直接保存当前自定义声音，无需先断电恢复。':
        'Audition record saved; you can save the current custom sound directly without a power-cycle first.',
    '这一步只记录试听结果。\n\n可直接点击“保存当前自定义声音”，无需先断电或记录恢复。'
    '若不满意，调整片段后重新转换；需要清除临时试听时，再按断电步骤恢复原声。':
        'This step only records the audition result.\n\nYou can click "Save current custom sound" directly, without a power-cycle or recovery record. '
        'If you are not satisfied, adjust the clip and convert again; to clear the temporary audition, follow the power-cycle steps to restore the original sound.',
    '保存尚未开始，请先转换片段': 'Save not started; convert a clip first',
    '等待操作：选择声音文件，转换后即可直接保存。': 'Waiting: choose a sound file; after converting you can save directly.',
    '尚无可保存的转换片段，本次没有相机写入。\n\n选择音频或视频，设置起点和长度，'
    '点击“转换所选片段”；转换成功后直接点击“保存当前自定义声音”。试听是可选步骤。':
        'There is no converted clip to save, and nothing was written to the camera.\n\nChoose audio or video, set the start and length, '
        'click "Convert selected clip", then click "Save current custom sound" after it succeeds. Audition is optional.',

    # Connection notice
    _pinned('connectionguide', 'TITLE', 'eea21d2bacd2'): 'Read this before connecting the camera',
    _pinned('connectionguide', 'TEXT', '577c0e325328'):
        'While this tool connects to the camera or switches drivers, the camera showing "Please check the connected device" is normal.\n\n'
        'The computer may not show a drive letter for the camera at that point. Do not judge a failed connection from that camera message alone; '
        "check this tool's progress and full log. Success is determined by the tool's actual result.\n\n"
        'The Windows "two-stage drivers" step first prepares administrator rights and the installer, then switches the camera mode. '
        'When 0336 appears its driver is handled automatically, and after installation the app waits for the interface again; '
        'there is no need to race Device Manager.\n\n'
        'On macOS, camera operations open a Terminal window that uses sudo to take over USB; enter your Mac login password there. '
        'The app never reads or stores the password. Closing the window before entering the password does not start a camera operation; '
        'once an operation starts, wait for it to finish and do not power off or unplug.\n\n'
        'Use Mass Storage mode and keep USB and power stable. '
        'Do not unplug, power off or reinstall drivers repeatedly because of this message while a task runs. '
        'Only act when the app explicitly asks you to reconnect and all reading and writing have ended.\n\n'
        'If the tool itself reports an error, keep and export a diagnostic bundle; this normal connection message does not mean other errors can be ignored.',

    # Zadig guide
    _pinned('zadigguide', 'TITLE', 'aa45df96d626'): 'Install drivers manually with Zadig',
    _pinned('zadigguide', 'TEXT', 'c55d7e847c5b'): """If automatic driver installation fails, installing manually with Zadig works on most computers. Nothing is written to the camera; only the drivers this computer uses for the camera's two USB identities are changed.

The camera has two USB identities, and both need a driver:
· Normal connection: shown in Zadig as ILCE-7CM2, USB ID 054C 0E8A. Appears when the camera is on, set to Mass Storage and connected.
· Service mode: shown in Zadig as Sony USB Device, USB ID 054C 0336. Appears only after this app authenticates; the camera usually shows "Please check the connected device".

Preparation
1. Click "Open Zadig download page" below and download the latest zadig-x.x.exe (a single file, no installation).
2. Turn the camera on and set USB Connection to "Mass Storage" in the menu. Use a data cable straight to the computer, without a dock; on a desktop, use a rear port.

Part 1: driver for 0E8A
1. Right-click Zadig and choose "Run as administrator". Answer the update-check question either way.
2. In the Options menu, tick List All Devices. Without it the camera does not appear.
3. Choose ILCE-7CM2 in the drop-down at the top.
4. Check that the USB ID field shows 054C 0E8A. If not, you picked the wrong device; choose another and check again. Never replace drivers for keyboards, mice, USB drives, network adapters or other devices.
5. In the driver box right of the green arrow, use the up/down arrows to select libusbK.
6. Click Replace Driver (Install Driver when no driver is present) and wait 1–2 minutes until it says The driver was installed successfully.
7. Afterwards, the camera drive letter disappearing and the camera showing "Please check the connected device" are both normal.

Part 2: make 0336 appear, then give it a driver
1. Keep Zadig open. On this page, click "Prepare two-stage drivers and test connection".
2. The app authenticates through the new 0E8A driver, after which the camera becomes Sony USB Device (054C 0336).
   · If the log shows the service connection succeeded and driver preparation finished: you are done; go to Part 3.
   · If the log says 0336 has no driver, its interface cannot be opened, or 0336 never appears: do not unplug or turn the camera off; continue with the next step.
3. In Zadig, click Options → List All Devices again to refresh, choose Sony USB Device and check that the USB ID is 054C 0336.
   · If 0336 is not listed, the camera has left service mode: repeat step 1 of this part and refresh Zadig as soon as 0336 appears.
4. Again select libusbK, click Replace Driver or Install Driver, and wait for the success message.

Part 3: power-cycle and test again
1. Unplug USB, turn the camera off and remove the battery for about 1 minute. Put it back, turn the camera on, select Mass Storage and reconnect.
2. Click "Prepare two-stage drivers and test connection" on this page again. When the log shows the service connection succeeded and driver preparation finished, go to Home for the one-click install.

To check: open Windows Device Manager. There should be a "libusbK USB Devices" category containing ILCE-7CM2, and Sony USB Device once 0336 is installed.

Troubleshooting
· libusbK fails to install: run Zadig as administrator again; if it still fails, choose WinUSB instead. This app works with WinUSB, libusbK or libusb0.
· The camera is not in the drop-down: make sure List All Devices is ticked, the camera is on and in Mass Storage, and try another data cable.
· To undo everything: click "Uninstall camera drivers and restore the Windows default" on this page; drivers installed by Zadig are removed too. Then replug USB and the camera appears as a drive again.
""",

    # Look format guide
    _pinned('lookguide', 'TITLE', '029f8d01b792'): 'LUT / DCP formats and color spaces',
    _pinned('lookguide', 'TEXT', '4b3703bba898'): """The camera write page only takes .a7look; .cube or .dcp files are never written directly. The creation tool only converts files on the computer and does not connect to the camera.

1. Which CUBE files does the desktop creator accept?
Input: RGB from Sony's ST (Standard) Creative Look, sRGB-encoded; output: sRGB.
Not S-Log3, S-Log2, HLG, S-Gamut3.Cine, DaVinci Wide Gamut or ACES. An ordinary Rec.709 video LUT is not automatically the same input either; check its transfer function and gamut.
Only LUTs labelled for Sony ST / sRGB photos can be used directly. The .cube extension carries no reliable color space declaration, so the program cannot tell automatically.

2. I only have an S-Log3 LUT. What now?
A LUT such as S-Log3 / S-Gamut3.Cine → Rec.709 cannot be used directly in the current desktop creator. Applied to ST images it gives wrong contrast, exposure or color; renaming the file or editing its header does not fix that.
Re-export a complete "Sony ST / sRGB input → target look → sRGB output" 3D CUBE from your grading software, including the required input and output transforms. Do not just relabel the export as sRGB.
The advanced command line supports an explicit input space with an ST-to-that-space bridge CUBE; the target LUT output must still be sRGB. The current GUI has no Log bridge option, and a bridge does not guarantee Sony's native Log processing.

3. CUBE file structure
A plain-text standalone 3D LUT with LUT_3D_SIZE N; N may be 2–129, commonly 17 / 33 / 65; 33 is recommended.
Exactly N³ rows follow, each with three finite R G B numbers (not 0–255 integer colors); red changes fastest. TITLE is optional; DOMAIN_MIN / DOMAIN_MAX are optional and default to 0 0 0 / 1 1 1.
1D LUTs, 1D shaper + 3D files, .3dl, .look, .xmp and images are not supported. Output outside 0–1 is clipped before fitting; export within 0–1 when possible.

4. What is a DCP?
A .dcp is an Adobe camera profile, not an S-Log3 video LUT. The creator parses the DCP LookTable/tone curve offline and fits it, with no Lightroom, development plugin, renderer configuration or network.
A DCP is fitted approximately through a built-in shared ST mapping; the source camera's sensor matrices and HueSat calibration are not copied, and full Adobe rendering is not claimed. A standalone CUBE does not automatically become a Lightroom RAW DCP profile.

5. How do I write it?
Create a new .a7look → add an operation → choose a slot and "Write A7Look" → choose the file and enter the in-camera name → review and apply. Several slots can be written together; slots not listed stay unchanged.
After writing, cold-reload as prompted. The result is a fitted in-camera table approximation; a 65-point CUBE does not mean every sample is kept, and an exact match with the original DCP / LUT is not guaranteed.""",

    # Voice guide pack, restore sources and backups (dev, Oct 28)
    '清理无障碍语音包，并将语音指南置灰（安装必选）': 'Remove the accessibility voice pack and grey out Voice Guide (required for install)',
    '删除十种语言的菜单朗读音频，约释放 283 MiB；不删除对焦提示音或快门声音。只能通过一键恢复补回。':
        'Deletes the menu read-aloud audio in ten languages, freeing about 283 MiB. Focus beeps and shutter sounds are kept. '
        'Only One-click restore can bring it back.',
    '备份与恢复来源：可在“恢复原厂功能”页备份当前项目与语音。为尊重原厂版权、降低包括 DMCA 在内的法律风险，安装包不附带完整官方固件或原厂语音包。一键恢复的程序、设置及语音来源由你提供：使用可用同机原始备份，或自行从索尼官方下载 ILCE-7CM2 2.01 BODYDATA.DAT。普通安装不强制先备份或下载；恢复也不保证能救回无法开机的相机。':
        'Backup and restore sources: the "Restore factory functions" page can back up the current project state and voice files. '
        "To respect Sony's copyright and reduce legal risk, including DMCA, the package does not include full official firmware or Sony's voice pack. "
        'You provide the source of programs, settings and voice files for One-click restore: a usable original backup of this body, '
        'or ILCE-7CM2 2.01 BODYDATA.DAT downloaded yourself from Sony. A normal install does not require a backup or download first; '
        'restore cannot guarantee recovery of a camera that no longer starts.',
    '查看可选备份与官方固件恢复来源': 'View optional backups and official-firmware restore sources',
    '恢复出厂、卸载驱动和删除外观不会混入安装流程。自定义声音请在“快门声音”中转换后选择机械／电子／两者并保存，试听可选。':
        'Factory restore, driver removal and look deletion are never part of the install. For a custom sound, convert it on "Shutter sound", '
        'choose mechanical / electronic / both and save; audition is optional.',
    '一键恢复本项目功能：六槽回 ST、快门回机械、关闭静音模式和新增电子音效。保留机身校准；语音包可选择是否同时恢复。':
        "One-click restore of this project's functions: six slots back to ST, shutter back to mechanical, silent mode and the added "
        'electronic sound turned off. Body calibration is kept; restoring the voice pack is optional.',
    '恢复来源（程序、设置及所选语音均从你的本地文件取得）': 'Restore source (programs, settings and selected voice files come from your local file)',
    '官方 2.01 BODYDATA.DAT': 'Official 2.01 BODYDATA.DAT',
    '或：同机原始备份': 'Or: original backup of this body',
    '应用不内置原厂恢复文件。为尊重版权、降低包括 DMCA 在内的法律风险，一键恢复需使用你自行取得的官方 2.01 固件，或可用的同机原始备份。普通安装不要求预先下载；这项说明适用于所有原厂恢复，不仅是语音包。':
        'The app has no built-in factory restore files. To respect copyright and reduce legal risk, including DMCA, One-click restore needs '
        'official 2.01 firmware you obtained yourself or a usable original backup of this body. A normal install needs no download first; '
        'this applies to every factory restore, not only the voice pack.',
    '打开索尼官方 2.01 固件下载页': "Open Sony's official 2.01 firmware download page",
    '同时恢复无障碍语音包，并解除语音指南置灰': 'Also restore the accessibility voice pack and un-grey Voice Guide',
    '勾选时补回语音文件并解除置灰；不勾选则不补回已删除的语音，已禁用的语音指南保持关闭、置灰。':
        'When ticked, the voice files are written back and Voice Guide is un-greyed. When not ticked, deleted voice files are not restored '
        'and the disabled Voice Guide stays off and greyed out.',
    '开始一键恢复': 'Start one-click restore',
    '点击开始；写入后按提示重启，再点同一个按钮继续完成恢复。':
        'Click Start. After writing, restart as prompted, then click the same button to finish the restore.',
    '上次恢复记录（可选）': 'Last restore record (optional)',
    '备份当前项目状态（可选）': 'Back up the current project state (optional)',
    '保存位置': 'Save location',
    '同时备份语音指南音频（约 287 MiB，耗时较长）': 'Also back up Voice Guide audio (about 287 MiB, takes longer)',
    '备份当前程序、外观、设置和名称（只读）': 'Back up current programs, looks, settings and names (read-only)',
    '保存创建时的当前项目状态，可能已修改；不是原厂基准或完整相机镜像。项目检查点可用下方“使用旧备份”入口恢复；语音包另存，不包含在当前项目还原范围内。安装和一键恢复无需先备份。':
        'Saves the project state as it is now, which may already be modified; it is not a factory baseline or a full camera image. '
        'Restore project checkpoints with "Use an old backup" below; the voice pack is saved separately and is not part of a project restore. '
        'Install and One-click restore need no backup first.',
    '恢复尚未完成：写入已结束。请按提示重启、接回 USB，然后点击上面的“继续完成一键恢复”；不会重复刷写程序。':
        'Restore not finished: writing has ended. Restart as prompted, reconnect USB, then click "Finish one-click restore" above; '
        'programs are not written again.',
    '恢复尚未完成：写入和读回已结束，必须断电重启、接回 USB，再点“继续完成一键恢复”。':
        'Restore not finished: writing and readback have ended. Cold-reload the camera, reconnect USB, then click "Finish one-click restore".',
    '继续完成一键恢复': 'Finish one-click restore',
    '本机测试：已配置本地原厂来源，以上留空也可恢复；手动选择文件优先，不跳过恢复与读回。':
        'Local test: a local factory source is configured, so restore works with the fields above empty. A manually chosen file takes priority; '
        'restore and readback are never skipped.',
    '“核对旧备份恢复后的加载状态”只用于“使用旧备份回到过去的状态”。\n用原厂来源恢复后，应点“继续完成一键恢复”。\n现在改为核对原厂恢复？':
        '"Verify load state after old-backup restore" is only for "Use an old backup to return to a past state".\n'
        'After restoring from a factory source, click "Finish one-click restore".\nVerify the factory restore instead?',
    '无障碍语音包是什么': 'What is the accessibility voice pack?',
    '这是相机为视障使用者提供的菜单朗读／语音指南，包含十种语言的音频，约占 283 MiB。\n\n一键安装会关闭语音指南、将相关机内选项置灰，重开核对后删除音频，为竖屏等资源腾出空间。不会删除语言索引、对焦提示音、原生快门声或自定义电子快门音效。\n\n该项属于新安装方案，不能取消。仅“一键恢复原厂功能”会从用户的官方固件或可用同机备份补回；机内初始化不能恢复。需要语音指南辅助操作的用户请勿使用本安装方案。':
        "It is the camera's menu read-aloud / Voice Guide for visually impaired users: audio in ten languages, about 283 MiB.\n\n"
        'One-click install turns Voice Guide off, greys out the related in-camera options, and deletes the audio after the reload check, '
        'freeing space for resources such as Vertical Display. The language index, focus beeps, the native shutter sound and the custom '
        'electronic shutter sound are not deleted.\n\n'
        'This is part of the new install plan and cannot be skipped. Only "One-click restore factory functions" brings it back, from your '
        "official firmware or a usable backup of this body; the camera's own reset cannot. If you rely on Voice Guide, do not use this install plan.",
    '请选择恢复来源': 'Choose a restore source',
    '请先选择官方 ILCE-7CM2 2.01 BODYDATA.DAT，或可用的同机原始备份；程序、设置及所选语音均从该来源取得。':
        'First choose the official ILCE-7CM2 2.01 BODYDATA.DAT or a usable original backup of this body; programs, settings and the selected '
        'voice files all come from it.',
    '语音资源操作完成': 'Voice resource operation complete',
    '机身取景、拍照与回放仍请实际检查。': 'Still check the viewfinder, shooting and playback on the camera.',
    '上次操作未完成或尚未开始，日志已保留。选择恢复来源后，点击“开始一键恢复”。':
        'The last operation did not finish or did not start; its log is kept. Choose a restore source, then click "Start one-click restore".',
    '语音文件已完整写回；关闭限制已解除，语音指南仍保持关闭，可在机内自行开启。':
        'The voice files were fully written back and the off-lock is removed. Voice Guide stays off; you can turn it on in the camera.',
    '当前状态备份完成': 'Current-state backup complete',
    '上次恢复已完成': 'The last restore is complete',
    '，按本次选择保留语音禁用及置灰。': '; as chosen, voice stays disabled and greyed out.',
    '已保存程序、外观、设置和名称，并通过本地校验。没有写入相机。\n这是当前状态备份，不是原厂基准。\n保存位置：':
        'Programs, looks, settings and names were saved and passed the local check. Nothing was written to the camera.\n'
        'This is a backup of the current state, not a factory baseline.\nSaved to: ',
    '\n语音包也已另存；当前项目还原不会自动写回语音包。':
        '\nThe voice pack was saved separately too; a project restore does not write it back automatically.',
    '重开后继续完成恢复，再清除私有音效文件。\n': 'After the reload, finish the restore, then remove the private sound files.\n',
    '先关闭语音指南并将机内语音选项置灰；写入后须按提示重开，再点同一按钮核对并删除十份语音音频。不会删除索引、对焦提示音或快门音频。\n':
        'First turns Voice Guide off and greys out the in-camera voice options. After writing, reload as prompted, then click the same button '
        'to verify and delete the ten voice audio files. The index, focus beeps and shutter audio are not deleted.\n',
    '将移除项目程序修改、将六个自订栏位设为 ST，快门设回机械并关闭新增电子快门音效；旧配方不找回。':
        'Removes project program changes, sets the six custom slots to ST, sets the shutter back to mechanical and turns off the added '
        'electronic shutter sound; former recipes are not recovered.',
    '从所选官方 2.01 文件或语音备份完整补回资源，核对全部文件后再解除限制。\n':
        'Fully writes the resources back from the selected official 2.01 file or voice backup, and removes the lock only after every file is verified.\n',
    '本次同时补回语音包并解除置灰；': 'This run also restores the voice pack and un-greys it; ',
    '本次保留语音已删除与置灰状态；': 'This run keeps the voice files deleted and greyed out; ',

    # Vertical display resources (dev)
    '采用与 M4 相同的原生资源分流：横／竖屏各自读取独立资源，保留原图像 ID 和原生刻度绘制。从旧版升级时先撤回补偿并按提示重开，再点开启继续；新竖屏资源完整复制与读回后才保存开启。资源约占 28 MiB，空间不足会停止；可在恢复页选择清理语音，工具不会自动删除。':
        'Uses the same native resource split as the M4: landscape and portrait read separate resources, keeping the original image IDs and '
        'native scale drawing. When upgrading from the old version, the compensation is first withdrawn and you reload as prompted, then click '
        'Enable to continue; the switch is saved only after the new portrait resources are fully copied and read back. The resources take about '
        '28 MiB and the step stops if space is short; you can choose to remove the voice pack on the restore page, the tool never deletes it automatically.',
    '当前为原生竖屏路径候选，尚未真机验收。重开后请检查横握／两侧竖握的 Fn、外框、橙色指针、触摸／按键方向及拍摄回放。':
        'This native portrait path is a candidate, not yet accepted on a real camera. After the reload, check Fn, the frame, the orange pointer, '
        'touch / button directions, shooting and playback in landscape and in both portrait grips.',
    '\n\n重开后接回 USB 海量存储，再点击“开启竖屏显示”；一键安装则点击“继续安装”。程序会核对已加载的原生路径，完整复制并读回三份竖屏资源后才保存开启。':
        '\n\nAfter the reload, reconnect USB Mass Storage and click "Enable Vertical Display" (for One-click install, click "Continue installation"). '
        'The app verifies the loaded native path and saves the switch only after the three portrait resources are fully copied and read back.',
    '旧竖屏引用和刻度补偿已撤回，尚未复制独立竖屏资源。请先让相机加载原生绘制路径。\n\n':
        'The old portrait references and scale compensation were withdrawn; the separate portrait resources are not copied yet. '
        'First let the camera load the native drawing path.\n\n',
    '独立竖屏资源与原生开关已准备。重开后先横握检查 Fn 网格和右移选择，再分别左右竖握检查 Fn、创意外观外框、橙色指针和触摸／按键方向，最后检查拍摄和回放。此候选尚未真机验收，不把文件读回当成显示正常。':
        'The separate portrait resources and native switch are ready. After the reload, first check the Fn grid and moving right in landscape, '
        'then in left and right portrait grips check Fn, the Creative Look frame, the orange pointer and touch / button directions, and finally '
        'shooting and playback. This candidate is not yet accepted on a real camera; file readback does not prove the display is correct.',

    # Voice guide reload steps (dev)
    '\n\n重开后接回 USB 海量存储，再点击首页“继续安装”。程序会核对实际加载的关闭限制；核对不符时不删除或写回语音文件。':
        '\n\nAfter the reload, reconnect USB Mass Storage and click "Continue installation" on Home. The app verifies the loaded off-lock; '
        'if it does not match, no voice file is deleted or written back.',
    '\n\n重开后语音指南保持关闭，可以在机内按需要开启。请检查菜单、取景和拍摄。':
        '\n\nAfter the reload Voice Guide stays off; you can turn it on in the camera if needed. Check the menus, viewfinder and shooting.',
    '\n\n下一步：确认相机能正常取景，接回 USB 海量存储，点击恢复页“继续完成一键恢复”。\n\n只有核对通过才显示恢复完成。核对失败时保留日志，不要把写入结束当成恢复完成。弹窗“确定”只关闭说明，不会自动完成核对。':
        '\n\nNext: confirm the camera shows a normal viewfinder image, reconnect USB Mass Storage and click "Finish one-click restore" on the restore page.\n\n'
        'Restore is shown as complete only after verification passes. If verification fails, keep the log; the end of writing is not a finished restore. '
        'OK only closes this note and does not complete verification.',
    '语音指南关闭限制及菜单置灰已写入，尚未删除音频。必须先让相机加载关闭限制与菜单禁用状态。\n\n':
        'The Voice Guide off-lock and greyed-out menu are written; the audio is not deleted yet. The camera must first load the off-lock and disabled menu.\n\n',
    '语音文件已完整写回并读回，关闭限制已解除。\n\n': 'The voice files were fully written back and read back; the off-lock is removed.\n\n',

    # Shutter sound page (dev): separate mechanical and electronic switches
    '快门声音': 'Shutter sound',
    '分别控制机械快门和电子快门拍摄时，扬声器额外播放的音效；不切换快门类型。':
        'Separately controls the extra speaker sound played for mechanical and electronic shutter shots; the shutter type is not changed.',
    '原厂声音与两个独立开关：查看说明': 'Factory sound and the two separate switches: read more',
    '机械快门 · 扬声器音效': 'Mechanical shutter · speaker sound',
    '只控制扬声器播放的快门音效。关闭后机械结构本身仍有咔嗒声；快门类型、电子快门音效和对焦提示音设置均保持原样。':
        'Controls only the shutter sound played by the speaker. When off, the mechanism itself still clicks; the shutter type, '
        'electronic shutter sound and focus beep settings stay as they are.',
    '开启机械快门音效': 'Turn on mechanical shutter sound',
    '关闭机械快门音效': 'Turn off mechanical shutter sound',
    '电子快门 · 扬声器音效': 'Electronic shutter · speaker sound',
    '原厂电子快门没有快门音效。本区控制新增音效；开启／关闭保留机械快门音效的当前开关及已保存的自定义声音。':
        'The stock electronic shutter has no sound. This section controls the added sound; turning it on / off keeps the mechanical '
        'shutter sound switch and any saved custom sound.',
    '开启电子快门专属音效': 'Turn on electronic shutter sound',
    '关闭电子快门专属音效': 'Turn off electronic shutter sound',
    '自定义快门声音': 'Custom shutter sound',
    '应用范围': 'Apply to',
    '保存到所选快门': 'Save to selected shutter',
    '转换成功后选择应用范围并保存，会开启所选音效；只修改一种时保留另一种的开关和自定义声音。机械快门自定义声音在开启段播放，关闭段静音，机械结构本身仍有声音。临时试听使用电子快门；保存后统一断电加载。':
        'After a successful conversion, choose where to apply it and save; this turns on the selected sound. Changing only one keeps the other '
        "one's switch and custom sound. A custom mechanical sound plays on the opening phase and is silent on the closing phase; the mechanism "
        'itself still makes a sound. Temporary audition uses the electronic shutter; after saving, cold-reload once to load it.',
    '重开后核对声音／完成音效恢复': 'Verify sound after reload / finish sound restore',
    '移除全部自定义音效，关闭电子快门音效': 'Remove all custom sounds and turn off electronic shutter sound',
    '只修改电子快门': 'Electronic shutter only',
    '只修改机械快门': 'Mechanical shutter only',
    '机械和电子都修改': 'Both mechanical and electronic',
    '相机读写已结束。当前声音只供临时试听，尚未永久保存。\n\n1. 拔掉 USB，保持相机开机；不要关机、取下电池或更改音频信号设置。\n2. 使用电子快门拍一张，检查声音内容、音量、音调／速度，以及拍摄和回放是否正常。\n3. 接回 USB 海量存储，选择应用范围后点击“保存到所选快门”。可以直接保存，无需先恢复原声。\n4. 保存写入完成后，再按弹窗完整断电重开，检查是否永久生效。\n\n“确认试听正确”只记录试听结果，是可选步骤。\n本弹窗的“确定”只关闭说明，不代表已确认试听正确。':
        'Camera reading and writing have ended. The current sound is a temporary audition only and is not saved permanently.\n\n'
        '1. Unplug USB and keep the camera on; do not power it off, remove the battery or change the audio signal settings.\n'
        '2. Take one shot with the electronic shutter and check the sound content, volume, pitch / speed, and that shooting and playback work.\n'
        '3. Reconnect USB Mass Storage, choose where to apply it and click "Save to selected shutter". You can save directly without restoring the original sound first.\n'
        '4. After the save is written, do a full cold reload as the dialog describes and check that it is permanent.\n\n'
        '"Confirm audition is correct" only records the audition result and is optional.\n'
        'OK in this dialog only closes the note; it does not confirm the audition.',
    '试听记录已保存；可直接保存到所选快门，无需先断电恢复。':
        'Audition record saved; you can save to the selected shutter directly without a cold reload first.',
    '这一步只记录试听结果。\n\n可直接点击“保存到所选快门”，无需先断电或记录恢复。若不满意，调整片段后重新转换；需要清除临时试听时，再按断电步骤恢复原声。':
        'This step only records the audition result.\n\nYou can click "Save to selected shutter" directly, without a cold reload or recording a restore. '
        'If you are not happy, adjust the clip and convert again; to clear the temporary audition, follow the cold-reload steps to restore the original sound.',
    '尚无可保存的转换片段，本次没有相机写入。\n\n选择音频或视频，设置起点和长度，点击“转换所选片段”；转换成功后直接点击“保存到所选快门”。试听是可选步骤。':
        'There is no converted clip to save yet; nothing was written to the camera.\n\nChoose an audio or video file, set Start and Length, '
        'click "Convert selected clip", then click "Save to selected shutter". Audition is optional.',
    '开机后分别用机械快门和电子快门拍摄，检查扬声器音效按各自开关播放，并确认对焦提示音、拍摄和回放。机械结构本身的咔嗒声仍然存在。保存自定义声音后，可在声音页核对加载状态。':
        'After power-on, shoot once with the mechanical and once with the electronic shutter and check that each speaker sound follows its own switch; '
        'also check focus beeps, shooting and playback. The mechanism itself still clicks. After saving a custom sound, you can verify the load state on the sound page.',

    # Shutter sound guide (shutterguide.py)
    _pinned('shutterguide', 'TITLE', 'e9378a062194'): 'Mechanical and electronic shutter sound',
    _pinned('shutterguide', 'TEXT', '4be96ff09b47'):
        'Applies to: A7C II (ILCE-7CM2), stock firmware 2.01.\n\n'
        '• Stock shutter sounds: the mechanical shutter makes a sound; the electronic shutter has no shutter sound.\n'
        '• "Mechanical shutter sound" on this page means only the extra sound played by the speaker. On / Off controls only that path '
        'and keeps any saved custom sound.\n'
        '• The mechanism itself still clicks. Neither button changes the shutter type, silent mode or focus beep settings.\n'
        '• The added electronic shutter sound has its own On / Off. The single custom entry can change mechanical only, electronic only '
        "or both; changing one keeps the other one's switch and sound.\n"
        '• Saving turns on the selected sound. A custom mechanical sound plays on the opening phase and is silent on the closing phase; '
        'temporary audition still uses the electronic shutter. Removing all custom sounds restores the sound resources and turns off '
        'the added electronic sound.\n'
        '• The camera\'s global "Audio signals" setting can still mute the speaker when it is off; this tool does not change it.\n\n'
        'This split path has been verified offline; sound, timing, shooting and playback still need confirming on a real camera.',

    # Startup consent (disclaimer.py). Wording follows the author's English README
    # notice; the full statement comes from docs/en/notices.md (i18n.DOCUMENTS).
    '使用前请阅读 · A7C II Tools': 'Read before use · A7C II Tools',
    '使用前，请先了解风险': 'Before you start, understand the risks',
    '非官方相机研究工具 · 每次启动均需本人确认': 'Unofficial camera research tool · you must confirm at every launch',
    '使用前必读 · 风险与免责声明': 'Read before use · risks and disclaimer',
    '我已阅读并接受': 'I have read and accept the',
    '<a href="terms">《风险告知与使用声明》</a>': '<a href="terms">Risk notice and use statement</a>',
    '不同意，退出': 'Decline and exit',
    '接受并进入': 'Accept and continue',
    '风险告知与使用声明 · 全文': 'Risk notice and use statement · full text',
    '关闭全文，返回确认': 'Close full text and return',
    '## 风险告知与使用声明': '## Risk notice and use statement',
    _pinned('disclaimer', 'SUMMARY', '6a5e224a7775'): (
        '<p><b>This is an unofficial, independent research tool for learning and technical discussion. '
        'It is not affiliated with, authorized or endorsed by Sony.</b></p>'
        '<h3 style="font-size:21px;color:#a51524;">Important: the camera may be bricked, and recovery is not guaranteed</h3>'
        '<p><b>Modifications can cause boot failure, repeated restarts, crashes during capture or playback, malfunctions or data loss. '
        'They may affect official updates, warranty or repairs, and may require paid repair or mainboard replacement.</b></p>'
        '<p><b>Successful writes, complete readback and passing offline tests do not establish boot safety or stability in every mode. '
        'Name, icon and other display-resource changes also carry risks. New development-version features have not all completed '
        'physical camera acceptance.</b></p>'
        '<p><b>One-click recovery is not a complete system reinstallation and may not recover the camera. Backups, camera initialization '
        'and official updates do not guarantee recovery either. On an error, disconnect or unknown result, stop writing, preserve '
        'diagnostics and do not repeatedly start installation or recovery.</b></p>'
        '<h3 style="font-size:21px;color:#a51524;">No commercial use or profit-making</h3>'
        '<p><b>All commercial use and profit-making are prohibited. The author explicitly opposes paid flashing, paid remote installation, '
        'resale or paid bundles of the tool, paid unlocking, selling activation keys/dongles, and hardware bundles for profit. '
        'This project is provided free of charge. The author offers no paid flashing service and has not authorized anyone to offer '
        "these paid services in the author's name.</b></p>"
        '<h3 style="font-size:19px;color:#a51524;">Do not impersonate Sony or claim author authorization</h3>'
        "<p><b>The author has never authorized anyone to offer paid services, advertise or promise warranty coverage in the author's "
        "or Sony's official name. Do not impersonate Sony, the author or an authorized service provider. Third-party fees imply no "
        'author involvement, approval, endorsement or guarantee.</b></p>'
        '<p><b>Only operate a device you lawfully own or for which the owner has given explicit permission. Back up important data. '
        'Do not proceed if you cannot accept device damage and repair costs.</b></p>'
        '<p><b>Original project code in this distribution uses the standard PolyForm Noncommercial License 1.0.0. Third-party and '
        'earlier licenses are retained separately. This statement does not exclude liability that cannot lawfully be excluded.</b></p>'),

    # Restore page wording still on main (kept so the layer rebases onto either branch)
    '恢复／继续恢复原厂 2.01 功能（无需旧备份）': 'Restore / continue restoring factory 2.01 functions (no old backup needed)',
    '恢复事务（自动识别；也可手动选择）': 'Restore transaction (detected automatically; can also be chosen manually)',
    '恢复事务目录（通常自动）': 'Restore transaction folder (usually automatic)',
    '重启后核对并完成恢复': 'Verify after restart and finish restore',
    '恢复尚未完成：写入与读回已结束。请断电重启、接回 USB，再点击上方按钮核对。':
        'Restore not finished: writing and readback have ended. Cold-reload the camera, reconnect USB, then click the button above to verify.',
    '重新恢复原厂 2.01 功能（无需旧备份）': 'Restore factory 2.01 functions again (no old backup needed)',
    '上次恢复核对已通过。程序、设置、加载状态及只读挂载已核对；当前功能和拍摄验收以机身为准。':
        'The last restore passed verification. Programs, settings, load state and the read-only mount were checked; '
        'check current functions and shooting on the camera itself.',
    '继续恢复／核对未完成事务': 'Continue restoring / verify the unfinished transaction',
    '恢复尚未完成，请继续处理未完成事务；当前不代表已恢复成功。':
        'Restore not finished. Continue the unfinished transaction; the camera is not restored yet.',
    '先只读核对；只有相机内容已改变时才按当前字节写入，已符合原厂的内容不重复写入。\n':
        'Reads and checks first; writes from the current bytes only where camera content has changed, and never rewrites content that already matches the factory state.\n',
    '断电后重试恢复（本次尚未写入）': 'Retry restore after a power cycle (nothing written yet)',
    '本次恢复尚未写入，遇到相机临时文件冲突。请按弹窗完整断电，接回 USB，再点击上方按钮重试；不需要旧 LUT 记录。':
        'Nothing was written: the restore met a conflicting temporary file on the camera. Cold-reload as the dialog describes, '
        'reconnect USB, then click the button above to retry. No old LUT record is needed.',
    '恢复原厂 2.01 功能（上次尚未开始）': 'Restore factory 2.01 functions (last attempt had not started)',
    '上次在 USB 连接阶段停止，尚未开始恢复写入。点击上方按钮，完成系统授权后重新连接。':
        'The last attempt stopped while connecting over USB; no restore write had started. Click the button above, '
        'grant system authorization, and the app reconnects.',
    '根据当前字节继续未完成阶段，已恢复的内容不重复写入；原失败事务保留，结果不明时先读取报告核对。\n':
        'Continues the unfinished stage from the current bytes without rewriting restored content. The failed transaction is kept; '
        'if a result is unknown, its report is read and checked first.\n',
    '核对上次恢复；相机内容若已改变，则按当前字节重新恢复：': 'Verify the last restore; if camera content has changed, restore again from the current bytes: ',
    '继续完成名称／设置恢复：': 'Finish restoring names / settings: ',
}
# Run-log messages from the camera workers live in locale_en_log.py.
EN.update(LOG)
