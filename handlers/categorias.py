# handlers/categorias.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_categorias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Mostrar menú principal de categorías
    if text == "🗂️ Categorías":
        teclado = [
            ["🍽️ Restaurantes", "🛒 Mercados"],
            ["🥤 Bebidas", "💊 Farmacias"],
            ["📱 Electrónica", "🏪 Tiendas"],
            ["⬅️ Regresar"]
        ]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text(
            "Aquí todas las categorías donde puedes ahorrar, luego selecciona tu subcategoría o ciudad:",
            reply_markup=reply_markup
        )
        return

    # Subcategorías Restaurantes
    if text == "🍽️ Restaurantes":
        teclado = [
            ["🍣 Sushi", "🍕 Pizza"],
            ["🍔 Comida rápida", "☕ Cafeterías"],
            ["🍳 Desayunos"],
            ["⬅️ Regresar"]
        ]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text("🍽️ Elige una subcategoría de Restaurantes:", reply_markup=reply_markup)
        return

    # Subcategorías Electrónica
    if text == "📱 Electrónica":
        teclado = [
            ["🧊 Línea blanca", "📱 Teléfonos"],
            ["📺 Televisores", "🔌 Otros"],
            ["⬅️ Regresar"]
        ]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text("📱 Elige una subcategoría de Electrónica:", reply_markup=reply_markup)
        return

    # Categorías directas (mercados, bebidas, farmacias, tiendas)
    directas = {
        "🛒 Mercados": ("mercados", "directo"),
        "🥤 Bebidas": ("bebidas", "directo"),
        "💊 Farmacias": ("farmacias", "directo"),
        "🏪 Tiendas": ("tiendas", "directo"),
    }
    if text in directas:
        categoria, subcategoria = directas[text]
        context.user_data["categoria"] = categoria
        context.user_data["subcategoria"] = subcategoria
        # Enviar a mostrar ciudades:
        from handlers.ciudades import mostrar_ciudades
        await mostrar_ciudades(update, context)
        return

    # Subcategoría elegida (Restaurantes o Electrónica)
    subcats_rest = ["🍣 Sushi", "🍕 Pizza", "🍔 Comida rápida", "☕ Cafeterías", "🍳 Desayunos"]
    subcats_elec = ["🧊 Línea blanca", "📱 Teléfonos", "📺 Televisores", "🔌 Otros"]
    if text in subcats_rest:
        context.user_data["categoria"] = "restaurantes"
        context.user_data["subcategoria"] = text.lower().replace(" ", " ")
        from handlers.ciudades import mostrar_ciudades
        await mostrar_ciudades(update, context)
        return
    if text in subcats_elec:
        context.user_data["categoria"] = "electronica"
        context.user_data["subcategoria"] = text.lower().replace(" ", " ")
        from handlers.ciudades import mostrar_ciudades
        await mostrar_ciudades(update, context)
        return

    # Botón “Regresar” devuelve al menú principal
    if text == "⬅️ Regresar":
        from handlers.start import start
        await start(update, context)
        return
