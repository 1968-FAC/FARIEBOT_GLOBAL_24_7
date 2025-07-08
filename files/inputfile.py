from telegram import InputFile
import os

def cargar_imagen(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    return InputFile(open(ruta_archivo, 'rb'))

def cargar_documento(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    return InputFile(open(ruta_archivo, 'rb'))

def cargar_audio(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    return InputFile(open(ruta_archivo, 'rb'))
