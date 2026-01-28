epic-gemini

Scaffold for an Epic Games free-game claimer that uses undetected-chromedriver
and can hand off CAPTCHA handling to a Gemini Computer Use flow (human-in-the-loop).

Quickstart

- Install dependencies with uv:
  - `uv sync`
- Run CLI:
  - `uv run epic-gemini --user-data-dir /path/to/Chrome/User\ Data`

Lint and format

- `uvx ruff check .`
- `uvx ruff format .`

Type check

- `uvx pyright`

Notes

- This project only provides the basic structure and stubs. You must implement
  site-specific selectors and the Gemini API integration for your environment.

Flow Diagram

```mermaid
flowchart TD
  A([Start]) --> B[Launch undetected-chromedriver - native Chrome profile]
  B --> C[Go to free-games page]
  C --> D{List current free offers}
  D -->|for each offer| E[Open offer detail - new tab]
  E --> F{Price is Free?}
  F -->|No| G[Skip offer<br/>log mismatch]
  F -->|Yes| H[Click Get / Add to cart]
  H --> I{CAPTCHA or verification?}
  I -->|Yes| J[Pause automation - Gemini handoff for CAPTCHA]
  J --> K[User completes CAPTCHA]
  K --> H
  I -->|No| L{Redirected to checkout?}
  L -->|Yes| M[Back out / Continue shopping]
  L -->|No| N[Return to free-games list]
  G --> N
  N --> D

  D -->|done| O[Open cart]
  O --> P{All items free?}
  P -->|No| Q[Stop & ask user]
  P -->|Yes| R[Ask user to confirm final claim]
  R --> S{User confirms?}
  S -->|No| T[Exit without purchase]
  S -->|Yes| U[Click Place Order/Confirm]
  U --> V[Capture receipt + log titles/timestamp]
  V --> W([Done])
```
