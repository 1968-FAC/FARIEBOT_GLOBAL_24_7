import os
import logging
import requests
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)
from dotenv import load_dotenv

# Carga las variables del entorno
load_dotenv()

# Llaves del entorno (reemplaza los nombres por los tuyos si es necesario)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")
TRAFFIC_API_KEY = os.getenv("TRAFFIC_API_KEY")

# ID de tu chat para enviar mensajes automáticos
CHAT_ID = os.getenv("CHAT_ID")  # Puedes poner tu chat_id directo o gestionarlo dinámicamente

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Bienvenido a FARI3L Global! 🚀\n"
        "Alertas automáticas de vuelos, clima y tráfico. No necesitas hacer nada, ¡te avisaré de todo! 😉"
    )

# Ejemplo de función: Consulta el clima de una ciudad
async def get_weather_alert():
    city = "Bogota,CO"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&lang=es&units=metric"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("weather"):
            desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            alert = f"🌦️ Clima actual en {city}: {desc}, {temp}°C"
        else:
            alert = "No se pudo obtener el clima."
    except Exception as e:
        alert = f"Error en clima: {e}"
    return alert

# Ejemplo de función: Consulta vuelos (simulado para ejemplo)
async def get_flight_alert():
    # Puedes usar tu propia integración real aquí
    alert = "✈️ Alerta de vuelos: Vuelo a Cancún 3:30pm, tiquetes con descuento especial. ¡Reserva ya!"
    return alert

# Ejemplo de función: Consulta tráfico (simulado)
async def get_traffic_alert():
    # Puedes usar Google Traffic o Waze si tienes la API
    alert = "🚦 Alerta de tráfico: Tráfico moderado en la vía al aeropuerto. ¡Sal con tiempo!"
    return alert

# Función que envía mensajes automáticos cada cierto tiempo
async def send_alerts(application):
    while True:
        weather = await get_weather_alert()
        flight = await get_flight_alert()
        traffic = await get_traffic_alert()
        message = f"{flight}\n{weather}\n{traffic}"
        try:
            await application.bot.send_message(chat_id=CHAT_ID, text=message)
        except Exception as e:
            logging.error(f"Error enviando alerta: {e}")
        await asyncio.sleep(1800)  # Espera 30 minutos (1800 segundos). Ajusta el tiempo según prefieras

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Comandos
    application.add_handler(CommandHandler("start", start))

    # Envía alertas automáticas
    application.job_queue.run_repeating(lambda _: asyncio.create_task(send_alerts(application)), interval=1800, first=10)

    print("Bot corriendo y enviando alertas automáticas.")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
