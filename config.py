import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID","6435225")) # Get this value from my.telegram.org/apps
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d") # Get this value from my.telegram.org/apps
BOT_TOKEN = getenv("BOT_TOKEN","5808748296:AAFrBWuAMhcXx-oshBGBWGhFoW050kcG9xI") # Get your token from @BotFather on Telegram.
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://morgana:kushal55@cluster0.9sexv.mongodb.net/?retryWrites=true&w=majority") # Get your mongo url from cloud.mongodb.com
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001717726836"))  # Chat id of a group for logging bot's activities/ Music Play Logs
PUBLICELOGS = int(getenv("PUBLICELOGS", "-1001841879487")) # Chat id of a group for Bot Added Messege/Leaved Messege U can Add Your Support Group id Aslo
GBANLOGS = int(getenv("GBANLOGS", "-1001908711819")) #Add Here Your Gbans Logs Channel Id 
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
SULTAN = int(getenv("SULTAN", "2105971379"))# Get this value from @Sophia_x_MusicBot on Telegram by /id
## Fill these variables if you're deploying on heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")# Your heroku app name
HEROKU_API_KEY = getenv("HEROKU_API_KEY") # Get it from http://dashboard.heroku.com/account
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AMBOTYTOP/MorganaMusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)# Fill this variable if your upstream repository is private
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Logs_Gban")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+jCS-YsVBVEE3NjQ1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True")) # Set this to "False" if you want the assistant to automatically leave chats after an interval
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170") #Leave it
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc") #Leave it
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25)) #Leave it
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000")) #Leave it
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000")) #Leave it
STRING1 = getenv("STRING_SESSION", "BQBr6tg-OurBV5pXriDhDaTC02Kb9wBHjCYvESfzilIS9mMfz6Gg4DqKJQs1vn18VpXctXNxW4YQ70ztMzDYikuhkVSFt7dlBM61RFUgTa1j35CVHqieAk4_jAbUypO8AIoMTwTUtMHATVqxBbAAsMZnan3mM6tszPfe8aOf6C-0znMBMqfu5UMD1Bbf6NwB5yHx4kXPxy6VAEEhcF6GVadpmKHiB_niijBg1dgVt6y2mXazwG-9x6pxbTRX4THnFAQbQCb7ClvxMqzaiRpH2Ev6wrCyfWarlcIRBWwV7FnzigyG7AKjeXbYadpQfIaWTKSveQp6ZSX51iOVpj-6Pg_bAAAAAXvWhJAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
    "💞",
    "🔎",
    "🔍",
    "🧪",
    "💣",
     "⚡️",
     "🔥",
     "🕺",
     "🎩",
     "🌈",
     "🍷",
     "🥂",
     "🍾",
    "🥃",
    "🥤",
    "🍽",
    "🍭",
    "🚗",
    "🚕",
    "🚓",
    "🚑",
    "🚀",
    "💎",
    "🔮",
    "🪄",
    "💌",
    "⁉️",
    "💤",
    "🧨"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = ["https://graph.org/file/56515b2097e2d2314581f.jpg", 
                 "https://graph.org/file/56515b2097e2d2314581f.jpg", 
                 "https://graph.org/file/56515b2097e2d2314581f.jpg", 
                 "https://graph.org/file/56515b2097e2d2314581f.jpg", 
                 "https://graph.org/file/d358f08e96cb819481957.jpg", 
                 "https://graph.org/file/d358f08e96cb819481957.jpg", 
                 "https://graph.org/file/d358f08e96cb819481957.jpg"
                ]
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/56515b2097e2d2314581f.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL","https://graph.org/file/56515b2097e2d2314581f.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
