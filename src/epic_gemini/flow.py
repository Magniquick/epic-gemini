from __future__ import annotations

from epic_gemini.browser import BrowserSession
from epic_gemini.config import AppConfig
from epic_gemini.gemini_handoff import GeminiCaptchaHandoff


def run_flow(
    config: AppConfig,
    browser: BrowserSession,
    captcha_handoff: GeminiCaptchaHandoff,
) -> None:
    browser.go(config.start_url)

    # TODO: implement selectors for offer cards and price checks.
    # Placeholder loop for structure only.
    offers = []
    if config.max_offers is not None:
        offers = offers[: config.max_offers]

    for _offer in offers:
        # TODO: open offer detail page in new tab.
        # TODO: verify price is free.
        # TODO: click "Get" / "Add to cart".
        # TODO: detect CAPTCHA or verification gates.
        if False:
            captcha_handoff.request_user_resolution("CAPTCHA detected")

        # TODO: return to offers list.

    # TODO: open cart and verify all items free.
    if config.dry_run:
        print("[dry-run] Skipping checkout confirmation.")
        return

    # TODO: ask user for confirmation before placing order.
