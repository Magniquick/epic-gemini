from __future__ import annotations

import argparse

from epic_gemini.browser import BrowserSession
from epic_gemini.config import AppConfig
from epic_gemini.flow import run_flow
from epic_gemini.gemini_handoff import GeminiCaptchaHandoff


def parse_args() -> AppConfig:
    parser = argparse.ArgumentParser(description="Epic Games free-game claimer scaffold.")
    parser.add_argument("--user-data-dir", required=True, help="Path to Chrome user data dir")
    parser.add_argument("--profile-dir", help="Chrome profile directory name")
    parser.add_argument("--headless", action="store_true", help="Run Chrome headless")
    parser.add_argument("--max-offers", type=int, help="Limit number of offers to process")
    parser.add_argument("--dry-run", action="store_true", help="Do not attempt checkout")
    args = parser.parse_args()

    return AppConfig(
        user_data_dir=args.user_data_dir,
        profile_dir=args.profile_dir,
        headless=args.headless,
        max_offers=args.max_offers,
        dry_run=args.dry_run,
    )


def main() -> None:
    config = parse_args()
    browser = BrowserSession.launch(config)
    try:
        run_flow(config, browser, GeminiCaptchaHandoff())
    finally:
        browser.close()


if __name__ == "__main__":
    main()
