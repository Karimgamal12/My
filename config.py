from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "11371179")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "9ba892aa7ac568ab8094f609f8dca656")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5969211519:AAHafRveNCNdmBgwE6EdvAySmVqEUWLPXyg")
SESSION_NAME = getenv("SESSION_NAME", "BAABGwYLNcX6Pum-ZMjwWjLJALxufxJ-U0a9qkHjybgnBsmn5WzD1T5OiKWsRQmt_rOMB6lb-nCKTiGPl-wyr_cZSRF6kUoz_-Uumgqe8itKvYML-B7mecCrpaMe1WnG2uHrpMWUoTwkrH_Mioeo_pj8cuRe_3peXrHvpl1H2oLzQDJbi1koR11ZDLi7LhX3juWGK3CffK-7J-j3eRIaAXzrg2N9G2VdVLvaZ1hHD07Faecum1_t0-OMHMVyIkeGpe0kDl3GQaUZQAtFmFSHmstB-rtWOHzTFE42mq5vPPa_QtVDXKTUb4zBSBbqTt2Jxcdom7aZoTMy1EeZ_EB8kd2KAAAAAU1r5qoABAABGwYLNcX6Pum-ZMjwWjLJALxufxJ-U0a9qkHjybgnBsmn5WzD1T5OiKWsRQmt_rOMB6lb-nCKTiGPl-wyr_cZSRF6kUoz_-Uumgqe8itKvYML-B7mecCrpaMe1WnG2uHrpMWUoTwkrH_Mioeo_pj8cuRe_3peXrHvpl1H2oLzQDJbi1koR11ZDLi7LhX3juWGK3CffK-7J-j3eRIaAXzrg2N9G2VdVLvaZ1hHD07Faecum1_t0-OMHMVyIkeGpe0kDl3GQaUZQAtFmFSHmstB-rtWOHzTFE42mq5vPPa_QtVDXKTUb4zBSBbqTt2Jxcdom7aZoTMy1EeZ_EB8kd2KAAAAAU1r5qoA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "e1_x_z") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "Dev monzer") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "XDEV_MEMO_BOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/rRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "UUX_VVX") # @ هنا ضغ يوزر كروبك بدون


UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "UUU_iiiiii") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.aPVu_9gtaPs.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5593884330").split(SUDO_USERS = list(map(int, getenv("SUDO_USERS"," 5593884330").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
