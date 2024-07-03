import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"SpaceX image saved: {filename}")


def get_image_extension(image_url):
    filename = os.path.basename(image_url)
    _, extension = os.path.splitext(filename)
    return extension