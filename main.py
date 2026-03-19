import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="أَهْلًا بِكَ! أَنَا بُوتٌ مَرْفُوعٌ مِنْ تِيرْمُوكْس إِلَى جِيت هَاب.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN_HERE').build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()
