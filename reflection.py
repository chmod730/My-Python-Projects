"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    reflected = SimpleImage.blank(width, height * 2)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, height * 2 - (y + 1), pixel)
    return reflected


def main():
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
