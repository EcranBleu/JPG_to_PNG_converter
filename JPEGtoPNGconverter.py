from PIL import Image
import sys
import os
from pathlib import Path
import shutil

existing_folder = Path(sys.argv[1])
new_folder = Path(sys.argv[2])


# Defining the jpg (and only jpg) image copy into the destination folder.

def jpg_copy():
    for source_file in existing_folder.iterdir():
        if str(source_file).lower().endswith(('.jpg', '.jpeg')):
            shutil.copy(source_file, new_folder)


# Create destination folder and apply copy, or just apply copy if the folder already exists.

try:
    os.mkdir(new_folder)
    jpg_copy()
except FileExistsError:
    jpg_copy()

# Convert the files in the destination folder.

for target_image in new_folder.iterdir():
    if str(target_image).lower().endswith('.png'):
        continue
    with Image.open(target_image) as img:
        img_copy = img.copy()
        img_copy.save(f'{str(target_image).rsplit(".")[0]}.png')
    os.remove(target_image)