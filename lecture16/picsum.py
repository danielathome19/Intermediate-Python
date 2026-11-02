import requests


def get_rand_img(filename="sample.jpg", width=800, height=600):
    URL = f"https://picsum.photos/{width}/{height}"
    headers = {
        "User-Agent": "CS218-Lecture/1.0"
    }

    try:
        # stream=True keeps the connection open so we can stream raw bytes
        # instead of storing the entire image in RAM at once
        response = requests.get(URL, headers=headers, stream=True, timeout=10)
        response.raise_for_status()

        # Write the raw binary chunks to a file
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # 8 KiB
                if chunk:
                    file.write(chunk)
        print(f"Saved image to '{filename}'")
    except requests.RequestException as e:
        print("Failed to download image:", e)


def main():
    get_rand_img(filename="lecture16/picsum_demo.jpg")


if __name__ == "__main__":
    main()
