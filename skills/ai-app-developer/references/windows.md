# Windows desktop track

Options: C# WPF/WinUI for Windows-native apps; Tauri + TypeScript where a web-based UI and small desktop shell suit the problem; Electron only when its ecosystem benefits outweigh memory/package size. Verify current OS and runtime prerequisites.

Document installer strategy, writable directories, file dialogs, UAC/elevation, auto-update mechanism, code signing, DPI scaling, multi-monitor behavior, accessible keyboard shortcuts, file locking, crash/log folder and offline operation.

Milestones: reproducible local run → main window/navigation → feature slice → storage/import/export → exception handling → clean release build → installer/portable package when appropriate. Never assume executable is signed.

Verification: clean install on supported Windows versions, paths with Vietnamese Unicode, missing permissions, different DPI, multiple monitors, crash recovery, uninstall behavior and updater rollback.
