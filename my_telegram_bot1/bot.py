from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive.file']
load_dotenv()
def is_drive_authorized():
    return os.path.exists("token.json")

def get_drive_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

async def google_drive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_drive_authorized():
        await update.message.reply_text("Auth is not done. Screen to auth going to open.")
        get_drive_service()  
        await update.message.reply_text("Auth succes!")

    keyboard = [["Upload to Drive", "Download from Drive"], ["Back"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Что вы хотите сделать?", reply_markup=reply_markup)
    context.user_data["in_drive_menu"] = True

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("MENU")
    keyboard = [
        ["Make a sticker", "Use google drive", "Menu"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Hello, I'm your bot! ", reply_markup=reply_markup)

async def handler_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Make sticker 
    if update.message.photo and context.user_data.get("waiting_for_photo"):
        await update.message.reply_text("I menued to do sticker")
        context.user_data["waiting_for_photo"] = False

        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        await file.download_to_drive("to_sticker.png")

        with open("to_sticker.png", "rb") as img:
            await update.message.reply_sticker(sticker=img)
    #make sticker but sent not a photo
    elif context.user_data.get("waiting_for_photo") and not update.message.photo:
        context.user_data["waiting_for_photo"] = False
        await update.message.reply_text("It's not a photo. I reset your choose")
        await menu(update, context)
    #sent a sticker
    elif update.message.sticker :
        await update.message.reply_text("Cool sticker bro!")
    #sent text
    elif update.message.text:
        text = update.message.text.lower() 
        #if in making sticker and want to back
        if context.user_data.get("waiting_for_photo") and text == "back":
            context.user_data["waiting_for_photo"] = False
            await menu(update, context)
        elif context.user_data.get("in_drive_menu") and text == "upload to drive":
            await update.message.reply_text("I'm waiting a file to upload.")
        elif context.user_data.get("in_drive_menu") and text == "download from drive":
            await update.message.reply_text("What's file do you want to download? ")

        elif text == "make a sticker":
            await makesticker(update, context)
        elif text == "menu":
            await menu(update, context)
        elif text == "use google drive":
            context.user_data["WorkInGoogleDrive"] = True
            await google_drive(update, context)
        elif "hi" in text or "hello" in text:
            await update.message.reply_text("Hello my dear user))")
        elif "bye" in text or "bb" in text or "goodbye" in text:
            await update.message.reply_text("Bye my dear user))")
        else: 
            await update.message.reply_text("I can't reply that text. Sorry)")

async def makesticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_for_photo"] = True
    keyboard = [
        ["Back"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Send me a photo to do a sticker. If you din't want it, press Back ", reply_markup=reply_markup)

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("menu", menu))

    app.add_handler(MessageHandler(~filters.COMMAND, handler_any))
    app.add_handler(CommandHandler("makesticker", makesticker))
    app.add_handler(CommandHandler("google_drive", google_drive))
    app.run_polling()