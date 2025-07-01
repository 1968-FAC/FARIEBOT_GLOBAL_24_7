import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

TOKEN = os.getenv("TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GOOGLE_TRAFFIC_API_KEY = os.getenv("GOOGLE_TRAFFIC_API_KEY")
FLIGHTLABS_API_KEY = os.getenv("FLIGHTLABS_API_KEY")
RADAR_API_KEY = os.getenv("RADAR_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy FARIEBOT GLOBAL 24/7.\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
        "/trafico - Consulta el tráfico\n"
        "/vuelos - Consulta vuelos\n"
        "/radar - Información de radar"
    )

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Por favor, proporciona una ciudad: /clima <ciudad>")
        return
    ciudad = " ".join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        mensaje = f"Clima en {ciudad}:\n🌡 Temp: {data['main']['temp']}°C\n🌤 {data['weather'][0]['description']}"
    else:
        mensaje = "No se pudo obtener el clima."
    await update.message.reply_text(mensaje)

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de tráfico: [Aquí integrarías la API real]")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de vuelos: [Aquí integrarías la API real]")

async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de radar: [Aquí integrarías la API real]")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("trafico", trafico))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("radar", radar))
    app.run_polling()

if __name__ == "__main__":
    main()
