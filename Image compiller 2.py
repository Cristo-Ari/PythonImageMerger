from PIL import Image, ImageOps
import os
import math
from tkinter import Tk, filedialog

def merge_images(folder_path):
    images_list = [Image.open(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.png'))]
    num_images = len(images_list)
    grid_size = math.ceil(math.sqrt(num_images))
    
    max_width = max(img.width for img in images_list)
    max_height = max(img.height for img in images_list)
    
    total_width = grid_size * max_width
    total_height = grid_size * max_height
    
    merged_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))
    
    for index, image in enumerate(images_list):
        row = index // grid_size
        col = index % grid_size
        resizedImage = image.resize((max_width, max_height))
        merged_image.paste(resizedImage, (col * max_width, row * max_height))
    parent_folder = os.path.abspath(os.path.join(folder_path, os.pardir))
    merged_image.save(os.path.join(parent_folder, "MergedImage.jpg"))

merge_images(filedialog.askdirectory(title="Select Folder with Images"))