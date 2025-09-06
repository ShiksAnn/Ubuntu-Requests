import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for one or multiple URLs
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename or "." not in filename:
                filename = "https://ubuntu.com/blog/ubuntu-21-10-wallpaper-competition.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(filepath):
                    filename = f"{base}_{counter}{ext}"
                    filepath = os.path.join("Fetched_Images", filename)
                    counter += 1

            # Save the image in binary mode
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("Connection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
