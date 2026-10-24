"""English for camera-worker messages shown in the run log.

Keyed by the Chinese printed or raised by the worker code (desktop worker,
camera runtime, look engine, sound and driver setup). Only the on-screen log is
translated; worker.log, process.log and diagnostic bundles keep the original
text. Pieces of composed messages (f-strings, concatenation) are listed as
fragments; i18n translates a line only when every piece is covered.
"""

LOG = {
    # Camera runtime: FL23 compatibility checks (camera_runtime/compat.py)
    '不驗證韌體來源。非本倉庫修改的韌體可能與 FL23 衝突，造成相機無法正常啟動；請保留備份。':
        'Firmware origin is not verified. Firmware modified outside this project may conflict with FL23 and stop the camera '
        'from starting normally; keep your backups.',
    'FL23 只適用於 ILCE-7CM2 2.01；請依相機版本頁填寫': 'FL23 only supports ILCE-7CM2 2.01; enter the version shown on the camera',
    '完整還原候選不符': 'Full restore candidate does not match',
    '相容任務來源或目標已變': 'Compatibility job source or target has changed',
    '色彩單元長度不符': 'Color unit length does not match',
    '既有 FL23 色彩資料不完整；拒絕重寫': 'Existing FL23 color data is incomplete; rewrite refused',
    'LUT 相容模式缺少依賴，請更新完整工具並重新開啟 FL23.cmd。':
        'LUT compatibility mode is missing dependencies; update the complete tool and reopen FL23.cmd.',
    '相容候選已變': 'Compatibility candidate has changed',
    'CP FL23 呼叫位置衝突：': 'CP FL23 call position conflict: ',
    '；沒有寫入': '; nothing written',
    '補丁位置越界：': 'Patch position out of range: ',
    '補丁位置衝突：': 'Patch position conflict: ',
    '；沒有寫入；目前位元組(': '; nothing written; current bytes (',
    '。若使用過舊版本，請先依 README 恢復原廠功能後再安裝；保留本次日誌。':
        '. If an older version was used, restore factory functions as the README describes before installing; keep this log.',
    'CP FL23 原生曲線／模式位置衝突：': 'CP FL23 native curve / mode position conflict: ',

    # Camera runtime: core checks (camera_runtime/core.py)
    '未知原生模組': 'Unknown native module',
    '未知的色彩參數／槽組合，拒絕寫入': 'Unknown color parameter / slot combination; write refused',
    '套件資產清單不符': 'Package asset list does not match',
    '機身備份必須包含兩份校驗有效的 BK4': 'A body backup must contain two BK4 copies with valid checksums',
    '補丁窗口重疊': 'Patch windows overlap',
    '候選檔長度被改動': 'Candidate file length was changed',
    '色彩記錄長度不符': 'Color record length does not match',
    '色彩記錄色度尾八項非零': 'The last eight chroma entries of the color record are not zero',
    '補丁窗口前置條件不符': 'Patch window precondition does not match',
    '色彩映射不符': 'Color mapping does not match',
    '目標參數已使用，拒絕覆蓋': 'Target parameter is already in use; overwrite refused',
    '目標色彩槽已有其他參數引用': 'Target color slot is already referenced by another parameter',
    '目標色彩槽已有資料': 'Target color slot already has data',
    '既有風格映射被改動': 'Existing style mapping was changed',
    '既有色彩記錄被改動': 'Existing color record was changed',
    '既有矩陣被改動': 'Existing matrix was changed',
    '設定項目集合改變': 'The set of setting items changed',
    '安裝器結果長度不符': 'Installer result length does not match',
    '安裝器未完整成功；請勿重試或重新開機': 'Installer did not fully succeed; do not retry or restart',
    '寫入前完整檔案雜湊不符': 'Full-file hash before writing does not match',
    '寫入後完整檔案雜湊不符': 'Full-file hash after writing does not match',
    '只校驗模式出現非零寫入': 'Verify-only mode reported a non-zero write',
    '診斷結果過短': 'Diagnostic result is too short',
    '型號欄位、權限或診斷結果不符': 'Model field, permissions or diagnostic result do not match',
    '開機快照結果長度不符': 'Boot snapshot result length does not match',
    '開機快照處理未驗證，請勿重複執行': 'Boot snapshot handling is unverified; do not run it again',
    '不支援此開機快照起始狀態': 'This boot snapshot starting state is not supported',
    '開機快照寫入或讀回不完整': 'Boot snapshot write or readback is incomplete',
    '執行期結果長度不符': 'Runtime result length does not match',
    '執行期身分／結果不符': 'Runtime identity / result does not match',
    '色度不等於供體目標值': 'Chroma does not equal the donor target value',
    '矩陣不等於供體目標值（逐槽）': 'Matrix does not equal the donor target value (per slot)',
    '套件缺少檔案：': 'Package is missing a file: ',
    '第 ': 'Slot ',
    ' 個槽展開後行和不是 1024，拒絕寫入': ': expanded row sums are not 1024; write refused',
    '目標設定讀回不符': 'Target setting readback does not match',
    '原厂对焦框显示尺寸变化：chip': 'Native focus-frame display size changed: chip',
    '会话字段变化：chip': 'Session field changed: chip',
    '發現額外設定變動：chip': 'Unexpected setting change found: chip',
    '，請保存紀錄後檢查': '; keep the record and check it',

    # Camera runtime: macOS USB host (camera_runtime/macos_host.py)
    '若相机屏幕询问 USB 连接方式，请选择第 2 项「影像传输（MSC）」。':
        'If the camera asks for the USB connection type, choose item 2, "Mass Storage (MSC)". ',
    '相机存储卷未能全部卸载，尚未接管 USB。请关闭照片、图像捕捉及使用存储卡的程序后重试。':
        'Not all camera volumes could be unmounted; USB was not taken over. Close Photos, Image Capture and any app using the card, then retry.',
    '请只连接一台海量存储模式的 A7C II，再准备 USB 连接。':
        'Connect only one A7C II in Mass Storage mode, then prepare the USB connection.',
    '相机或磁盘在卸载前发生变化，尚未接管 USB。请重新连接后重试。':
        'The camera or disk changed before unmounting; USB was not taken over. Reconnect and retry.',
    '正在卸载相机磁盘（不拔线）：': 'Unmounting the camera disk (do not unplug): ',
    '无法卸载相机存储卷。请关闭照片、图像捕捉及使用存储卡的程序后重试。':
        'Could not unmount the camera volume. Close Photos, Image Capture and any app using the card, then retry.',
    '服务模式已退出，等待普通 USB 连接（最多 %d 秒）。':
        'Service mode exited; waiting for the normal USB connection (up to %d s).',
    '普通 USB 连接已恢复。': 'Normal USB connection restored.',
    '等存取灯停止后重试。': 'Retry after the access lamp stops.',
    '%d 秒内未恢复普通 USB 连接。下次操作前请在相机上选择「影像传输（MSC）」。':
        'Normal USB connection did not return within %d s. Before the next operation, choose "Mass Storage (MSC)" on the camera.',
    '相机磁盘尚未稳定，尚未接管 USB。': 'The camera disk is not stable yet; USB was not taken over. ',
    '等待普通 USB 重新枚举：': 'Waiting for normal USB to re-enumerate: ',

    # Camera runtime: USB transport (camera_runtime/transport.py)
    '找不到 libusb 程式庫': 'libusb library not found',
    '無法讀取 USB 配置': 'Cannot read the USB configuration',
    '服務備份缺少四位元組序列號屬性 00e70003': 'Service backup is missing the four-byte serial property 00e70003',
    '只读通信出错后，已让相机退出服务模式（未写入相机）。':
        'After a read-only communication error, the camera was taken out of service mode (nothing was written to the camera).',
    'Jiritsu 狀態 ': 'Jiritsu status ',
    '相機操作超出有界等待時間': 'Camera operation exceeded its bounded wait time',
    '需要且只能連接一台目標相機（USB ': 'Exactly one target camera must be connected (USB ',
    '）；請確認大量儲存模式及驅動': '); check Mass Storage mode and the driver',
    '等待相機完成 USB 初始化。': 'Waiting for the camera to finish USB initialization.',
    '只支援 ': 'Only supports ',
    '等待相机从上一次服务模式恢复（%d 秒）。': 'Waiting for the camera to recover from the previous service mode (%d s).',
    '會話結果未知，停止後續命令': 'Session result is unknown; further commands stopped',
    '不允許此 Jiritsu 命令': 'This Jiritsu command is not allowed',
    'Jiritsu 回應格式錯誤': 'Malformed Jiritsu response',
    '路徑不符': 'Path does not match',
    '不是指定臨時檔': 'Not the designated temporary file',
    '不允許此 CP 單元': 'This CP unit is not allowed',
    'CP 寫入目標或長度不符': 'CP write target or length does not match',
    'AP 綁定目標或長度不符': 'AP binding target or length does not match',
    '相機正在準備機身資訊，稍候再讀取。': 'The camera is preparing body information; reading again shortly.',
    '相机未能自动退出服务模式（%s）；请拔 USB、取电池约 1 分钟后重开。':
        'The camera could not leave service mode automatically (%s); unplug USB, remove the battery for about 1 minute, then restart.',
    '服务身份 0336 已出现，但接口无法打开；请保留驱动与 USB 日志，不重新认证。':
        'Service identity 0336 appeared, but its interface cannot be opened; keep the driver and USB logs. Not re-authenticating.',
    '认证后相机未进入服务模式（期间出现的 Sony USB 身份：%s）。':
        'After authentication the camera did not enter service mode (Sony USB identities seen meanwhile: %s).',
    '认证后相机未进入服务模式（期间出现的 Sony USB 身份：无）。':
        'After authentication the camera did not enter service mode (Sony USB identities seen meanwhile: none).',
    '服務身份未出現，相機也未回到普通 USB；請在相機選擇「影像傳輸（MSC）」後重新連接':
        'Service identity did not appear and the camera did not return to normal USB; choose "Mass Storage (MSC)" on the camera and reconnect',
    '相机已回到普通 USB，冷却后自动重试（第 %d/%d 次）。':
        'The camera returned to normal USB; retrying automatically after a cool-down (attempt %d/%d).',
    '目前機身與備份機身不同': 'The connected body differs from the backed-up body',
    '不允許空檔寫入': 'Writing an empty file is not allowed',
    'USB 身份：': 'USB identity: ',
    '；正在等待 ': '; waiting for ',
    '；阶段经过 ': '; stage time ',
    ' 秒': ' s',
    '未出现': 'none present',
    '服務身份未出現；若是第一次，請依文件安裝0336驅動（已嘗試 %d 次）':
        'Service identity did not appear; if this is the first time, install the 0336 driver as documented (%d attempts made)',
    '臨時檔過大': 'Temporary file is too large',
    '；USB 型號不符': '; USB model does not match',

    # Sound state (desktopapp/actions/sound_state.py)
    '当前自定义声音配置不存在，请重新保存或恢复原厂音效。':
        'The current custom sound configuration does not exist; save it again or restore the factory sound.',
    '当前声音尚未按磁盘配置加载，请按写入后的提示断电重开。':
        'The current sound has not been loaded from the disk configuration; cold-reload as instructed after the write.',
    '机械快门关闭段不是静音数据，请保留诊断包。':
        'The mechanical shutter closing segment is not silent data; keep the diagnostic bundle.',

    # One-click install (desktopapp/allinone.py)
    '本次一键安装已结束，没有重复写入。': 'This one-click install has finished; nothing was written again.',
    '重新读取当前竖屏与线框状态，续接本次安装；相同内容不重复写入。':
        'Re-reading the current Vertical Display and frame state to continue this install; identical content is not written again.',
    '所选安装已完成；请在机身检查预览、名称、拍摄和回放。':
        'The selected installation is complete; check preview, names, shooting and playback on the camera.',
    '执行：': 'Running: ',
    '相机安装与重启核对已通过；只继续电脑端插件步骤。':
        'Camera installation and the restart check passed; continuing only the computer-side plugin step.',
    '上次程序与名称已完整读回；核对当前内容后只继续设置，不重装驱动、不重复刷写程序。':
        'Programs and names from last time were fully read back; after checking current content only settings continue. '
        'No driver reinstall and no program rewrite.',
    '名称已经写好；核对／准备资源重新加载，不重写名称，不重装驱动。':
        'Names are already written; verifying / preparing the resource reload. Names are not rewritten and drivers are not reinstalled.',
    '继续已保存的安装计划；先核对新开机，不重新刷写。':
        'Continuing the saved installation plan; verifying the fresh boot first, without rewriting.',
    '程序安装尚未完成，不能继续收尾：': 'Program installation is not finished, so finishing cannot continue: ',
    '所有读写已结束。\n': 'All reading and writing have ended.\n',
    '所有读写已结束。': 'All reading and writing have ended.',
    '上次停在连接准备；本次只测试连接，不重复更换驱动。':
        'Last time stopped at connection preparation; this run only tests the connection and does not change drivers again.',
    '竖屏已保存开启，并已核对重开后的实际运行状态。':
        'Vertical Display is saved as on, and its running state after the reload was verified.',
    '旧安装的竖屏仅在本次开机开启；可用新版竖屏页保存开启。':
        'Vertical Display from the old install is on only for this boot; use the new Vertical Display page to save it as on.',
    '语音清理未完整核对，不继续安装其他功能': 'Voice cleanup was not fully verified; other features will not be installed',
    '竖屏线框步骤没有返回已写入／已符合目标状态，请保留日志':
        'The Vertical Display frame step did not report written / already at target; keep the log',
    '本次程序／外观写入和完整读回已结束。\n': 'Program / look writing and full readback for this run have ended.\n',
    '重启后核对尚未完成，不能标记安装完成：': 'The post-restart check is not finished, so the install cannot be marked complete: ',
    '竖屏持久化加载尚未确认，不以会话临时开启代替完成。请保留日志。':
        'The saved Vertical Display load is not confirmed yet; a temporary session switch does not count as done. Keep the log.',
    '上次安装在写入前停止；保留失败记录，使用新版代码重新生成方案，不重装驱动。':
        'The last install stopped before writing; the failure record is kept and the plan is rebuilt with the new code. No driver reinstall.',
    '上次在名称提交前空间不足；先核对现有字节并清理该次已完成的临时报告。':
        'Last time ran out of space before names were committed; checking current bytes and cleaning that run\'s finished temporary reports first.',
    '；原始阶段：%s；原始错误：%s': '; original stage: %s; original error: %s',
    '缺少原始错误，请导出包含子事务的新诊断包': 'original error missing; export a new diagnostic bundle that includes the child transactions',
    '上次安装结果需要核对，不会重复刷写。保留本目录并查看完整错误：':
        'The last install result needs checking and will not be rewritten. Keep this folder and see the full error: ',
    '未知': 'unknown',

    # Current-state backup (desktopapp/backup.py)
    '当前状态备份只支持 ILCE-7CM2 2.01': 'Current-state backup only supports ILCE-7CM2 2.01',
    '请选择新的备份目录，已有备份不会覆盖': 'Choose a new backup folder; existing backups are never overwritten',
    '当前状态备份已完成并通过本地校验；没有写入相机。': 'Current-state backup finished and passed the local check; nothing was written to the camera.',
    '语音包备份本地校验失败': 'Voice pack backup failed the local check',
    '语音文件备份：%d/%d': 'Voice file backup: %d/%d',
    '；已完成的项目备份仍保留。': '; the finished project backup is kept.',
    '备份的是创建时的当前项目状态，可能已修改，不是原厂基准或完整相机镜像。':
        'The backup holds the project state at creation time, which may already be modified; it is not a factory baseline or a full camera image.',
    '不包含完整文件系统；自定义声音文件与其他未列入的资源不在项目检查点中。':
        'It does not contain the full file system; custom sound files and other unlisted resources are not in the project checkpoint.',
    '语音包备份未完成，文件不可读或长度不符：': 'Voice pack backup incomplete; file unreadable or wrong length: ',

    # ExifTool helper (desktopapp/exiftool.py)
    '正在准备 Lightroom 的 ExifTool 辅助程序（仅电脑端，不连接相机）。':
        'Preparing the ExifTool helper for Lightroom (computer only; the camera is not connected).',
    'ExifTool 自动下载失败，本次未开始相机操作。请检查网络后再点同一按钮；完整错误：\n':
        'ExifTool download failed; no camera operation was started. Check the network and click the same button again. Full error:\n',
    'ExifTool 已就绪：': 'ExifTool ready: ',
    '下载官方 ExifTool：': 'Downloading official ExifTool: ',
    'ExifTool 启动失败：': 'ExifTool failed to start: ',

    # Look batch validation (desktopapp/lookbatch.py)
    '请至少添加一个操作项；未添加的槽位保持原样。': 'Add at least one operation; slots you do not add stay unchanged.',
    '每个目标槽位只能有一个操作，范围为 1–6。': 'Each target slot can have only one operation, in the range 1–6.',
    '外观名称必须是文字。': 'The look name must be text.',

    # Recovery sources (desktopapp/official.py)
    '正在解码原厂文件，仅操作电脑文件…': 'Decoding the factory file (computer files only)…',
    '请提供本地原厂恢复来源；软件不再内置原厂恢复字节':
        'Provide a local factory restore source; the app no longer has built-in factory restore bytes',
    '本机恢复来源配置无效，请重新选择官方固件。': 'The configured local restore source is invalid; choose the official firmware again.',
    '本机恢复来源不可用，请接回原厂固件所在磁盘或手动选择文件。':
        'The local restore source is unavailable; reconnect the disk holding the factory firmware or choose the file manually.',
    '使用本机预设的官方恢复来源；仍按正常流程提取、恢复并读回。':
        'Using the preset local official restore source; extraction, restore and readback still run normally.',
    '恢复来源不是可用的原厂区域，请选择官方 2.01 固件；普通当前状态备份不一定可用。':
        'The restore source does not hold usable factory regions; choose the official 2.01 firmware. A normal current-state backup may not work.',
    '所选备份没有语音包。请选择官方固件、带语音 ZIP 的同机原始备份，或取消勾选“同时恢复语音包”。':
        'The selected backup has no voice pack. Choose the official firmware or an original same-body backup with a voice ZIP, '
        'or untick "Also restore the voice pack".',
    '一键恢复需要原厂恢复来源。请选择官方 ILCE-7CM2 2.01 BODYDATA.DAT，或可用同机原始备份；安装不要求预先提供。':
        'One-click restore needs a factory restore source. Choose the official ILCE-7CM2 2.01 BODYDATA.DAT or a usable original '
        'same-body backup; installing does not need one.',
    '原厂文件已解码 %.0f MiB': 'Factory file decoded: %.0f MiB',

    # macOS authorization (desktopapp/platforms/macos_authorization.py)
    '请在打开的「终端」窗口中输入 Mac 登录密码（输入时不显示）。':
        'Enter your Mac login password in the Terminal window that opened (it is not shown while typing).',
    '管理员进程意外结束，相机操作结果未知。请导出诊断包，不要重复刚才的操作。':
        'The administrator process ended unexpectedly; the camera operation result is unknown. Export a diagnostic bundle and do not repeat the operation.',
    '终端授权未完成（窗口已关闭或密码不正确）；本次相机操作尚未开始，可重新点击原按钮。':
        'Terminal authorization did not finish (window closed or wrong password); the camera operation has not started, so you can click the button again.',
    '等待在「终端」窗口输入 Mac 登录密码；尚未接管 USB 或开始相机操作。输入密码前关闭终端窗口不会刷写相机。\n':
        'Waiting for the Mac login password in the Terminal window; USB is not taken over and no camera operation has started. '
        'Closing Terminal before entering the password does not write the camera.\n',
    '终端授权未完成，相机操作未报告开始。请保留日志；系统详情：':
        'Terminal authorization did not finish and the camera operation did not report a start. Keep the log; system details: ',
    '相机授权 worker 必须由终端 sudo 启动。': 'The camera authorization worker must be started by sudo in Terminal.',
    '相机任务已结束，但文件所有权交还失败；请保留此日志。\n':
        'The camera task ended, but returning file ownership failed; keep this log.\n',

    # Windows drivers (desktopapp/platforms/usb_drivers.py)
    '等待 Windows 管理员确认…': 'Waiting for Windows administrator confirmation…',
    '管理员进程已启动；正在实时读取进度。': 'Administrator process started; reading its progress live.',
    '正在读取 Windows 驱动绑定…': 'Reading Windows driver bindings…',
    '正在检测 Sony 054C:': 'Checking the existing driver for Sony 054C:',
    ' 的现有驱动…': '…',
    '已安装可用驱动，本次沿用，未重复安装': 'A usable driver is installed and is kept; not reinstalled',
    '正在建立相机服务连接（此步骤不写固件）；两种 USB 身份分别检查。':
        'Opening the camera service connection (this step does not write firmware); both USB identities are checked separately.',
    '正在让 Windows 重新识别设备…': 'Asking Windows to re-detect the device…',
    '已列出所有 Sony USB 身份；未知 PID 不等于已确认的 A7C II。请核对设备名称、接口类型及海量存储模式，不会给未知设备自动换驱动。':
        'All Sony USB identities are listed; an unknown PID is not a confirmed A7C II. Check the device name, interface type and Mass Storage mode; '
        'drivers are never changed automatically for unknown devices.',
    '054C:%s 尚未出现；预先安装 WinUSB 驱动包，相机切换到该身份时 Windows 可直接使用。':
        '054C:%s has not appeared yet; pre-installing the WinUSB driver package so Windows can use it as soon as the camera switches to that identity.',
    '未发现 Sony USB 设备': 'no Sony USB device found',
    '054C:%s 已安装 %s，直接沿用，跳过驱动安装与管理员申请。':
        '054C:%s already has %s installed; keeping it and skipping driver installation and the administrator request.',
    '驱动安装超过 180 秒，已停止等待；请保留日志核对当前绑定，不自动重复安装。':
        'Driver installation took over 180 s and waiting stopped; keep the log and check the current binding. It will not be reinstalled automatically.',
    '服务身份已出现，检测现有驱动。': 'Service identity appeared; checking its existing driver.',
    '驱动准备已完成，重新等待 0336 接口连接。': 'Driver preparation finished; waiting again for the 0336 interface to connect.',
    '服务连接成功，驱动准备结束。': 'Service connection succeeded; driver preparation finished.',
    '正在备份驱动包：': 'Backing up driver package: ',
    '正在卸载相机驱动包：': 'Uninstalling camera driver package: ',
    '054C:%s 尚未出现；系统中已有其驱动包 %s，跳过预装。':
        '054C:%s has not appeared yet; Windows already has its driver package %s, so pre-installation is skipped.',
    '无可读设备': 'no readable device',
    '。完整设备／接口信息已保存，不会为未知 PID 自动更换驱动。':
        '. Full device / interface details were saved; drivers are never changed automatically for an unknown PID.',
    '。本次未安装驱动或写入相机。原始查询错误：': '. No driver was installed and nothing was written to the camera. Original query error: ',
    '当前检测：': 'Currently detected: ',
    'Windows 驱动查询失败，不能据此判断相机未连接。libusb 当前检测：':
        'The Windows driver query failed, so it cannot tell whether the camera is connected. libusb currently detects: ',
    '未找到相机的海量存储身份 054C:0E8A，请在相机选择“海量存储”后重新连接。':
        'The camera\'s Mass Storage identity 054C:0E8A was not found; choose "Mass Storage" on the camera and reconnect. ',
    '未找到服务身份 054C:0336，请先使用“两阶段驱动与连接”入口。':
        'Service identity 054C:0336 was not found; use "Two-stage drivers & connection" first. ',

    # Built-in looks (desktopapp/presets.py)
    '内置六款外观文件缺失，请使用完整工具包；尚未连接相机：':
        'The six built-in look files are missing; use the complete package. The camera was not connected: ',
    '内置外观名称／照片阶段不符：': 'Built-in look name / photo stage does not match: ',

    # Name review (desktopapp/reviewnames.py)
    '已确认此前没有提交名称或程序；只清理了对应临时报告／worker。原失败记录保留，下一次使用新的事务。':
        'Confirmed that no names or programs were committed earlier; only the related temporary reports / worker were cleaned. '
        'The original failure record is kept and the next run uses a new transaction.',
    '核对已完成的名称失败报告、原程序窗口与名称绑定；不写固件或设置。':
        'Checking the finished name failure report, original program windows and name bindings; no firmware or settings are written.',

    # USB stability check (desktopapp/usbcheck.py)
    '通过只说明这段时间内连续只读传输稳定；不保证刷写期间一定不掉线，也不代表线材认证。':
        'Passing only shows continuous read-only transfers were stable during this period; it does not guarantee the link stays up while writing, '
        'and it is not a cable certification.',
    '%d 轮只读传输均完成，共 %.1f MB，连续读取 %.0f 秒，逐轮字节一致。%s':
        'All %d read-only rounds finished: %.1f MB in total, %.0f s of continuous reading, identical bytes in every round. %s',
    '请换线或直连电脑 USB 接口后重测；': 'Change the cable or connect directly to a computer USB port, then test again; ',
    '相机端 /tmp/jiritsu 暂存目录挂载准备失败，尚未读取目标文件；需要核查机身端挂载环境，不能据此判定线材故障。':
        'The camera failed to prepare the /tmp/jiritsu staging mount before reading the target file; the camera-side mount needs checking. '
        'This does not indicate a cable fault. ',
    '相机端文件命令已返回失败；请保留诊断记录，按状态码检查文件访问，不能据此判定线材故障。':
        'A camera-side file command returned a failure; keep the diagnostics and check file access by status code. This does not indicate a cable fault. ',
    'USB 稳定性检测未通过（%s）：%s。%s本次没有固件或设置写入。':
        'USB stability check failed (%s): %s. %sNo firmware or settings were written.',
    'USB 稳定性检测：第 %d 轮只读读取程序文件（至少 %d 轮、连续 %d 秒），不写固件或设置。':
        'USB stability check: round %d of read-only program-file reads (at least %d rounds and %d s continuous); no firmware or settings are written.',
    'USB 稳定性检测未完成：%s。本次没有固件或设置写入。': 'USB stability check did not finish: %s. No firmware or settings were written.',
    '已读 %d 轮，达到轮数上限，但连续读取只持续 %.0f 秒，未满 %d 秒；本次不算通过':
        '%d rounds read and the round limit was reached, but continuous reading lasted only %.0f s, less than %d s; this run does not pass',
    '连接阶段': 'connection stage',
    '第 %d 轮': 'round %d',
    '程序文件未完整读回：': 'Program file was not fully read back: ',
    '重复读回的字节不一致：': 'Repeated readback bytes differ: ',
    '读取 %s 只有 %.2f MB/s，低于 %.1f MB/s；连接可能经过 USB 1.1、扩展坞或线材质量较差':
        'Reading %s ran at only %.2f MB/s, below %.1f MB/s; the link may go through USB 1.1, a dock or a poor cable',
    '竖屏线框操作停止：文件 %d，步骤 %d，窗口 %d，错误 %d；已写 %d 字节。原生报告：%s':
        'Vertical Display frame operation stopped: file %d, step %d, window %d, error %d; %d bytes written. Native report: %s',

    # Vertical Display (desktopapp/vertical_native.py, looktool/verticalpersist.py, portraitjob.py)
    '旧竖屏补偿已撤回，尚未安装原生资源。按提示完整断电重开，再点击“开启竖屏显示”继续。':
        'The old Vertical Display compensation was withdrawn; native resources are not installed yet. Do a full cold reload as instructed, '
        'then click "Enable Vertical Display" to continue.',
    '原生竖屏资源准备前必须先关闭竖屏；本次未复制资源':
        'Vertical Display must be off before native portrait resources are prepared; no resources were copied',
    '竖屏资源处理已结束，仍需冷重开恢复 /usr 只读状态；不标记加载成功':
        'Vertical Display resource handling has ended, but a cold reload is still needed to restore /usr to read-only; not marked as loaded',
    '竖屏保存值已读取，但开机运行状态／资源尚不符合目标；不以 RAM 临时开启代替持久化验证':
        'The saved Vertical Display value was read, but the running state / resources after boot do not match the target yet; '
        'a temporary RAM switch does not replace persistent verification',
    '线框资源已清理，但只读挂载仍忙；完整断电后再核对恢复':
        'Frame resources were cleaned, but the read-only mount is still busy; verify the restore after a full power-off',
    '恢复本测试版的原线框引用和资源索引。': 'Restoring the original frame references and resource indexes of this test version.',
    '所有读写已结束。按弹窗完整断电重开后，检查横握／两侧竖握的 Fn 网格、创意外观选择页和参数调整页。':
        'All reading and writing have ended. After a full cold reload as the dialog describes, check the Fn grid, the Creative Look '
        'selection page and the adjustment page in landscape and both portrait grips.',
    '当前内容已符合所选状态，没有重复写入。': 'Current content already matches the selected state; nothing was written again.',
    '竖屏开关和线框步骤已写好，继续安装其余所选功能。':
        'The Vertical Display switch and frame step are written; continuing with the other selected features.',
    '请保留日志。下次点击同一操作会重新读取当前资源和机内撤销记录，不重放旧任务。':
        'Keep the log. Clicking the same operation next time re-reads the current resources and the in-camera undo record; old jobs are not replayed.',

    # Voice pack (desktopapp/voicespace.py, worker.py, looktool/resourceworker.py)
    '语音恢复请使用一键恢复': 'Use One-click restore to restore the voice pack',
    '语音音频已移除，机内语音指南相关选项保持置灰、关闭限制保持启用；语音索引、对焦提示音和快门音频未删除。':
        'Voice audio was removed. The in-camera Voice Guide options stay greyed out and the off-lock stays active; the voice index, '
        'focus beeps and shutter audio were not deleted.',
    '语音指南关闭限制及菜单禁用状态已写入。按提示完整断电重开，再点击同一操作；此阶段尚未删除音频。':
        'The Voice Guide off-lock and disabled menu are written. Do a full cold reload as instructed, then click the same operation; '
        'no audio has been deleted at this stage.',
    '语音指南尚未关闭，未开始资源操作': 'Voice Guide is not off yet; the resource operation did not start',
    '请在“一键恢复原厂功能”中勾选恢复语音包；不再提供独立语音恢复入口。':
        'Tick the voice pack option in "One-click restore factory functions"; there is no separate voice restore anymore.',
    '语音指南关闭限制尚未按磁盘版本加载。请按提示完整断电重开，再继续资源操作；尚未删除或写回语音文件。':
        'The Voice Guide off-lock has not been loaded from disk yet. Do a full cold reload as instructed before continuing; '
        'no voice files were deleted or written back.',
    '资源操作未完成：status=%s，readonly=%s，cleanup=%s': 'Resource operation incomplete: status=%s, readonly=%s, cleanup=%s',
    '资源文件写回：%s %.1f / %.1f MiB': 'Writing back resource file: %s %.1f / %.1f MiB',

    # Worker entry points (desktopapp/worker.py)
    '准备竖屏显示的 USB 驱动与服务连接。': 'Preparing the USB driver and service connection for Vertical Display.',
    '先完成一次本页操作，再核对重新加载状态。': 'Complete one operation on this page first, then verify the reload state.',
    '所选目录没有旧备份恢复记录，本次没有连接相机。用内置原厂基准或固件文件恢复后，请点“重启后核对并完成恢复”。':
        'The selected folder has no old-backup restore record; the camera was not connected. After restoring from the built-in factory '
        'reference or a firmware file, click "Verify after restart and finish restore".',

    # Checkpoint restore (looktool/checkpointjob.py, checkpointworker.py)
    '此备份会解除语音关闭限制。请提供官方 2.01 文件或该备份附带的语音 ZIP，先补回资源；本次尚未写入程序。':
        'This backup removes the voice off-lock. Provide the official 2.01 file or the voice ZIP from that backup to restore the resources first; '
        'no programs have been written.',
    '请完整断电重开（拔 USB、关机、取下电池至少 1 分钟后装回开机），再接回 USB 点同一个恢复按钮。':
        'Do a full cold reload (unplug USB, power off, remove the battery for at least 1 minute, put it back and power on), '
        'then reconnect USB and click the same restore button. ',
    '名称内容已完成，但只读挂载忙碌；需要完成设置与重新加载准备后再重开核对。':
        'Name content is complete, but the read-only mount is busy; finish settings and reload preparation, then reload and verify.',
    '只会处理剩下的部分。': 'Only the remaining part is processed.',
    '写入前检查发现相机 /usr 分区临时空间不足，本次没有写入。':
        'The pre-write check found too little temporary space on the camera /usr partition; nothing was written. ',
    '相机 /usr 分区仍处于可写挂载，通常是上一次操作后还没有完整断电重开；本次没有写入。':
        'The camera /usr partition is still mounted writable, usually because there was no full cold reload after the last operation; nothing was written. ',
    '旧任务名称备份清理未完成，相机名称文件没有改动；请完整断电重开后再点恢复。Backup cleanup incomplete: ':
        'Cleanup of old-job name backups is incomplete; camera name files were not changed. Do a full cold reload, then click restore again. '
        'Backup cleanup incomplete: ',
    '相机 /usr 分区的临时空间用完了：已恢复 %d/%d 个名称文件，程序和已恢复的部分保持不变，相机可以正常开机使用。旧文件占用的空间要断电后才释放。':
        'The camera /usr partition ran out of temporary space: %d/%d name files were restored. Programs and the restored part are unchanged '
        'and the camera can start and be used normally. Space held by old files is freed only after a power-off. ',

    # Look conversion (looktool/compilelook.py, coupledfit.py)
    '已生成近似结果；最终优化未完全收敛。验证色样平均预测误差 %.2f / 255，不能代表实机色彩准确度。':
        'An approximate result was created; the final optimization did not fully converge. Mean prediction error on validation patches is '
        '%.2f / 255, which does not represent in-camera color accuracy.',
    '初始拟合达到迭代预算，保留当前近似值继续优化；不会中断转换。':
        'The initial fit reached its iteration budget; continuing optimization from the current approximation. The conversion is not interrupted.',

    # Device session (looktool/devicesession.py)
    '已清理上次只读检测留下的报告（不影响相机内容），继续本次操作。':
        'Cleaned the report left by the last read-only check (camera content unaffected); continuing this operation.',
    '相机没有以普通“海量存储”身份连接（可能仍停在上次的服务模式 054C:0336）。请拔掉 USB、关机并取出电池约 1 分钟，再开机选择海量存储、接回 USB 后重试；本次没有写入相机。（Normal Mass Storage USB serial is required for body binding）':
        'The camera is not connected with its normal "Mass Storage" identity (it may still be in the previous service mode 054C:0336). '
        'Unplug USB, power off and remove the battery for about 1 minute, then power on, choose Mass Storage, reconnect USB and retry; '
        'nothing was written to the camera. (Normal Mass Storage USB serial is required for body binding)',
    '普通 USB 身份未出现；只读取已有服务会话的机身序列，核对后续接，不重复认证。':
        'The normal USB identity did not appear; reading the body serial from the existing service session only, then continuing after the check. '
        'Not re-authenticating.',
    '读取相机文件失败：': 'Reading a camera file failed: ',
    '等待相机普通 USB 连接（最多 %d 秒）。': 'Waiting for the camera\'s normal USB connection (up to %d s).',

    # Direct transactions (looktool/direct.py, namespause.py)
    '读取当前状态': 'Reading current state',
    '准备重新加载': 'Preparing reload',
    '写入前检查通过，接下来应用更改': 'Pre-write checks passed; applying changes next',
    '正在应用所选操作': 'Applying the selected operations',
    '读回完成，等待断电重开': 'Readback complete; waiting for a cold reload',
    '加载状态符合目标': 'Load state matches the target',
    '完成': 'Done',
    '已停止，请保留日志核对结果': 'Stopped; keep the log to check the result',
    'FL23 操作完成：已写入并完整读回；重开后生效，无需再点核对。':
        'FL23 operation complete: written and fully read back. It takes effect after a reload; no need to click verify.',
    '所选槽位已保存为 ST。': 'The selected slots were saved as ST.',
    '恢复布局清单不包含原厂字节，请先提供官方固件或可用同机原始备份':
        'The restore layout contains no factory bytes; first provide the official firmware or a usable original same-body backup',
    '恢复计划已生成': 'Restore plan created',
    '所选操作的写入计划已生成': 'Write plan for the selected operations created',
    '恢复并核对名称资源': 'Restoring and verifying name resources',
    '核对名称资源': 'Verifying name resources',
    '恢复原厂外观设置': 'Restoring factory look settings',
    '应用并核对所选设置': 'Applying and verifying the selected settings',
    '名称已写好；请按提示断电重开，再继续程序安装': 'Names are written; cold-reload as prompted, then continue the program install',
    '名称及只读挂载已确认，可以继续程序安装': 'Names and the read-only mount are confirmed; the program install can continue',
    '恢复尚未完成：写入与读回已结束，等待重启后核对': 'Restore not finished: writing and readback have ended; waiting for the post-restart check',
    '已核对程序和名称均符合原安装计划，只续做设置与重新加载准备；没有重复刷写程序。':
        'Programs and names match the original install plan; only settings and reload preparation continue. Programs were not rewritten.',
    '尚未确认新的冷启动与只读挂载；没有重复写入。请按弹窗完成断电重开、接回。':
        'A fresh cold boot and read-only mount are not confirmed yet; nothing was written again. Cold-reload and reconnect as the dialog describes.',
    '已清理旧任务遗留的名称备份 %d 个，释放相机 /usr 空间。': 'Removed %d name backups left by old jobs, freeing camera /usr space.',
    '所有读写已结束。68 个名称已完整核对，程序和配方尚未写入。旧资源仍被占用，需要断电重开释放后，再点同一按钮继续；不重复写名称。':
        'All reading and writing have ended. All 68 names were verified; programs and recipes are not written yet. Old resources are still in use: '
        'cold-reload to release them, then click the same button to continue. Names are not written again.',
    '安装／关闭任务已结束，没有后续待写入步骤。以下断电仅用于让相机加载已写入的程序，电脑端核对可选。':
        'The install / disable job has ended with no further write steps. The power cycle below only lets the camera load the written programs; '
        'verifying on the computer is optional.',
    '所有读写已结束。拔 USB 和其他外部供电，等存取灯停止闪烁，再正常关机并等屏幕和灯完全熄灭；取下电池至少一分钟，再装回开机、检查功能并核对。':
        'All reading and writing have ended. Unplug USB and other external power, wait for the access lamp to stop blinking, power off normally '
        'and wait for the screen and lamp to go dark; remove the battery for at least one minute, put it back, power on, check the features and verify.',
    '磁盘与设置已符合目标，本次没有重复写入；实际预览、照片和声音仍需在机身检查。':
        'Disk and settings already match the target; nothing was written again. Still check preview, photos and sound on the camera.',
    '所有读写已结束。名称已核对，程序未写入。': 'All reading and writing have ended. Names are verified; programs are not written. ',
    '本测试只用于已安装自定义 LUT 的相机；本次没有写入。': 'This test is only for cameras with a custom LUT installed; nothing was written.',
    '只读挂载已恢复，无需额外重开。': 'The read-only mount is restored; no extra reload is needed.',
    '请按弹窗断电重开后接回，继续剩余程序安装。': 'Cold-reload as the dialog describes, reconnect, and continue the remaining program install.',
    '原厂恢复后的 /usr 只读挂载尚未确认；不标记恢复完成，请保留日志':
        'The read-only /usr mount after the factory restore is not confirmed; restore is not marked complete. Keep the log',
    '尚未确认新的冷启动。完成断电重开后再核对，不要重复写入。':
        'A fresh cold boot is not confirmed yet. Verify after a cold reload; do not write again.',
    '名称写入已完成，但尚未确认新开机后的只读挂载；不清理旧资源':
        'Name writing finished, but the read-only mount after a fresh boot is not confirmed; old resources are not cleaned',
    '先写入名称资源，成功后才写入程序。': 'Name resources are written first; programs are written only after they succeed.',
    '语音空间清理已启用。请先选择索尼官方 2.01 BODYDATA.DAT，再一键恢复；必须完整补回语音文件后才能解除关闭限制，本次尚未恢复程序。':
        "Voice space cleanup is active. First choose Sony's official 2.01 BODYDATA.DAT, then run One-click restore; the off-lock is removed only "
        'after all voice files are written back. No programs were restored.',
    '相机仍在运行上次写入前加载的程序，本次没有写入。请先拔 USB、关机，取下电池至少一分钟，再开机接回 USB，点击“重启后核对并完成恢复”或再次点击恢复。':
        'The camera is still running the programs loaded before the last write; nothing was written. Unplug USB, power off, remove the battery '
        'for at least one minute, power on, reconnect USB and click "Verify after restart and finish restore" or restore again.',
    '正在逐文件更新名称（共 %d 项）；名称完成后才写入程序。':
        'Updating names file by file (%d items); programs are written only after names finish.',
    '正在写入程序窗口批次 %d/%d': 'Writing program window batch %d/%d',
    '名称内容已完成；只读挂载忙碌。完成设置与重新加载准备后，需要断电重开核对挂载状态。':
        'Name content is complete; the read-only mount is busy. After settings and reload preparation, cold-reload to verify the mount state.',
    '正在读取原程序，核对尚未写入的程序窗口。': 'Reading the original programs and checking the program windows not yet written.',
    '名称完整读回：%d/%d': 'Full name readback: %d/%d',

    # Request cleanup (looktool/requestcleanup.py)
    '旧临时工作文件已保存诊断并清理；重新读取相机现况，直接生成本次操作计划，不重放旧任务。':
        'Old temporary work files were saved for diagnostics and cleaned; re-reading the camera state to plan this operation directly. '
        'Old jobs are not replayed.',
    '相机执行插件仍存在，尚不能确认执行入口空闲；本次操作没有开始，请等待当前操作结束':
        'The camera execution plugin still exists, so the execution entry cannot be confirmed idle; this operation did not start. '
        'Wait for the current operation to finish',
    '相机存在启用中的 preload，尚未覆盖临时工作文件或开始写入':
        'The camera has an active preload; temporary work files were not overwritten and writing did not start',
    '相机执行插件出现，已保存诊断，未覆盖工作文件': 'A camera execution plugin appeared; diagnostics saved and work files not overwritten',
    '相机临时状态仍在变化，已保存诊断，未覆盖工作文件：':
        'Camera temporary state is still changing; diagnostics saved and work files not overwritten: ',

    # Shutter sound (shutter_sound/*)
    '旧自定义声音配置过大，无法作为本次替换的依据': 'The old custom sound configuration is too large to base this replacement on',
    '旧自定义声音配置包含冲突的文件引用，请保留诊断包':
        'The old custom sound configuration has conflicting file references; keep the diagnostic bundle',
    '旧自定义声音配置包含冲突的文件引用': 'The old custom sound configuration has conflicting file references',
    '现有声音标记无法对应到已完成的试听报告，已保存原标记；未覆盖未知运行任务。':
        'The existing sound marker does not match a finished audition report; the original marker was saved and the unknown running task was not overwritten.',
    '当前相机的电子快门声音尚未开启，请先开启；本次没有注册试听声音。':
        'The electronic shutter sound is not on for this camera; turn it on first. No audition sound was registered.',
    '请重新开启电子快门声以更新机械快门过滤，再进行试听；本次未注册声音。':
        'Turn the electronic shutter sound on again to update the mechanical shutter filter, then audition; no sound was registered.',
    '所选片段（起点 %.3f 秒，长度 %.3f 秒）几乎没有声音。很多音频开头是一段静音，请把起点移到声音出现的位置，或加长片段后重新转换。':
        'The selected clip (start %.3f s, length %.3f s) is almost silent. Many recordings begin with silence; move Start to where the sound '
        'begins, or lengthen the clip, and convert again.',
    '相机执行入口当前仍被占用，本次声音操作尚未开始。请等待正在执行的操作结束。':
        'The camera execution entry is still busy; this sound operation has not started. Wait for the running operation to finish.',
    '另一个声音操作仍在执行，请等它结束后再点击。': 'Another sound operation is still running; wait for it to finish before clicking.',
    '使用本次选择替换声音；旧任务已归档，接下来读取相机现况，不重放旧命令。':
        'Replacing the sound with this selection; old jobs are archived. Reading the camera state next; old commands are not replayed.',
    '当前声音操作的机身绑定不一致': 'The body binding of the current sound operation does not match',
    '相机开始了另一项操作，本次声音替换尚未执行。': 'The camera started another operation; this sound replacement was not run.',
    '相机临时状态仍在变化，请等待当前操作结束。': 'Camera temporary state is still changing; wait for the current operation to finish.',
    '当前声音临时文件替换未完成：': 'Replacing the current sound temporary file did not finish: ',
    '旧声音任务已确认停在写入前，检查结果和临时清理均完整；已解除占用，原日志保留。':
        'The old sound job is confirmed to have stopped before writing, with complete check results and temporary cleanup; '
        'it was released and its log is kept.',
    '上次保存停在电脑端准备阶段，未执行相机写入；已解除占用，保留原日志。':
        'The last save stopped during computer-side preparation with no camera write; it was released and its log is kept.',
    '试听结果已记录；可直接保存当前转换片段，无需先断电恢复。':
        'Audition result recorded; you can save the current converted clip directly without a cold reload first.',
    '声音支援已准备，继续保存当前片段；全部写入结束后统一提示断电。':
        'Sound support is ready; continuing to save the current clip. You will be asked to power-cycle once all writes end.',
    '请先转换所选片段，再调节音量。': 'Convert the selected clip before adjusting the volume.',
    '请先点「转换所选片段」，转换成功后再试听。': 'Click "Convert selected clip" first, then audition after it succeeds.',
    '自动准备电子快门声支援；已有开关直接接入，不要求先手动开启或关联旧任务。':
        'Preparing electronic shutter sound support automatically; an existing switch is used directly, without turning it on manually '
        'or linking old jobs.',
    '这个声音工作目录里没有可用的永久声音安装记录，本次没有连接相机。要还原相机的原厂快门音效，请点“恢复原厂功能”：它按相机当前字节还原全部声音程序，不依赖旧记录。':
        'This sound work folder has no usable permanent sound install record; the camera was not connected. To restore the factory shutter sound, '
        'use "Restore factory functions": it restores every sound program from the camera\'s current bytes without old records.',
    '最近的声音安装记录不可直接恢复；改用同一机身最近一次完成的安装记录，从相机当前字节规划恢复。':
        'The latest sound install record cannot be restored directly; using the latest finished install record of the same body and planning '
        'the restore from the camera\'s current bytes.',
    '上一次声音操作（%s）中途停止，结果还没确认，所以没有开始新的操作，也没有连接相机。请点窗口底部“导出诊断包”发给作者核对；不要删除声音工作目录。（Previous operation is unresolved: %s）':
        'The previous sound operation (%s) stopped part-way and its result is unconfirmed, so no new operation started and the camera was not '
        'connected. Click "Export diagnostic bundle" at the bottom of the window and send it to the author; do not delete the sound work folder. '
        '(Previous operation is unresolved: %s)',
    '上次试听在调用相机原生程序之前就已停止，没有注册任何声音；已解除占用，原记录保留。':
        'The last audition stopped before calling the camera\'s native program, so no sound was registered; it was released and its record is kept.',
    '电子快门声已启用；已核对并接入声音工具，没有重复刷写。':
        'Electronic shutter sound is enabled; verified and connected to the sound tool without rewriting.',
    '本次只接入已启用的声音开关，保持开机继续。': 'This run only connects the enabled sound switch; keep the camera on and continue.',
    '\n电脑端音频处理失败，本次没有相机读写；请修正输入后重试。':
        '\nAudio processing on the computer failed; the camera was not read or written. Fix the input and retry.',
    '上次试听因旧标记在分配前停止，没有注册新声音；本次按当前状态新建试听。':
        'The last audition stopped before allocation because of an old marker, so no new sound was registered; starting a new audition from the current state.',
    '\n电脑端转换失败，本次没有相机读写；请修正输入后重新转换。':
        '\nConversion on the computer failed; the camera was not read or written. Fix the input and convert again.',
    '电脑端转换失败，本次没有相机读写；请修正输入后重新转换。':
        'Conversion on the computer failed; the camera was not read or written. Fix the input and convert again.',
    '选择只修改机械、只修改电子或两者都修改': 'Choose mechanical only, electronic only or both',
    '相机仍加载着旧声音，暂无空闲音频位置；请先按上次写入提示断电重开并核对，不覆盖在用文件。':
        'The camera still has the old sound loaded and no audio slot is free; cold-reload and verify as the last write instructed. '
        'Files in use are not overwritten.',
    '电子快门声尚未开启。请先点击“开启电子快门声”，完成断电重开后再试听；本次没有写入固件或注册试听。':
        'Electronic shutter sound is not on. Click "Enable electronic shutter sound", do a cold reload, then audition; '
        'no firmware was written and no audition registered.',
    '旧版快门声音尚未限制机械快门。请重新点击“开启电子快门声”更新后再试听；本次未注册声音。':
        'The old shutter sound does not yet exclude the mechanical shutter. Click "Enable electronic shutter sound" again to update it, '
        'then audition; no sound was registered.',
    '未找到相机 USB 连接。请拔插 USB 并选择海量存储后重试；尚未进行服务认证或声音写入。':
        'No camera USB connection found. Replug USB, choose Mass Storage and retry; no service authentication or sound write happened.',
    # Same messages in the 3.0.3-era develop code, so the layer also rebases there.
    '正在等待服务身份 054C:0336；出现后先检测驱动，已有可用绑定则跳过安装。':
        'Waiting for service identity 054C:0336; when it appears its driver is checked first, and a usable binding skips installation.',
    '准备本次线框测试的 USB 驱动与服务连接。': 'Preparing the USB driver and service connection for this frame test.',
}
