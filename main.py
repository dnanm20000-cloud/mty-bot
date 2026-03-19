import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="تَمَّ التَّشْغِيلُ بِنَجَاحٍ! هَذَا البُوتُ يَعْمَلُ الآنَ.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('8630383826:AAHEPPRgJuGoAHGgQ6lMQ9K3SiRyciIfjzo').build()
    application.add_handler(CommandHandler('start', start))
    print('--- البُوتُ قَيْدُ التَّشْغِيلِ الآنَ ---')
    application.run_polling()
