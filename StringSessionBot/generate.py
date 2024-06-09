from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

from data import Data


ask_ques = "𝙎𝙄𝙇𝘼𝙃𝙆𝘼𝙉 𝙋𝙄𝙇𝙄𝙃 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝙔𝙂 𝙄𝙉𝙂𝙄𝙉 𝘿𝙄𝘽𝙐𝘼𝙏"
buttons_ques = [
    [
        InlineKeyboardButton("𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠", callback_data="pyrogram"),
        InlineKeyboardButton("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗕𝗢𝗧", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗕𝗢𝗧", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡"
    else:
        ty = "𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠"
    if is_bot:
        ty += " 𝗕𝗢𝗧"
    await msg.reply(f"𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 {ty} 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙀𝙉𝘿 𝙔𝙊𝙐𝙍 `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('𝙉𝙊𝙏 𝘼 𝙑𝘼𝙇𝙄𝘿 API_ID. 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙀𝙉𝘿 𝙔𝙊𝙐𝙍 `API_HASH`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "𝙉𝙊𝙒 𝙎𝙀𝙉𝘿 𝙔𝙊𝙐𝙍 `PHONE_NUMBER` 𝙒𝙄𝙏𝙃 𝙏𝙃𝙀 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 𝘾𝙊𝘿𝙀. \𝙀𝙓𝘼𝙈𝙋𝙇𝙀 : `+6289*****`'"
    else:
        t = "𝙉𝙊𝙒 𝙎𝙀𝙉𝘿 𝙔𝙊𝙐𝙍 `BOT_TOKEN` \n𝙀𝙓𝘼𝙈𝙋𝙇𝙀 : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("𝗦𝗘𝗡𝗗𝗜𝗡𝗚 𝗢𝗧𝗣...")
    else:
        await msg.reply("𝗟𝗢𝗚𝗚𝗜𝗡𝗚 𝗔𝗦 𝗕𝗢𝗧 𝗨𝗦𝗘𝗥...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` & `API_HASH` 𝘾𝙊𝙈𝘽𝙄𝙉𝘼𝙏𝙄𝙊𝙉 𝙄𝙎 𝙄𝙉𝙑𝘼𝙇𝙄𝘿, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` 𝙄𝙎 𝙄𝙉𝙑𝘼𝙇𝙄𝘿, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "𝙋𝙇𝙀𝘼𝙎𝙀 𝘾𝙃𝙀𝘾𝙆 𝙁𝙊𝙍 𝘼𝙉 𝙊𝙏𝙋 𝙄𝙉 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝘼𝘾𝘾𝙊𝙐𝙉𝙏, \n𝙄𝙁 𝙊𝙏𝙋 𝙄𝙎 `12345`, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙀𝙉𝘿 𝙄𝙏 𝘼𝙎** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('𝙏𝙃𝙀 𝙇𝙄𝙈𝙄𝙏 𝙍𝙀𝘼𝘾𝙃𝙀𝘿 𝙊𝙁 10 𝙈𝙄𝙉𝙐𝙏𝙀𝙎. 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('𝙊𝙏𝙋 𝙄𝙎 𝙄𝙉𝙑𝘼𝙇𝙄𝘿, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('𝙊𝙏𝙋 𝙄𝙎 𝙀𝙓𝙋𝙄𝙍𝙀𝘿, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '𝙔𝙊𝙐𝙍 𝘼𝘾𝘾𝙊𝙐𝙉𝙏 𝙃𝘼𝙎 𝙀𝙉𝘼𝘽𝙇𝙀 𝙏𝙒𝙊-𝙎𝙏𝙀𝙋 𝙑𝙀𝙍𝙄𝙁𝙄𝘾𝘼𝙏𝙄𝙊𝙉. 𝙋𝙇𝙀𝘼𝙎𝙀 𝙋𝙍𝙊𝙑𝙄𝘿𝙀 𝙏𝙃𝙀 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('𝙏𝙃𝙀 𝙇𝙄𝙈𝙄𝙏 𝙍𝙀𝘼𝘾𝙃𝙀𝘿 𝙊𝙁 5 𝙈𝙄𝙉𝙐𝙏𝙀𝙎. 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 𝙋𝙍𝙊𝙑𝙄𝘿𝙀, 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙏𝘼𝙍𝙏 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝘼𝙂𝘼𝙄𝙉.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"{ty.upper()} 𝙎𝙏𝙍𝙄𝙉𝙂 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 \n\n`{string_session}` \n\𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀𝘿 𝘽𝙔 @stringway_bot"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗗 {} 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡. \n\𝗣𝗟𝗘𝗔𝗦𝗘 𝗖𝗛𝗘𝗖𝗞 𝗬𝗢𝗨𝗥 𝗦𝗔𝗩𝗘𝗗 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦🔥 \n\n𝘽𝙔 @waymethodd".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("𝘾𝘼𝙉𝘾𝙀𝙇𝙇𝙀𝘿 𝙏𝙃𝙀 𝙋𝙍𝙊𝘾𝙀𝙎𝙎!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙀𝘿 𝙏𝙃𝙀 𝘽𝙊𝙏!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("𝘾𝘼𝙉𝘾𝙀𝙇𝙇𝙀𝘿 𝙏𝙃𝙀 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀𝘿 𝙋𝙍𝙊𝘾𝙀𝙎𝙎!", quote=True)
        return True
    else:
        return False
