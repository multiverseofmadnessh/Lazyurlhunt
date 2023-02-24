# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "13290427"))
    API_HASH = os.environ.get("API_HASH", "c33b2f280810fc2f60a6387a4c4217f2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5894919927:AAHTPcseEL_HRJE7ik2SVGKa0nhKCqXSkE0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001711211283"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisk_search_ary_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5079629749"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aryan1082:aryan_1082@cluster0.jmqpi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/starkownerbot'>Lazy Url Hunterr</a>.

    Devs: 
        <a href='https://t.me/starkownerbot'>❤️ Stark Owner Bot ❤️</a>
    
    
🤖 My Name: <b>Mdisk Search Robot</b>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://render.com'>Render</a>



👨‍💻 Developer: <a href='https://t.me/starkownerbot'>Stark Owner Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨🏻‍💻 Developer : <a href='https://t.me/starkownerbot'>Stark Owner Bot</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/starkownerbot'>Stark Owner Bot</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

