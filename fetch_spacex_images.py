import argparse
import os
import requests

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"SpaceX image saved: {filename}")
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")

def fetch_spacex_last_launch(launch_id=None):
    base_url = "https://api.spacexdata.com/v5/launches"
    url = f"{base_url}/{launch_id}" if launch_id else f"{base_url}/latest"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        images = []
        if 'flickr' in data["links"] and data["links"]["flickr"]["original"]:
            images = data["links"]["flickr"]["original"]
        elif 'patch' in data["links"] and data["links"]["patch"]["large"]:
            images = [data["links"]["patch"]["large"]]
        elif 'patch' in data["links"] and data["links"]["patch"]["small"]:
            images = [data["links"]["patch"]["small"]]

        if images:
            print(f"Found {len(images)} images")
            folder_path = "downloaded_images/spacex"
            os.makedirs(folder_path, exist_ok=True)
            for i, image_url in enumerate(images):
                filename = os.path.join(folder_path, f"spacex_{i}.jpg")
                download_image(image_url, filename)
        else:
            print("No valid images found for this SpaceX launch.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch SpaceX launch images")
    parser.add_argument('--launch_id', help="ID of the SpaceX launch", default=None)
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)

if __name__ == "__main__":
    main()
