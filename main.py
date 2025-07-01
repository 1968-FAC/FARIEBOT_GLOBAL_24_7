import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# ====== FUNCIONES ======

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "¡Hola! Soy FARIEBOT GLOBAL 24/7 🌍🚦✈️🌧\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima 🌦\n"
        "/trafico - Consulta el tráfico 🚦\n"
        "/vuelos - Consulta vuelos ✈️\n"
        "/radar - Información de radar 🌐"
    )
    await update.message.reply_text(msg)

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor indica una ciudad: /clima <ciudad>")
        return
    
    ciudad = ' '.join(context.args)
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            await update.message.reply_text(f"Ciudad no encontrada: {ciudad}")
            return
        clima_msg = (
            f"Clima en {ciudad}:\n"
            f"🌡 Temperatura: {data['main']['temp']}°C\n"
            f"💧 Humedad: {data['main']['humidity']}%\n"
            f"🌬 Viento: {data['wind']['speed']} m/s\n"
            f"☁️ Condición: {data['weather'][0]['description'].capitalize()}"
        )
        await update.message.reply_text(clima_msg)
    except Exception as e:
        await update.message.reply_text("Error al obtener el clima.")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí deberías integrar Google Traffic o TomTom API
    await update.message.reply_text("Información de tráfico: [Aquí integrarías la API real]")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí deberías integrar Aviationstack o Amadeus API
    await update.message.reply_text("Información de vuelos: [Aquí integrarías la API real]")

async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí deberías integrar la API del radar global
    await update.message.reply_text("Información de radar: [Aquí integrarías la API real]")

# ====== INICIO DEL BOT ======

async def main():
    token = os.getenv('TOKEN')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("trafico", trafico))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("radar", radar))

    print("✅ FARIEBOT GLOBAL 24/7 activo...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
