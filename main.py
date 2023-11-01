import os
import cv2
import tkinter as tk
from tkinter import filedialog

def convert_to_grayscale(image_path):
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(image_path, gray_image)
        print(f"Converted {image_path} to grayscale.")
    except Exception as e:
        print(f"Error converting {image_path}: {str(e)}")

def convert_images_to_grayscale(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(directory_path, filename)
            convert_to_grayscale(image_path)

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    return directory

if __name__ == "__main__":
    directory = select_directory()

    if directory:
        convert_images_to_grayscale(directory)
        print("Conversion completed.")
    else:
        print("No directory selected.")
