from PIL import Image
from concurrent.futures import ProcessPoolExecutor
import os


def resize_image(image_path):
    """ function that resize image to desired size
    """
    img = Image.open(image_path)
    img = img.resize((300, 300))

    new_name = f"resized_{os.path.basename(image_path)}"
    img.save(new_name)

    print(f"Processed: {new_name}")


if __name__ == "__main__":
    images = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpg"
    ]

    with ProcessPoolExecutor() as executor:
        executor.map(resize_image, images)

    print("All pictures processed.")
