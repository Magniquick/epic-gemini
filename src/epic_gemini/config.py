from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    user_data_dir: str
    profile_dir: str | None = None
    headless: bool = False
    start_url: str = "https://store.epicgames.com/en-US/free-games"
    max_offers: int | None = None
    dry_run: bool = False
