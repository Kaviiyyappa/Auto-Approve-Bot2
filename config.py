import os
from typing import List

API_ID = os.environ.get("API_ID", "36464925")
API_HASH = os.environ.get("API_HASH", "942f6440a3ab83321135d7c1927aba0a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8283429361:AAHHlyo0ji9sEpFALOURGbv4673kHCagLvE")
ADMIN = int(os.environ.get("ADMIN", "8422190094"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg https://i.ibb.co/LDxwffYv/pic.jpg https://i.ibb.co/m5BN0XPD/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003707618369"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rarajan06_db_user:bMpXc2LLO8BIqWo0@cluster0.ice8cwo.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNEL", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
