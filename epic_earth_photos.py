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

def get_epic_earth_photos(output_folder, num_photos=10):
    url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data:
        for i, image_info in enumerate(data[:num_photos]):
            image_date = image_info["date"].split()[0].replace("-", "/")
            image_name = image_info["image"]
            image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/png/{image_name}.png"
            extension = get_image_extension(image_url)
            filename = os.path.join(output_folder, f"earth_photo_{i+1}{extension}")
            download_image(image_url, filename)
            print(f"Фотография Земли {i+1} сохранена: {filename}")
    else:
        print("Не удалось получить данные о фотографиях Земли.")

def main():
    output_directory = "downloaded_images/earth"
    get_epic_earth_photos(output_directory, num_photos=10) 

if __name__ == "__main__":
    main()
