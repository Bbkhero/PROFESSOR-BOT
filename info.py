import re, time
from os import environ
from Script import script  # Assuming 'script' is a separate module for texts/templates

# ID pattern to validate numeric IDs
id_pattern = re.compile(r'^.\d+$')

# Helper function to determine boolean values from environment variables
def is_enabled(value, default):
    value = value.strip().lower()
    return value in ["on", "true", "yes", "1", "enable", "y"] if value else default

# --- PyroClient Setup ---
API_ID = int(environ.get('API_ID', '26614080'))  # Default ID set
API_HASH = environ.get('API_HASH', '7d2c9a5628814e1430b30a1f0dc0165b')
BOT_TOKEN = environ.get('BOT_TOKEN', '7580767881:AAGjzqzkDXY5fxy6CboK0i6iGIASPPVcrpg')

# --- Bot Settings ---
WEBHOOK_ENABLED = is_enabled(environ.get("WEBHOOK", 'True'), True)  # Web support setting
UPTIME = time.time()

# Predefined image URLs
PICS = environ.get('PICS', (
    'https://graph.org/file/01ddfcb1e8203879a63d7.jpg '
    'https://graph.org/file/d69995d9846fd4ad632b8.jpg '
    'https://graph.org/file/a125497b6b85a1d774394.jpg '
    'https://graph.org/file/43d26c54d37f4afb830f7.jpg '
    'https://graph.org/file/60c1adffc7cc2015f771c.jpg '
    'https://graph.org/file/d7b520240b00b7f083a24.jpg '
    'https://graph.org/file/0f336b0402db3f2a20037.jpg '
    'https://graph.org/file/39cc4e15cad4519d8e932.jpg '
    'https://graph.org/file/d59a1108b1ed1c6c6c144.jpg '
    'https://te.legra.ph/file/3a4a79f8d5955e64cbb8e.jpg '
    'https://graph.org/file/d69995d9846fd4ad632b8.jpg'
)).split()

# --- Admins, Channels, & Users ---
ADMINS = [int(admin) if id_pattern.match(admin) else admin for admin in environ.get('ADMINS', '5606990991').split()]
CHANNELS = [int(ch) if id_pattern.match(ch) else ch for ch in environ.get('CHANNELS', '-1001899588945 -1002055520451').split()]

# Authentication Users
AUTH_USERS = [int(user) if id_pattern.match(user) else user for user in environ.get('AUTH_USERS', '').split()] + ADMINS
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002490446965')) if id_pattern.match(environ.get('AUTH_CHANNEL', '')) else None
AUTH_GROUPS = [int(grp) for grp in environ.get('AUTH_GROUP', '-1002101393086').split()]

# --- MongoDB Configuration ---
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://vzak7z02ib:WRN2RA3Apm94TiWk@cluster0.upqas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', 'Cluster0')
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# --- Filters Configuration ---
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)
WELCOM_PIC = environ.get("WELCOM_PIC", 'https://i.ibb.co/NZSRJfK/images.png')
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)

# Filter enable/disable options
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)

# --- URL Shortener ---
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# --- Other Settings ---
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002349193496'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '-1002187853993')

# Additional Settings
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# File storage channel and settings
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Log message template
LOG_MSG = (
    "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n"
    "⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n"
    "🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
)
