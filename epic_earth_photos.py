import os
import requests
from dotenv import load_dotenv
import urllib.parse
from image_utils import download_image
from image_utils import get_image_extension

def save_earth_photos(epic_images_data, num_photos, output_folder, api_key):
    if not epic_images_data:
        print("Не удалось получить данные о фотографиях Земли.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    base_url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        'api_key': api_key
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        epic_images_data = response.json()
        
        for index, image_info in enumerate(epic_images_data[:num_photos], start=1):
            image_date = image_info["date"].split()[0].replace("-", "/")
            image_name = image_info["image"]
            image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/png/{image_name}.png"
            extension = get_image_extension(image_url)
            file_path = os.path.join(output_folder, f"earth_photo_{index}{extension}")
            download_image(image_url, file_path)
            print(f"Фотография Земли {index} сохранена: {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")

def main():
    load_dotenv('.env')
    nasa_api_key = os.getenv('nasa_api')
    output_folder = "downloaded_images/earth"
    num_photos = 10
    save_earth_photos([], num_photos, output_folder, nasa_api_key)

if __name__ == "__main__":
    main()
