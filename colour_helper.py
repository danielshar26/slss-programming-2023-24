# Colour Helper
# Functions that help wither colours

def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel
    Params:
        pixel - 3-tuple of values r, g, b
    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    average = (red + green + blue) / 3
    if average >= 128:
        return True
    else:
        return False
def is_gray(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel
    Params:
        pixel - 3-tuple of values r, g, b
    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    gray_average = (red + green + blue) / 3 *2
    if gray_average >= 133:
        return True
    else:
        return False
def is_dark_gray(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel
    Params:
        pixel - 3-tuple of values r, g, b
    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    gray_average = (red + green + blue) / 3 / 4
    if gray_average >= 133:
        return True
    else:
        return False
def pixel_to_grayscale(pixel: tuple) ->tuple:
    red, green, blue = pixel
    gray = int(red * 0.3 +green * 0.59 + blue * 0.11)
    return(gray,gray,gray)
def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour
    Params:
        pixel = 3-tuple of values (red, green, blue)
    Returns:
        name of the colour
    """
    red, green, blue = pixel
    # TODO: detect red pixels
    if red < 200 and blue < 200 and green > 220:
        return "green"
    elif red > 170 and green < 80 and blue < 85:
        return "red"
    elif red<60 and green >100 and blue <60:
        return "jelly bean green"
    elif red>220 and green <200 and blue <5:
        return "jelly bean yellow"
    else:
        return "colour unknown"
print(pixel_to_name((180, 3, 2)))
print(pixel_to_name((255, 255, 255)))