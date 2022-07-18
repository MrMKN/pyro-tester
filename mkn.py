from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 


MKN = Client(
      "yourkeyword",
      bot_token="5231845980yG-mykf7-5d8zFx_X_RWcWBv_SUP0M",
      api_id="613425",
      api_hash="2d291700db7092d1f34f07c",
)

@MKN.on_message(filters.command("start")
async def start_text(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention} sugamaano 😉",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("💥 ABOUT 💥", callback_data="about")
            ]]
            )
        )


@MKN.on_message(filters.command("help")
async def help_text(mkn, msg):
    await msg.reply_sticker(
        sticker="CAADBQADEgQAAtMJyFVJOe6-VqYVzAI"
    )


@MKN.on_callback_query()
async def callback_data(client, query: CallbackQuery):
    if query.data == "about":
        await query.answer("""
┣⪼🚀 𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙷𝙴𝚁𝚄𝙺𝙾
┣⪼🍀 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 : 𝙼𝙾𝚃𝙾𝚁 𝙰𝚂𝚈𝙽𝙲𝙾
┣⪼🗂️ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚁𝙾𝙶𝚁𝙰𝙼
┣⪼📃 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 3
┣⪼👨‍💻 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : 𝙼𝚛.𝙼𝙺𝙽 𝚃𝙶""", show_alert=True)




print("💥𝑴𝑲𝑵 𝑰𝑺 𝑺𝑻𝑨𝑹𝑻𝑬𝑫🚀")        
MKN.run()

