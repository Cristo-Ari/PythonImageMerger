from PIL import Image
import os
import math

def merge_images(folder_path, output_path):
    images = []
    max_width, max_height = 0, 0
    # Open and gather images from the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            images.append(img)
            # Track maximum width and height to determine grid size
            max_width = max(max_width, img.width)
            max_height = max(max_height, img.height)
    cols = math.ceil(math.sqrt(num_images))
    rows = cols
    # Calculate square size for the grid
    grid_width = cols * max_width
    grid_height = rows * max_height

    # Create a new image with white background
    new_img = Image.new('RGB', (grid_width, grid_height), (255, 255, 255))

    # Paste each image into the grid
    x_offset, y_offset = 0, 0
    for img in images:
        new_img.paste(img, (x_offset, y_offset))
        x_offset += max_width
        if x_offset >= grid_width:
            x_offset = 0
            y_offset += max_height

    # Save the merged image
    new_img.save(output_path)
    print(f"Merged images saved to {output_path}")

# Пример использования функции
folder_path = r'C:\Users\Administrator\Desktop\all'
output_path = r'C:\Users\Administrator\Desktop\merged_image_grid.jpg'
merge_images(folder_path, output_path)

