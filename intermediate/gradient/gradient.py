from PIL import Image

def lerp(low, high, progress):
    return low + (high - low)*progress

def get_gradient(width, height, leftcolor, rightcolor):
    
    image = Image.new("RGB", (width, height))

    r0, g0, b0 = leftcolor
    r1, g1, b1 = rightcolor

    for y in range(height):
        for x in range(width):
            p = x/width
            r, g, b = lerp(r0, r1, p), lerp(g0, g1, p), lerp(b0, b1, p)
            image.putpixel((x, y), (int(r), int(g), int(b)))
    return image

if __name__ == "__main__":
    image = get_gradient(1000, 100, (154, 21, 14), (1, 66, 37))
    
    image.save("gradient2.png")
