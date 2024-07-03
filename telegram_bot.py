import os
import random
import time
import schedule
from telegram import Bot
from dotenv import load_dotenv


def load_bot_settings():
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    group_chat_id = os.getenv("GROUP_CHAT_ID")
    publication_interval = int(os.getenv("PUBLICATION_INTERVAL", 4))
    return bot_token, group_chat_id, publication_interval


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

def publish_photos():
    images = get_random_images(directory)
    while True:
        for image_path in images:
            send_image(bot_token, group_chat_id, image_path, caption="Привет, привет")
            time.sleep(publication_interval * 3600)  
        random.shuffle(images)  


def main():
     bot_token, group_chat_id, publication_interval = load_bot_settings()
     schedule.every(publication_interval).hours.do(publish_photos)
     while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()