from PIL import Image
from random import randint

# blue color
blue_color = (0, 126, 255, 255)

# original square
ORIGINAL_SQUARE = 18.42

# square of 1 x 1 in pixels
square1x1 = 58 * 58


def numerical_calculation_error(square):
    return 100 - square * 100 / ORIGINAL_SQUARE


def monte_carlo_method(percent, pixels):
    rec_pixels = 0

    max_pixels = int(len(pixels) / (100 / percent))

    for i in range(max_pixels):
        rand = randint(0, len(pixels) - 1)
        pixel = pixels[rand]
        if pixel == blue_color:
            rec_pixels += 1

    return rec_pixels * 100 / max_pixels


if __name__ == '__main__':
    graph_map = Image.open("images/graph.png")
    width, height = graph_map.size
    square = width * height
    pixels = list(graph_map.getdata())

    rec_percent = monte_carlo_method(10, pixels)
    rec_square = (rec_percent * square / 100) / square1x1

    print(f"Square by Monte-Carlo: {rec_square:.2f} and error: {numerical_calculation_error(rec_square):.2f}")
