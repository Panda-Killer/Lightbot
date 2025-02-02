class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5629555417"
    sudo_users = ["7251293982", "5629555417"]
    GROUP_ID = "-1002147955274"
    TOKEN = "7371599507:AAGNM516YsLzhtOtfQf8tcT1hWA89lr_Yls"
    mongo_url = "mongodb+srv://karan69:karan69@cluster0.gfw7e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "https://t.me/HyugaSupport"
    UPDATE_CHAT = "https://t.me/Hyuga_update"
    BOT_USERNAME = "@Fancy_Capable_bot"
    CHARA_CHANNEL_ID = "-1002147955274"
    api_id = "24835491"
    api_hash = "04ee66f0079a9b11eefb33a89289899e"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
