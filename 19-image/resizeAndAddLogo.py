#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
LOGO_RESIZE = 0.25

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')) or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself.

    im = Image.open(filename)
    width, height = im.size
    newLogoWidth, newLogoHeight = logoWidth, logoHeight

    # Check if the image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        # Also resize the logo to make sure it's at max 25% of the image.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
            if width * LOGO_RESIZE < logoWidth:
                newLogoHeight = int(((width * LOGO_RESIZE) / logoWidth) * logoHeight)
                newLogoWidth = int(width * LOGO_RESIZE)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            if height * LOGO_RESIZE < logoHeight:
                newLogoWidth = int(((height * LOGO_RESIZE) / logoHeight) * logoWidth)
                newLogoHeight = int(height * LOGO_RESIZE)

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
        newLogoIm = logoIm.resize((newLogoWidth, newLogoHeight))

        # Add the logo.
        print('Adding logo to %s...' % (filename))
        im.paste(newLogoIm, (width - newLogoWidth, height - newLogoHeight), newLogoIm)

        # Save the changes.
        im.save(os.path.join('withLogo', filename))
