import os
import requests
from dotenv import load_dotenv

load_dotenv('nasa_api.env')
NASA_API = os.getenv('NASA_API')

def get_image_extension(image_url):
    filename = os.path.basename(image_url)
    _, extension = os.path.splitext(filename)
    return extension

def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as file:
        file.write(response.content)

def fetch_nasa_apod(NASA_API):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API, "count": 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    folder_path = "downloaded_images/nasa"
    os.makedirs(folder_path, exist_ok=True)
    for i, image in enumerate(images):
        image_url = image["url"]
        if "youtube" in image_url:
            print(f"Пропуск видео: {image_url}")
            continue
        extension = get_image_extension(image_url)
        filename = os.path.join(folder_path, f"nasa_{i}{extension}")
        download_image(image_url, filename)
        print(f"Фотография NASA сохранена: {filename}")

def main(): 
    fetch_nasa_apod(NASA_API)  

if __name__ == "__main__":
    main()
