import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy FARIEBOT GLOBAL 24/7.\nComandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
        "/trafico - Consulta el tráfico\n"
        "/vuelos - Consulta vuelos\n"
        "/radar - Información de radar"
    )

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        ciudad = ' '.join(context.args)
        await update.message.reply_text(f"Consultando clima para: {ciudad} [Aquí integras la API real]")
    else:
        await update.message.reply_text("Por favor proporciona una ciudad. Ejemplo: /clima Bogotá")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de tráfico: [Aquí integras la API real]")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de vuelos: [Aquí integras la API real]")

async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de radar: [Aquí integras la API real]")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("comenzar", start))
    application.add_handler(CommandHandler("clima", clima))
    application.add_handler(CommandHandler("trafico", trafico))
    application.add_handler(CommandHandler("vuelos", vuelos))
    application.add_handler(CommandHandler("radar", radar))
    application.run_polling()

if __name__ == '__main__':
    main()
