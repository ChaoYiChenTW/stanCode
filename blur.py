"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """

def blur(img):
    """
    :param img: image
    :return: new_img, blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.width):
            img_p = img.get_pixel(x, y)
            sum_color = "0+0-0=0"  # to record the sum of red, blue, green and the count information
            if x != 0:
                sum_color = plus_color(img_p, sum_color)
                sum_color = plus_color(img.get_pixel(x - 1, y), sum_color)
                if y != 0: sum_color = plus_color(img.get_pixel(x - 1, y - 1), sum_color)
                if y != img.height - 1: sum_color = plus_color(img.get_pixel(x - 1, y + 1), sum_color)
            if x != img.width - 1:
                sum_color = plus_color(img.get_pixel(x + 1, y), sum_color)
                if y != 0: sum_color = plus_color(img.get_pixel(x + 1, y - 1), sum_color)
                if y != img.height - 1: sum_color = plus_color(img.get_pixel(x + 1, y + 1), sum_color)
            if y != 0: sum_color = plus_color(img.get_pixel(x, y - 1), sum_color)
            if y != img.height - 1: sum_color = plus_color(img.get_pixel(x, y + 1), sum_color)
            index1 = sum_color.find('+')
            index2 = sum_color.find('-')
            index3 = sum_color.find('=')
            red = int(sum_color[:index1])
            blue = int(sum_color[index1 + 1:index2])
            green = int(sum_color[index2 + 1:index3])
            count = int(sum_color[index3 + 1:])
            new_img_p = new_img.get_pixel(x, y)
            new_img_p.red = red // count
            new_img_p.blue = blue // count
            new_img_p.green = green // count
    return new_img

def plus_color(pixel, sum_color):
    """
    :param pixel: SimpleImage, image
    :param sum_color: str, with the sum of red, blue, green and the count information
    :return: sum_color, str
    """
    index1 = sum_color.find('+')
    index2 = sum_color.find('-')
    index3 = sum_color.find('=')
    red = pixel.red + int(sum_color[:index1])
    blue = pixel.blue + int(sum_color[index1 + 1:index2])
    green = pixel.green + int(sum_color[index2 + 1:index3])
    count = int(sum_color[index3 + 1:]) + 1
    sum_color = str(red) + '+' + str(blue) + '-' + str(green) + '=' + str(count)
    return sum_color


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
