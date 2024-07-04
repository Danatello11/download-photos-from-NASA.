import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_utils import download_image
from image_utils import get_image_extension

def load_nasa_api_key():
    load_dotenv('.env')
    return os.getenv('NASA_API')

def get_epic_images_url(api_key):
    base_url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        'api_key': api_key
    }
    return f"{base_url}?{urllib.parse.urlencode(params)}"


def save_earth_photos(epic_images_data, num_photos, output_folder):
    if not epic_images_data:
        print("Не удалось получить данные о фотографиях Земли.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    for index, image_info in enumerate(epic_images_data[:num_photos], start=1):
        image_date = image_info["date"].split()[0].replace("-", "/")
        image_name = image_info["image"]
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/png/{image_name}.png"
        extension = get_image_extension(image_url)
        file_path = os.path.join(output_folder, f"earth_photo_{index}{extension}")
        download_image(image_url, file_path)
        print(f"Фотография Земли {index} сохранена: {file_path}")

def get_epic_earth_photos(api_key, output_folder, num_photos=10):
    url = get_epic_images_url(api_key)
    try:
        response = requests.get(url)
        response.raise_for_status()
        epic_images_data = response.json()
        save_earth_photos(epic_images_data, num_photos, output_folder)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")

def main():
    load_dotenv('nasa_api.env')
    NASA_API_KEY = load_nasa_api_key()
    output_folder = "downloaded_images/earth"
    num_photos = 10
    get_epic_earth_photos(NASA_API_KEY, output_folder, num_photos)

if __name__ == "__main__":
    main()
