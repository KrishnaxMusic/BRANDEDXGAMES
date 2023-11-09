from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BRANDED_WORLD"),
    ],
    [
        InlineKeyboardButton(
            text="💫 ɢᴀᴍᴇꜱ 💫",
            url=f"https://poki.com/",
        ),
    ],
    [
        InlineKeyboardButton(text="❤️‍🔥 ᴄʜᴀɴɴᴇʟ ❤️‍🔥", url=f"https://t.me/BRANDRD_BOT"),
        InlineKeyboardButton(text="💦 ᴀʙᴏᴜᴛ 💦", url=f"https://t.me/BRANDED_PAID_CC"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="💫 ɢᴀᴍᴇꜱ 💫",
            url=f"https://www.crazygames.com/t/with-friends",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✨ ᴄʟᴏsᴇ ✨",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BRANDED_WORLD"),
    ],
    [
        InlineKeyboardButton(text="❤️‍🔥 ᴄʜᴀɴɴᴇʟ ❤️‍🔥", url=f"https://t.me/BRANDRD_BOT"),
        InlineKeyboardButton(text="💦 ᴀʙᴏᴜᴛ 💦", url=f"https://t.me/BRANDED_PAID_CC"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❄️ ᴄʟᴏsᴇ ❄️", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BRANDED_WORLD"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="❤️‍🔥 ᴄʜᴀɴɴᴇʟ ❤️‍🔥", url=f"https://t.me/BRANDRD_BOT"),
        InlineKeyboardButton(text="💦 ᴀʙᴏᴜᴛ 💦", url=f"https://t.me/BRANDED_PAID_CC"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BRANDED_WORLD"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="❤️‍🔥 ᴄʜᴀɴɴᴇʟ ❤️‍🔥", url=f"https://t.me/BRANDRD_BOT"),
        InlineKeyboardButton(text="💦 ᴀʙᴏᴜᴛ 💦", url=f"https://t.me/BRANDED_PAID_CC"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="💫 ɢᴀᴍᴇꜱ 💫", url=f"https://poki.com/en/online-worlds"
        ),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BRANDED_WORLD"),
    ],
    [
        InlineKeyboardButton(text="❤️‍🔥 ᴄʜᴀɴɴᴇʟ ❤️‍🔥", url=f"https://t.me/BRANDRD_BOT"),
        InlineKeyboardButton(text="💦 ᴀʙᴏᴜᴛ 💦", url=f"https://t.me/BRANDED_PAID_CC"),
    ],
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", url=f"https://t.me/BRANDEDKING82"),
        InlineKeyboardButton(text="✨ ɢᴀᴍᴇꜱ ✨", url=f"https://tbot.xyz/lumber/#eyJ1Ijo2MjU4ODc3MjA1LCJuIjoi8J2XlfCdl6XwnZeU8J2XofCdl5fwnZeY8J2XlyDwk4ap8J+HvfCThqog8J2XnvCdl5zwnZeh8J2XmiAiLCJnIjoiTHVtYmVySmFjayIsImNpIjoiNDcyOTQ2MjUyMDMzMTM2MzY4NiIsImkiOiJCUUFBQUJYakRuVUJBQUFBNEFNQkFJTFZGWk9NV1RCQyJ9ZWNmMzMwMGE2NjJiZGVkMDI2OGUwZDg4ZGE4NWRiYjU=&tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DNxcccgVdfCQKNokgrfYJ"),
    ],
]
