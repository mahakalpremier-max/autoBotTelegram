from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8916656407:AAG523Re_75MLzTkwPdeBdWLrn7EE7hgeeQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏏 Join Channel", url="https://t.me/mahakalhere")],
        [InlineKeyboardButton("🎁 Referral Bonus", callback_data="bonus")],
        [InlineKeyboardButton("📞 GET YOUR ID", url="https://www.mahakalpremier.com/")],
        [InlineKeyboardButton("Go To Website Now", url="https://www.mahakalpremier.com/"],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to RudraOne 🔥\n\nChoose an option below:",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
