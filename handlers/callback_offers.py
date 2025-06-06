# handlers/callback_offers.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes
from data.ofertas_data import ofertas_data

async def enviar_oferta(update: Update, context: ContextTypes.DEFAULT_TYPE, categoria, subcategoria, ciudad):
    idx = context.user_data.get("indice_oferta", 0)
    try:
        lista_ofertas = ofertas_data[categoria][subcategoria][ciudad]
    except KeyError:
        await update.message.reply_text("Lo siento, aún no hay ofertas disponibles para esa selección.")
        return

    if idx < 0 or idx >= len(lista_ofertas):
        await update.message.reply_text("Lo siento, no hay más ofertas disponibles.")
        return

    oferta = lista_ofertas[idx]
    caption = (
        f"🏪 *{oferta['nombre']}*\n"
        f"📍 Dirección: {oferta['direccion']}\n"
        f"📝 Descripción: {oferta['descripcion']}\n"
        f"💰 Oferta: {oferta['oferta']}\n"
        f"📞 Teléfono: {oferta['telefono']}"
    )
    await update.message.reply_photo(
        photo=oferta["imagen"],
        caption=caption,
        parse_mode="Markdown"
    )

    keyboard = [
        [InlineKeyboardButton("🔁 Ver otra oferta", callback_data="SIGUIENTE_OFERTA")],
        [InlineKeyboardButton("⬅️ Regresar", callback_data="REGRESAR_MENU")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("", reply_markup=reply_markup)

    context.user_data["ciudad_actual"] = ciudad
    context.user_data["indice_of
