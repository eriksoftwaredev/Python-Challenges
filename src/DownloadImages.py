import os
import requests

def download_images(url, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Download and save the images until there are no more available
    i = 1
    while True:
        image_url = f"{url}/image{i:03d}.jpg"
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(os.path.join(output_dir, f"image{i:03d}.jpg"), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image{i:03d}.jpg")
            i += 1
        else:
            print(f"No more images found. Total images downloaded: {i-1}")
            break

# Test the function:
url = "http://699340.youcanlearnit.net"
output_dir = ".\\assets\\images"
    
download_images(url, output_dir)
