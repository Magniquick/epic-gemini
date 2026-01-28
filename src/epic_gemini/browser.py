from __future__ import annotations

from dataclasses import dataclass

import undetected_chromedriver as uc

from epic_gemini.config import AppConfig


@dataclass
class BrowserSession:
    driver: uc.Chrome

    @classmethod
    def launch(cls, config: AppConfig) -> "BrowserSession":
        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={config.user_data_dir}")
        if config.profile_dir:
            options.add_argument(f"--profile-directory={config.profile_dir}")
        if config.headless:
            options.add_argument("--headless=new")
        driver = uc.Chrome(options=options)
        return cls(driver=driver)

    def go(self, url: str) -> None:
        self.driver.get(url)

    def close(self) -> None:
        self.driver.quit()
