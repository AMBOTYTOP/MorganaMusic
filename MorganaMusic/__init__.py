from MorganaMusic.core.bot import PubliceMusic
from MorganaMusic.core.dir import dirr
from MorganaMusic.core.git import git
from MorganaMusic.core.userbot import Userbot
from MorganaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PubliceMusic()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
