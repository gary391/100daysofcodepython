import colorgram


# Extract all colors from an image.

def extract_color(image, color_count):
    colors = colorgram.extract(image, color_count)
    # first_color = colors[0]
    # rgb = first_color.rgb
    color_palette = []
    for color in colors:
        rgb = color.rgb
        color_palette.append((rgb.r, rgb.g, rgb.b))
    return color_palette
print(extract_color('damien-hirst-spot-painting-for-sale.jpg', 60))
