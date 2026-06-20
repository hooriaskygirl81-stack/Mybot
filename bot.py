import telebot

TOKEN ="8705168654:AAFvFf3iQF1v-r7zMJRRsv5hKZZG8L0isR4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "✅ ربات با موفقیت روشن شد."
    )

print("Bot Started...")
bot.infinity_polling()