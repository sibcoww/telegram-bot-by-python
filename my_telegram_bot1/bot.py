from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START")
    keyboard = [
        ["Make a sticker", "Use google drive", "Help"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Hello, I'm your bot!", reply_markup=reply_markup)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("HELP")
    await update.message.reply_text("/start - reset the bot\n" \
    "/help - write this text\n" \
    "/makesticker - make sticker by photo", reply_markup = ReplyKeyboardRemove())

async def handler_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo and context.user_data.get("waiting_for_photo"):
        await update.message.reply_text("I started to do sticker")
        context.user_data["waiting_for_photo"] = False

        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        await file.download_to_drive("to_sticker.png")

        with open("to_sticker.png", "rb") as img:
            await update.message.reply_sticker(sticker=img)

    elif context.user_data.get("waiting_for_photo") and not update.message.photo:
        context.user_data["waiting_for_photo"] = False
        await update.message.reply_text("It's not a photo. I reset your choose")
        await help(update, context)

    elif update.message.sticker :
        await update.message.reply_text("Cool sticker bro!")

    elif update.message.text:
        text = update.message.text.lower() 
        if text == "make a sticker":
            await makesticker(update, context)
        elif text == "help":
            await help(update, context)
        elif text == "use google drive":
            await google_drive(update, context)
            await context.user_data["WorkInGoogleDrive"] = True
        elif "hi" in text or "hello" in text:
            await update.message.reply_text("Hello my dear user))")
        elif "bye" in text or "bb" in text or "goodbye" in text:
            await update.message.reply_text("Bye my dear user))")
        else: 
            await update.message.reply_text("I can't reply that text. Sorry)")

async def makesticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me photo and i will do sticker.", reply_markup=ReplyKeyboardRemove())
    context.user_data["waiting_for_photo"] = True


async def google_drive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["WorkInGoogleDrive"] = True
if __name__ == "__main__":
    app = ApplicationBuilder().token("7230904619:AAEB2p-aCHVTOtyY0mu86YmTXanNpU0lSF4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    app.add_handler(MessageHandler(~filters.COMMAND, handler_any))
    app.add_handler(CommandHandler("makesticker", makesticker))
    app.run_polling()