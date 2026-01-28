from __future__ import annotations


class GeminiCaptchaHandoff:
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled

    def request_user_resolution(self, reason: str) -> None:
        if not self.enabled:
            raise RuntimeError("CAPTCHA encountered but Gemini handoff is disabled.")
        print(f"[captcha] User action required: {reason}")
        input("Solve the CAPTCHA in the browser, then press Enter to continue...")
