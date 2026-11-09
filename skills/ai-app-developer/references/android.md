# Android track

Choose Kotlin/Jetpack Compose for Android-native by default when Android only and strong system integration is needed; consider Flutter if multi-platform reuse is a core requirement. Validate SDK/API requirements and licensing with current official docs.

Document package ID, min/target SDK, runtime permissions, local storage (scoped storage / picker), background jobs, notification policy, deep links, media codecs, battery impacts, portrait/landscape, offline and device performance.

Milestones: Android Studio/Gradle scaffold → first Compose screen → one usable flow → local data handling → platform integration → emulator/device test → debug APK → signing/release plan. Never claim APK exists until built and file verified.

Acceptance checks: clean build, unit tests, UI test/smoke test, permission deny/retry, no internet, process death/restart, low storage, multiple resolutions and Android versions within support matrix. Video feature: check codecs, permissions and lawful source restrictions; avoid undocumented platform bypass.
