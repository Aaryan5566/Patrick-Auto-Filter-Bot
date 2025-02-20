import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23378704'))
API_HASH = environ.get('API_HASH', '15a02b4d02babeb79e8f328b0ead0c17')
BOT_TOKEN = environ.get('BOT_TOKEN', "7998698561:AAFLrWwEedW8b_UkH_rAjVV4BEhhSCUVijw")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/7e18cfe55b0086a68ce62.jpg https://graph.org/file/595470e256a6479921b64.jpg https://graph.org/file/db89f81917260e6fda9bd.jpg https://graph.org/file/4aaf40a42eaeadbd1f192.jpg https://graph.org/file/dadcc2b4f2a9ac109f89a.jpghttps://graph.org/file/91a1f743b8dc68736a015.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/aZ4.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://envs.sh/aZf.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/73f8243e23b6005dc9885.jpg'))
CODE = (environ.get('CODE', 'https://telegra.ph/file/72f425007b22d28bd935e.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', ''))
STREAM_API = (environ.get('STREAM_API', ''))
STREAMHTO = (environ.get('STREAMHTO', 'https://filmclan1.blogspot.com/p/how-to-open-kingurl-link.html'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7364818327').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002187501114').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# info.py

# Primary Database
PRIMARY_DB_URI = "mongodb+srv://username:password@cluster0.mongodb.net/PrimaryDB?retryWrites=true&w=majority"
PRIMARY_DB_NAME = "PrimaryDB"

# Secondary Database
SECONDARY_DB_URI = "mongodb+srv://username:password@cluster0.mongodb.net/SecondaryDB?retryWrites=true&w=majority"
SECONDARY_DB_NAME = "SecondaryDB"

# Verify
VERIFY = bool(environ.get('VERIFY', False))
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://filmclan1.blogspot.com/p/how-to-open-kingurl-link.html') # How to open tutorial link for verification

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'kingurl.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '52fc11e73a9d9da5ed673830b55ca9c252dda348')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/requestmoviesgroup0')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Patrick_Botz')
TUTORIAL = environ.get('TUTORIAL', 'https://filmclan1.blogspot.com/p/how-to-open-kingurl-link.html')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', '🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : Pᴀᴛʀɪᴄᴋ Bᴏᴛᴢ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002187501114'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'requestmoviesgroup0')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002318221129')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10" , "season 11" , "season 12" , "season 13" , "season 14", "season 15" , "season 16" , "season 17" , "season 18" , "season 19" , "season 20"]

EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40", "E41", "E42", "E43", "E44", "E45", "E46", "E47", "E48", "E49", "E50"]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "".format(FQDN) if ON_HEROKU or NO_PORT else \
    "".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://wee-kaile-flashpoint-8310314b.koyeb.app/".format(FQDN)
else:
    URL = "https://wee-kaile-flashpoint-8310314b.koyeb.app/".format(FQDN)

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002001547224'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
