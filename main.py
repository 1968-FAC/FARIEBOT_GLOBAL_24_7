from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! El bot está funcionando correctamente. Usa /trafico para consultar el tráfico.")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de tráfico: [Aquí integrarías la API real].")

def main():
    token = os.getenv("TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trafico", trafico))

    app.run_polling()

if __name__ == "__main__":
    main()
