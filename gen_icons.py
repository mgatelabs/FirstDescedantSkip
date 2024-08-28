from PIL import Image

def forImage(image_name, icon_name):
    # Create images for different icon sizes
    icon_sizes = [(256, 256), (48, 48), (32, 32), (16, 16)]
    img = Image.open(image_name)

    # Save the images as an ICO file
    #icon_images[0].save(icon_name, format="ICO", sizes=[(size, size) for size in icon_sizes])

    img.save(icon_name, sizes=icon_sizes)

if __name__ == '__main__':
    forImage('one_screen.png', 'one_screen.ico')
    forImage('two_screens.png', 'two_screens.ico')
    forImage('skip.png', 'skip.ico')