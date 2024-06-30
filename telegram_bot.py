import os
import random
from telegram import Bot

bot_token = "7185204155:AAFFrYXob7fs_iCkrr4XpWNgso82TywrYVI"
group_chat_id = "-1002179626422"

def get_random_image(directory):
    images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, file))
    if not images:
        return None
    return random.choice(images)

def send_random_image(bot_token, chat_id, image_path, caption=None):
    bot = Bot(token=bot_token)
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

if __name__ == "__main__":
    image_path = get_random_image("downloaded_images")
    if image_path:
        send_random_image(bot_token, group_chat_id, image_path, caption="привет, это фото космоса")
    else:
        print("No images found in the specified directory.")
