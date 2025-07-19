# config.py

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# 基本配置 (Your Details)
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '14689508')) # আপনার API ID
API_HASH = environ.get('API_HASH', '79413cfe2dBcc93ddf1815ef588e80d5') # আপনার API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '8114449011:AAHHp0r9K9RAJXIiYdx7plcPaCGn_-Zz3Eo') # আপনার BOT TOKEN

# অ্যাডমিন এবং চ্যানেল (Admins and Channels)
ADMINS = [int(admin) for admin in environ.get('ADMINS', '7931847651').split()] # আপনার ADMIN ID
USERNAME = environ.get('USERNAME', "https://t.me/Mr_SuryaBhaskar")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100xxxxxxxxxx')) # লগ চ্যানেল আইডি দিন
CHANNELS = [int(ch) for ch in environ.get('CHANNELS', '-100xxxxxxxxxx').split()] # ফাইল স্টোর করা চ্যানেলগুলোর আইডি

# ডেটাবেস (Database)
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://...") # আপনার ডেটাবেস URI
DATABASE_NAME = environ.get('DATABASE_NAME', "SuryaXProvider")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'movie_files')

# অন্যান্য চ্যানেল (Other Channels)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100xxxxxxxxxx')) # ফাইল ডিলিট হলে যেখানে যাবে

# বট সেটিংস (Bot Settings)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False) # True করলে চ্যানেল থেকে কেউ ফাইল ফরোয়ার্ড করতে পারবে না
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True) # True রাখলে ফাইলগুলো একটি লিঙ্কে গ্রুপ করে দেবে

# অটো-ডিলিট কাউন্টডাউন (Auto-Delete Countdown)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = 600  # 600 সেকেন্ড = 10 মিনিট

# IMDB এবং ক্যাপশন (IMDB and Caption)
IMDB = is_enabled('IMDB', True) # True রাখলে সিনেমার পোস্টার ও তথ্য দেখাবে

# Heroku/Render এর জন্য (For Heroku/Render)
URL = environ.get("FQDN", "") # আপনার অ্যাপের URL দিন
ON_HEROKU = 'DYNO' in environ
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
