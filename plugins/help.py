from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="t.me/shineytsupport")
      ],
      [ 
        InlineKeyboardButton(
            "Say Hello!", url="https://www.instagram.com/callmeonlyshine/")]
    ])  
    helptxt = f"<b> Just send a Youtube url to download it in video or audio format!\n\n ~ @shinebarbhuiya </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
