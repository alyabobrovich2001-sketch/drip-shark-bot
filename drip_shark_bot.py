import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# === НАСТРОЙКИ ===
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_CHAT_ID = 741159183  # твой chat ID
# =================

logging.basicConfig(level=logging.INFO)

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    # Формируем уведомление админу
    notification = (
        f"📦 Новый заказ!\n\n"
        f"👤 От: {user.full_name}"
        f"{f' (@{user.username})' if user.username else ''}\n"
        f"🆔 ID: {user.id}\n\n"
        f"💬 Сообщение:\n{message.text}"
    )

    # Отправляем уведомление админу
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=notification
    )

    # Отвечаем покупателю
    await message.reply_text(
        "Спасибо! Твой заказ принят 🦈\n"
        "Мы свяжемся с тобой в ближайшее время."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    print("Бот запущен ✅")
    app.run_polling()
