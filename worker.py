import os
import asyncio
import requests
from telegram import Bot

TOKEN = os.getenv("TOKEN")
WEATHER_API = os.getenv("WEATHER_API")
CHAT_ID = os.getenv("CHAT_ID")  # Debes definir este ID en tu Render env

bot = Bot(token=TOKEN)

async def enviar_alerta_clima():
    ciudad = "Bogotá"  # Puedes cambiar la ciudad
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={WEATHER_API}&units=metric&lang=es"
    while True:
        res = requests.get(url).json()
        if res.get("cod") == 200:
            desc = res["weather"][0]["description"]
            temp = res["main"]["temp"]
            mensaje = f"🌦 Alerta automática: Clima en {ciudad}: {desc}, {temp}°C"
            await bot.send_message(chat_id=CHAT_ID, text=mensaje)
        await asyncio.sleep(600)  # Cada 10 minutos

if __name__ == "__main__":
    asyncio.run(enviar_alerta_clima())
