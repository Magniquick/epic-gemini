# Repository Guidelines

## Project Structure & Module Organization

- `src/epic_gemini/`: Core package. CLI entrypoint in `cli.py`, browser setup in
  `browser.py`, flow stub in `flow.py`, config dataclass in `config.py`, and
  CAPTCHA handoff stub in `gemini_handoff.py`.
- `main.py`: Thin entrypoint that forwards to the package CLI.
- `README.md`: Quickstart and usage notes.
- `pyproject.toml`: Dependencies and tooling configuration.

## Build, Test, and Development Commands

- `uv sync --extra dev`: Create `.venv` and install runtime + dev dependencies.
- `uv add --dev <package>`: Add dev dependencies (use `uv add <package>` only for normal deps); prefer over manual `pyproject.toml` edits.
- `uv run epic-gemini --user-data-dir /path/to/Chrome/User\ Data`: Run the CLI.
- `uvx ruff check .`: Lint the codebase.
- `uvx ruff format .`: Auto-format files.

There is no build step or packaging pipeline configured.

## Coding Style & Naming Conventions

- Python 3.12, formatted with Ruff (100 char line length).
- Use `snake_case` for functions/variables and `PascalCase` for classes.
- Prefer small modules with clear responsibilities (config, browser, flow).

## Testing Guidelines

- No test framework is configured yet.
- If you add tests, place them under `tests/` and name files `test_*.py`.
- Keep tests deterministic; avoid hitting external services unless mocked.

## Commit & Pull Request Guidelines

- No Git history exists yet, so there is no established commit convention.
- If you add commits, use concise messages (e.g., `Add flow stub for offers`).
- PRs should include: summary of changes, how to run checks, and any risks.

## Security & Configuration Notes

- The CLI expects a Chrome profile path via `--user-data-dir`. This can expose
  real session data, so use a dedicated profile when possible.
- CAPTCHA handling must be human‑in‑the‑loop; do not attempt to bypass or solve
  CAPTCHAs programmatically.

## ASCII Flow (Reference)

```
Start
  |
  v
Launch undetected-chromedriver (native profile)
  |
  v
Open /free-games page
  |
  v
For each free offer
  |
  +--> Open offer detail (new tab)
  |     |
  |     v
  |   Price = Free?
  |     |         \
  |     | Yes      \ No
  |     v           v
  |   Click Get     Skip + log
  |     |
  |     v
  |   CAPTCHA?
  |     |         \
  |     | Yes      \ No
  |     v           v
  |   User solves   Continue
  |     |
  |     v
  |   Back/continue shopping
  |
  v
Open cart
  |
  v
All items free?
  |         \
  | Yes      \ No
  v           v
Ask user      Stop + ask user
confirm
  |
  v
User confirms?
  |         \
  | Yes      \ No
  v           v
Place order  Exit
  |
  v
Log receipt + timestamps
  |
  v
Done
```
