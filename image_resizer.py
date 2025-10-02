# image_resizer.py

import os
from PIL import Image

# --- Configuration ---
# 1. Define the input and output folders.
INPUT_FOLDER = r'C:\Users\Sagar\Pictures\Wallpapers'
OUTPUT_FOLDER = 'output_images'

# 2. Define the new size (width, height) for the images.
NEW_SIZE = (800, 600) 

# 3. Define the output format (e.g., 'JPEG', 'PNG', 'WEBP').
OUTPUT_FORMAT = 'PNG'


def resize_and_convert_images():
    """
    Resizes and converts all images from the input folder and saves them
    to the output folder.
    """
    # [cite_start]Create the output folder if it doesn't exist [cite: 7]
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # [cite_start]Get the list of files in the input directory [cite: 16]
    files = os.listdir(INPUT_FOLDER)
    
    for filename in files:
        # Construct the full path for input and output files
        input_path = os.path.join(INPUT_FOLDER, filename)
        
        # Change the file extension for the output file
        file_basename, _ = os.path.splitext(filename)
        output_filename = f"{file_basename}.{OUTPUT_FORMAT.lower()}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # [cite_start]Use a try-except block to handle non-image files gracefully [cite: 20]
        try:
            # [cite_start]Open the image using Pillow [cite: 8, 14]
            with Image.open(input_path) as img:
                # [cite_start]Resize the image using the resize() method [cite: 8, 15]
                resized_img = img.resize(NEW_SIZE)
                
                # [cite_start]Save the resized image in the new format [cite: 8, 14, 18]
                resized_img.save(output_path, OUTPUT_FORMAT)
                
                print(f"✅ Successfully processed {filename} -> {output_filename}")

        except (IOError, SyntaxError) as e:
            print(f"❌ Could not process {filename}. It might not be an image file. Error: {e}")

if __name__ == "__main__":
    print("--- Starting Image Resizer Tool ---")
    resize_and_convert_images()
    print("--- All tasks completed! ---")