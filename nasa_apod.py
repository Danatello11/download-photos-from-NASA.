import requests
import os
from dotenv import load_dotenv
from image_utils import download_image
from image_utils import get_image_extension


def load_nasa_api_key():
    load_dotenv('nasa_api.env')
    return os.getenv('NASA_API')



def fetch_nasa_apod(NASA_API):
    url = "https://api.nasa.gov/planetary/apod"
    NUM_PHOTOS = 30
    params = {"api_key": NASA_API, "count": NUM_PHOTOS}
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
    NASA_API = load_nasa_api_key()
    fetch_nasa_apod(NASA_API)  

if __name__ == "__main__":
    main()
