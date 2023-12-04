import os
from telebot import TeleBot

# Replace 'YOUR_BOT_TOKEN' with the actual token you received from BotFather
bot_token = os.getenv('BOT_TOKEN')
bot = TeleBot(bot_token)

from telebot import types

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "xin chào mình là trợ lý DNS !")

@bot.message_handler(func=lambda message: False)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: "newbi" in message.text.lower())
def handle_newbi_message(message):
    reply_text = (
        "Hướng dẫn sử dụng DNS:\n"
        "1. KHÔNG sử dụng VPN khi dùng cấu hình DNS này.\n"
        "2. KHÔNG dùng thêm 1 DNS khác khi dùng cấu hình DNS này.\n"
        "3. KHÔNG tắt nguồn khi dùng cấu hình DNS này. Nếu có thì chuyển sang chế độ máy bay trước.\n"
        "4. Khi dùng DNS, có thể cài chứng chỉ sống hoặc cc die điều kiện ứng dụng như bình thường, nên đừng quan tâm đã thu hồi hay chưa."
    )

    bot.reply_to(message, reply_text)

bot.polling()
