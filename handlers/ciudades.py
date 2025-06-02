# handlers/ciudades.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from data.ofertas_data import ofertas_data
from handlers.callback_offers import enviar_oferta

async def mostrar_ciudades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        ["🏙️ Caracas", "🏙️ Valencia"],
        ["🏙️ Barquisimeto", "🏙️ Maracay"],
        ["🏙️ Maracaibo", "🏙️ Cabudare"],
        ["⬅️ Regresar"]
    ]
    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
    await update.message.reply_text("Selecciona tu ciudad:", reply_markup=reply_markup)

async def handle_ciudad_seleccion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    ciudades_all = ["🏙️ Caracas", "🏙️ Valencia", "🏙️ Barquisimeto", "🏙️ Maracay", "🏙️ Maracaibo", "🏙️ Cabudare"]

    if text in ciudades_all:
        ciudad = text.replace("🏙️ ", "")
        categoria = context.user_data.get("categoria")
        subcategoria = context.user_data.get("subcategoria")
        if not categoria or not subcategoria:
            await update.message.reply_text("Primero debes elegir categoría o subcategoría.")
            return

        # Enviar oferta:
        await enviar_oferta(update, context, categoria, subcategoria, ciudad)
        return

    if text == "⬅️ Regresar":
        from handlers.start import start
        await start(update, context)
        return
