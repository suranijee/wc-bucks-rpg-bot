"""
Config File - Bot ke liye sabhi settings
Ye file independent hai, sirf constants rakhti hai
"""

import os
from dotenv import load_dotenv

# .env file se settings load karo
load_dotenv()

# ============= BOT SETTINGS =============
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
BOT_PREFIX = "!"  # Quick access prefix
BOT_SLASH = "/"   # Slash commands

# ============= IDS =============
OWNER_ID = 1360331955354472589        # Aapka ID
CO_OWNER_ID = 1360862519484485744     # Co-owner ID
SERVER_ID = 1442454295399370835       # Aapka Discord Server

# ============= CURRENCY SETTINGS =============
CURRENCY_NAME = "🪙 Wc-Bucks"
CURRENCY_EMOJI = "💵"

# Reward Settings
DAILY_MESSAGE_REWARD_MIN = 1
DAILY_MESSAGE_REWARD_MAX = 50

ONLINE_ACTIVITY_REWARD_MIN = 10
ONLINE_ACTIVITY_REWARD_MAX = 100
ONLINE_ACTIVITY_TIME = 300  # 5 minutes in seconds

# ============= QUIZ SETTINGS =============
QUIZ_TIME_LIMIT = 5  # Seconds
QUIZZES_PER_DAY = 10
QUIZ_AUTO_TIME_MIN = 180  # 3 minutes
QUIZ_AUTO_TIME_MAX = 300  # 5 minutes
QUIZ_AUTO_CHANNEL_USER_REQUIREMENT = 2  # Kitne users online hone chahiye

# ============= PET SYSTEM =============
XP_PER_BUCK = 5  # 1 Buck = 5 XP
XP_PER_LEVEL = 1000  # 1000 XP = 1 level
BUCKS_PER_LEVEL = 1  # Har level = +1 Bucks/hour income

# ============= COLORS =============
EMBED_COLOR_SUCCESS = 0x00FF00  # Green
EMBED_COLOR_ERROR = 0xFF0000    # Red
EMBED_COLOR_INFO = 0x0099FF     # Blue
EMBED_COLOR_WARNING = 0xFFFF00  # Yellow

# ============= DATABASE =============
DATABASE_URL = "sqlite://db.sqlite3"  # Local SQLite database
# Production ke liye: "postgresql://user:password@localhost/dbname"

# ============= CHATGPT SETTINGS (Optional) =============
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY_HERE")
CHAT_MODEL = "gpt-3.5-turbo"