import os
from telebot import TeleBot, types

# Đọc token từ biến môi trường
bot_token = os.environ.get('BOT_TOKEN')
if bot_token is None:
    raise ValueError("BOT_TOKEN không được tìm thấy trong biến môi trường.")

bot = TeleBot(bot_token)

# Các đoạn mã khác ở đây không thay đổi

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
