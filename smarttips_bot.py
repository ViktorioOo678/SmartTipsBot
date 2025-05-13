
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравей! Това е СмартТипс Бот. Използвай !анализ [мач], за да получиш прогноза.")

async def анализ(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        match = " ".join(context.args)
        await update.message.reply_text(f"Анализ за мача {match}:
- Форма: добра
- Прогноза: Над 2.5 гола")
    else:
        await update.message.reply_text("Моля, въведи мач след командата, например: !анализ Специя - Козенца")

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("анализ", анализ))

    app.run_polling()

if __name__ == "__main__":
    main()
