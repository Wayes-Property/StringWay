from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀 𝙎𝙏𝙍𝙄𝙉𝙂", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="𝘽𝘼𝘾𝙆", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/WayDevv")],
        [
            InlineKeyboardButton("𝙃𝙊𝙒 𝙏𝙊 𝙐𝙎𝙀", callback_data="help"),
            InlineKeyboardButton("𝘼𝘽𝙊𝙐𝙏", callback_data="about")
        ],
        [InlineKeyboardButton("𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝙊𝙒𝙉𝙀𝙍", url="https://t.me/waymethodd")],
    ]

    START = """
𝙃𝙀𝙇𝙇𝙊 {}

𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 {}

𝘽𝙊𝙏 𝙄𝙉𝙄 𝘿𝙄𝙂𝙐𝙉𝘼𝙆𝘼𝙉 𝙐𝙉𝙏𝙐𝙆 𝙈𝙀𝙉𝙂𝙃𝘼𝙎𝙄𝙇𝙆𝘼𝙉 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉.

𝙆𝘼𝙈𝙄 𝙈𝙀𝙈𝙄𝙉𝙏𝘼 𝘿𝘼𝙏𝘼 𝙃𝘼𝙉𝙔𝘼 𝙐𝙉𝙏𝙐𝙆 𝙈𝙀𝙉𝙂𝙃𝘼𝙎𝙄𝙇𝙆𝘼𝙉 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉.

𝙅𝙄𝙆𝘼 𝙍𝘼𝙂𝙐 𝙎𝙄𝙇𝘼𝙃𝙆𝘼𝙉 𝙃𝘼𝙎𝙄𝙇𝙆𝘼𝙉 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝙎𝙀𝘾𝘼𝙍𝘼 𝙈𝘼𝙉𝙐𝘼𝙇.

𝘽𝙔 @waymethodd
    """

    HELP = """
𝘼𝙑𝘼𝙄𝙇𝘼𝘽𝙇𝙀 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎

/about - **ABOUT THE BOT**
/help - **THIS MESSAGE**
/start - **START THE BOT**
/generate - **GENERATE SESSION**
/cancel - **CANCEL THE PROCESS**
/restart - **CANCEL THE PROCESS**
"""

    ABOUT = """
𝘼𝘽𝙊𝙐𝙏 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏

𝘽𝙊𝙏 𝙐𝙉𝙏𝙐𝙆 𝙈𝙀𝙉𝙂𝘼𝙈𝘽𝙄𝙇 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘽𝙔 @waymethodd

𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 : @waymethodd
    """
