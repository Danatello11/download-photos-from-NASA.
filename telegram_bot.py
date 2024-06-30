from telegram import Bot

bot_token = "7185204155:AAFFrYXob7fs_iCkrr4XpWNgso82TywrYVI"
group_chat_id = "-1002179626422"
message_text = "привет, привет"

bot = Bot(token=bot_token)
bot.send_message(chat_id=group_chat_id, text=message_text)
