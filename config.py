# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "sharun")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "kwic2002")

# Account
API_HASH = os.environ.get("API_HASH", "d7b9e677664d2c87db4c4c0205b6e18f")
API_ID = os.environ.get("API_ID", "16929529")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5556181975:AAFEM7f5WsXhJK-ivXiWPXnkKDhPMJIcsas")
PICS = os.environ.get("PICS", "https://te.legra.ph/file/8dfe7256883cbc0190478.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "𝙆𝙒𝙄𝘾𝘽𝙊𝙏")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kwicbot:kwicbot@cluster0.mtrrmfd.mongodb.net/?retryWrites=true&w=majority")
# Chats & Users
ADMINS = os.environ.get("ADMINS", "942099709")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "kwicbotupdates")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001769691298")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001686640034").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001620413958")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001480651413")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "1800"))

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
