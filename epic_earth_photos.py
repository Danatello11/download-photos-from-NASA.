import os
import requests
from dotenv import load_dotenv
from image_utils import download_image, get_image_extension

    

def fetch_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {'api_key': api_key}
    
    response = requests.get(url, params=params)
    if response.ok:
        return response.json()
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        return []


def save_earth_photos(epic_images, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for index, image_info in enumerate(epic_images, start=1):
        image_date = image_info["date"].split()[0].replace("-", "/")
        image_name = image_info["image"]
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/png/{image_name}.png"
        extension = get_image_extension(image_url)
        file_path = os.path.join(output_folder, f"earth_photo_{index}{extension}")
        download_image(image_url, file_path)
        print(f"Фотография Земли {index} сохранена: {file_path}")

def main():
    load_dotenv('.env')
    nasa_api_key = os.getenv('NASA_API')
    output_folder = "downloaded_images/earth"
    photos_num = 10
    epic_images = fetch_epic_images(nasa_api_key)[:photos_num]
    save_earth_photos(epic_images, output_folder)

if __name__ == "__main__":
    main()
