import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
WEATHER_API = os.getenv("WEATHER_API")
FLIGHTS_API = os.getenv("FLIGHTS_API")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Bienvenido a FARIEBOT_GLOBAL_24_7\n"
        "Comandos disponibles:\n"
        "/clima <ciudad>\n"
        "/vuelos <origen> <destino>\n"
        "/trafico <ciudad>\n"
        "/radar"
    )

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🌦 Indica una ciudad. Ej: /clima Bogotá")
        return
    ciudad = ' '.join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={WEATHER_API}&units=metric&lang=es"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        await update.message.reply_text(f"⚠️ Ciudad no encontrada: {ciudad}")
    else:
        desc = res["weather"][0]["description"]
        temp = res["main"]["temp"]
        await update.message.reply_text(f"🌦 Clima en {ciudad}: {desc}, {temp}°C")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("✈️ Indica origen y destino. Ej: /vuelos BOG MIA")
        return
    origen = context.args[0].upper()
    destino = context.args[1].upper()
    url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHTS_API}&dep_iata={origen}&arr_iata={destino}"
    res = requests.get(url).json()
    if "data" not in res or not res["data"]:
        await update.message.reply_text(f"✈️ No se encontraron vuelos de {origen} a {destino}.")
    else:
        vuelo = res["data"][0]
        airline = vuelo["airline"]["name"]
        flight_iata = vuelo["flight"]["iata"]
        status = vuelo["flight_status"]
        await update.message.reply_text(f"✈️ Vuelo {flight_iata} de {airline}\nEstado: {status.capitalize()}")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚦 Módulo de tráfico: en desarrollo.")

async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛰 Módulo de radar global: en desarrollo.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("trafico", trafico))
    app.add_handler(CommandHandler("radar", radar))
    app.run_polling()

if __name__ == "__main__":
    main()
