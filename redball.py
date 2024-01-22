# Red Ball
# Author: Daniel
# 9 January 2024
rom PIL import Image
import colour_helper
red_ball = Image.open("./Images/Red Ball.jpeg")
red_pixels = []
red_pixel=(255,0,0)
orig_image_width = red_ball.width
orig_image_height = red_ball.height
for y in range(red_ball.height):
    for x in range(red_ball.width):
        current_pixel = red_ball.getpixel((x, y))
        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
newImg=Image.new("RGB", (orig_image_width, orig_image_height))
for pixel_location in red_pixels:
    newImg.putpixel(pixel_location,red_pixel)
newImg.save("./Images/red_ball_map.jpg")