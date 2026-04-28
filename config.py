"""放置ゲーあるある図鑑 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "放置ゲーあるある図鑑"
BLOG_DESCRIPTION = "放置ゲーマーの心理・行動・生態をコラム形式で図鑑化。短文×イラスト風で「ライト勢→廃人」までのグラデーションを描く読み物メディア。"
BLOG_URL = "https://musclelove-777.github.io/idle-aru/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/idle-aru"

TARGET_CATEGORIES = [
    "ライト勢あるある",
    "中級者あるある",
    "廃人あるある",
    "復帰勢あるある",
    "サブ垢あるある",
    "イベント期間あるある",
    "引退宣言あるある",
]

THEME = {
    "primary": "#ff6b35",
    "accent": "#ffd166",
    "gradient_start": "#ff6b35",
    "gradient_end": "#ffd166",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
