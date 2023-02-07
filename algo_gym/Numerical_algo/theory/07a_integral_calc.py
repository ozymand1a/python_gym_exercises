from math import sin

WIDTH = 0.01
ORIGINAL_SQUARE = 18.42


def get_y(x):
    return 1 + x + sin(2 * x)


def rectangle_square(x):
    return WIDTH * get_y(x)


def trapezoid_square(x):
    y1 = get_y(x)
    y2 = get_y(x + WIDTH)
    return WIDTH * ((y1 + y2) / 2)


def numerical_calculation_error(square):
    return 100 - square * 100 / ORIGINAL_SQUARE


if __name__ == '__main__':
    r_square, t_square = 0, 0
    x = 0
    while x < 5:
        r_square += rectangle_square(x)
        t_square += trapezoid_square(x)

        x += WIDTH

    print(f"Square by rectangles: {r_square:.2f} and error: {numerical_calculation_error(r_square):.2f}")
    print(f"Square by rectangles: {t_square:.2f} and error: {numerical_calculation_error(t_square):.2f}")
