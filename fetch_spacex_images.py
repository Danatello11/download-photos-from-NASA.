import argparse
import os
import requests
from image_utils import download_image


def save_spacex_images(images, output_folder):
    if not images:
        print("No valid images found for this SpaceX launch.")
        return

    os.makedirs(output_folder, exist_ok=True)
    print(f"Found {len(images)} images")
    for index, image_url in enumerate(images):
        filename = os.path.join(output_folder, f"spacex_{index}.jpg")
        download_image(image_url, filename)
        print(f"SpaceX image saved: {filename}")

def fetch_spacex_last_launch(launch_id=None):
    base_url = "https://api.spacexdata.com/v5/launches"
    url = f"{base_url}/{launch_id or 'latest'}"  
    response = requests.get(url)
    launch = response.json()
    links = launch.get("links", {})
    images = []
    if 'flickr' in links and links["flickr"].get("original"):
        images = links["flickr"]["original"]
    elif 'patch' in links and (links["patch"].get("large") or links["patch"].get("small")):
        images = [links["patch"].get("large") or links["patch"].get("small")]

    save_spacex_images(images, "downloaded_images/spacex")

def main():
    parser = argparse.ArgumentParser(description="Fetch SpaceX launch images")
    parser.add_argument('--launch_id', help="ID of the SpaceX launch", default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)

if __name__ == "__main__":
    main()
