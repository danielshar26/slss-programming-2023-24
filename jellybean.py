# Jelly Bean Colour Counter
# Author: Daniel
# 9 January 2024

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")
red_pixels = []
green_pixels= []
yellow_pixels= []
yellow_pixel=(255,255,0)
green_pixel=(0,255,0)
red_pixel=(255,0,0)
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))
        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
        if colour_helper.pixel_to_name(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))
        if colour_helper.pixel_to_name(current_pixel) == "jelly bean yellow":
            yellow_pixels.append((x, y))
red_pixel_count = len(red_pixels)
green_pixel_count = len(green_pixels)
yellow_pixel_count = len(yellow_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height
red_pixel_percentage = red_pixel_count / total_pixels * 100
green_pixel_percentage = green_pixel_count/total_pixels*100
yellow_pixel_percentage = yellow_pixel_count/total_pixels*100
orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height
print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_pixel_percentage, 2)}%")
print(f"yellow Jelly Beans: {round(yellow_pixel_percentage, 2)}%")
newImg=Image.new("RGB", (orig_image_width, orig_image_height))
for pixel_location in red_pixels:
    newImg.putpixel(pixel_location,red_pixel)
newImg.save("./Images/red_map.jpg")
jelly_bean_img.close()