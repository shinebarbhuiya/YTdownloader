
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="t.me/shineytsupport")
      ],
      [ 
        InlineKeyboardButton(
            "Say Hello!", url="https://instagram.com/callmeonlyshine")]
    ])
    welcomed = f"<b> Hey {message.from_user.first_name} , \n\nI'm ShineYt Bot. I can download video or audio f\n rom Youtube. \n\nMade by @shinebarbhuiya 😍/help for More info </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
