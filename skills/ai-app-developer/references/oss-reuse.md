# GitHub/repository reuse due diligence

Search public repositories only when external access is available. Do not invent stars, licenses or maintained status. Prefer official SDKs, actively maintained libraries and simple dependencies over wholesale repo copying.

For each candidate record: URL and commit/tag checked; verified license and obligations (SPDX, notices, copyleft constraints); last release and recent commit activity; platform compatibility; security advisories; transitive dependency risk; tests, documentation, build reproduction and maintenance. Flag unknown license as **not authorized for reuse until clarified**.

Run dependency/install instructions only in safe isolated environments. Never execute untrusted install scripts or copied shell commands blindly. Review imports, secrets and network behavior.

Use decision table: task fit, license, integration effort, breakage risk, performance, alternatives, recommendation. Cite links and dates. Track modifications and required attribution.
