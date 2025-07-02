import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Crear la aplicación
app = ApplicationBuilder().token(TOKEN).build()

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy FARIEBOT GLOBAL 24/7.\nComandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
        "/trafico - Consulta el tráfico\n"
        "/vuelos - Consulta vuelos\n"
        "/radar - Información de radar"
    )

# Comando /clima
async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Por favor proporciona una ciudad. Ejemplo: /clima Bogotá")
        return
    ciudad = " ".join(context.args)
    # Aquí integrarías la API real de clima
    await update.message.reply_text(f"Información de clima para {ciudad}: [Aquí integrarías la API real]")

# Comando /trafico
async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí integrarías la API real de tráfico
    await update.message.reply_text("Información de tráfico: [Aquí integrarías la API real]")

# Comando /vuelos
async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí integrarías la API real de vuelos
    await update.message.reply_text("Información de vuelos: [Aquí integrarías la API real]")

# Comando /radar
async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Aquí integrarías la API real de radar
    await update.message.reply_text("Información de radar: [Aquí integrarías la API real]")

# Registrar los handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clima", clima))
app.add_handler(CommandHandler("trafico", trafico))
app.add_handler(CommandHandler("vuelos", vuelos))
app.add_handler(CommandHandler("radar", radar))

# Iniciar polling
if __name__ == "__main__":
    app.run_polling()
