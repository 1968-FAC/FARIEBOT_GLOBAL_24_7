import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuración de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Variables de entorno
TOKEN = os.getenv("TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
# Agrega aquí el resto si quieres usarlos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "¡Hola! Soy FARIEBOT GLOBAL 24/7.\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
        "/trafico - Consulta el tráfico\n"
        "/vuelos - Consulta vuelos\n"
        "/radar - Información de radar"
    )
    await update.message.reply_text(msg)

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor proporciona una ciudad. Ejemplo: /clima Bogotá")
        return
    ciudad = ' '.join(context.args)
    # Aquí puedes integrar la API real (ejemplo con OpenWeather)
    await update.message.reply_text(f"Información de clima para {ciudad}: [Aquí integras la API real]")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de tráfico: [Aquí integras la API real]")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de vuelos: [Aquí integras la API real]")

async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de radar: [Aquí integras la API real]")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("trafico", trafico))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("radar", radar))

    logging.info("BOT INICIADO 🚀")
    app.run_polling()

if __name__ == '__main__':
    main()
