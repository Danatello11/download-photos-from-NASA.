import os
import requests
from dotenv import load_dotenv
from image_utils import download_image, get_image_extension


def fetch_nasa_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    photos_num = 30
    params = {"api_key": api_key, "count": photos_num}
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    folder_path = "downloaded_images/nasa"
    os.makedirs(folder_path, exist_ok=True)
    for index, image in enumerate(images):
        image_url = image["url"]
        if "youtube" in image_url:
            print(f"Пропуск видео: {image_url}")
            continue
        extension = get_image_extension(image_url)
        filename = os.path.join(folder_path, f"nasa_{index}{extension}")
        download_image(image_url, filename)
        print(f"Фотография NASA сохранена: {filename}")

def main():
    load_dotenv('.env')
    api_key = os.getenv('NASA_API_KEY')
    fetch_nasa_apod(api_key)

if __name__ == "__main__":
    main()
