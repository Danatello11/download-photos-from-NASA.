import os
import random
import time
import schedule
from functools import partial
from telegram import Bot
from dotenv import load_dotenv


def get_random_images(directory):
    images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, file))
    random.shuffle(images)
    return images


def send_image(bot_token, chat_id, image_path, caption=None):
    bot = Bot(token=bot_token)
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption)


def publish_photos(bot_token, group_chat_id, directory):
    images = get_random_images(directory)
    for image_path in images:
        send_image(bot_token, group_chat_id, image_path, caption="Привет, привет")
        time.sleep(1)  # Вместо publication_interval уменьшим задержку до 1 секунды


def main():
    load_dotenv()
    bot_token = os.getenv("TG_BOT_TOKEN")
    group_chat_id = os.getenv("TG_GROUP_CHAT_ID")
    directory = "path_to_your_image_directory"
    publish_func = partial(publish_photos, bot_token, group_chat_id, directory) 
    publication_interval = int(os.getenv("PUBLICATION_INTERVAL", 4))
    schedule.every(publication_interval).hours.do(publish_func)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
