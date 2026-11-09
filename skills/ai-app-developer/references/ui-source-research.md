# Research first, code second: functional UI source selection

## Discovery order
1. Identify the task and target runtime (web, Android native, React Native, Windows native, browser shell).
2. Locate functional reference implementations: official component docs -> library source repository -> live storybook/demo -> independently audited reusable packages. The eight curated sites are in `ui-reference-catalog.md`; use official framework docs when architectural behavior is at stake.
3. For each candidate, inspect **both** rendered interaction and code/usage: component props, handlers, event lifecycle, async behavior, loading, focus, gestures, error, keyboard, screenreader, mobile layout, tests, license, maintenance and dependency sizes.
4. Build a short proof-of-concept in the actual target stack when practical. Record file/commit, installation command, run command, limitations, visual states and behavior cases.
5. Compare 2-3 candidates and either select one, adapt it lawfully, or implement in-house. Highlight missing behavior, not just visual differences.

## Functional reference classification
- `INSPIRATION`: screenshots only; no source.
- `DEMO`: functional preview, implementation not inspected.
- `SOURCE`: actual code inspectable, not yet built locally.
- `POC`: installed and built in target environment.
- `VERIFIED`: integrated into app with passing acceptance tests.

## Research artifact
Fill `ui-reference-evaluation.md` and a row in `traceability-matrix.csv`. A source URL alone is not evidence of functional parity.

## Avoid wrong assumptions
- Animated mockup != accessible input; beautiful dashboard != implemented API.
- A SaaS product screenshot cannot grant rights to its code, styles, icons or brand.
- Browser packages are not interchangeable with Compose, WinUI or React Native.
- Version claims, counts, license and pricing may change, and paid/pro source cannot be copied without authorization.
