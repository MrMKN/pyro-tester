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
        text=f"Hello {message.from_user.mention} sugamaano π",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("π₯ ABOUT π₯", callback_data="about")
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
β£βͺΌπ ππ΄πππ΄π : π·π΄πππΊπΎ
β£βͺΌπ π³π°ππ°π±π°ππ΄ : πΌπΎππΎπ π°πππ½π²πΎ
β£βͺΌποΈ π»πΈπ±ππ°ππ : πΏππΎπΆππ°πΌ
β£βͺΌπ π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ 3
β£βͺΌπ¨βπ» π³π΄ππ΄π»πΎπΏπ΄π : πΌπ.πΌπΊπ½ ππΆ""", show_alert=True)




print("π₯π΄π²π΅ π°πΊ πΊπ»π¨πΉπ»π¬π«π")        
MKN.run()

