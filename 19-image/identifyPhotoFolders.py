#! python3
# identifyPhotoFolders.py - Go through every folder on the hard drive and finds potential photo folders.
# A photo folder is a folder where more than half of the files are photos.
# A file is a photo if it has the extension .png or .jpg and a width and height larger than 500 pixels.

from PIL import Image, UnidentifiedImageError
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith('.png') and not filename.lower().endswith('.jpg'):
            numNonPhotoFiles += 1
            continue  # skip to next filename

        # Open image file using Pillow and check if height and width are larger than 500.
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
            if width > 500 and height > 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1
        except UnidentifiedImageError:
            numNonPhotoFiles += 1

    # If more than half of the files were photos, print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
