
from math import *
from PIL import Image

image_file = "bluemarble.png"

in_width = 0
in_height = 0
out_width = 1000
out_height = 1000

max_lat = atan(sinh(pi))
min_lat = -atan(sinh(pi))


nan = float('nan')

def mercator(lon, lat):
    if lat > max_lat or lat < min_lat:
        return nan,nan

    return lon, log(tan(pi/4 + lat/2))

def inverse_mercator(x, y):
    
    return x, 2*atan(exp(y)) - pi/2

min_x = -pi
max_x = pi
min_y = mercator(0, min_lat)[1]
max_y = mercator(0, max_lat)[1]

def image_to_coordinate(x, y):
    lon = 2*pi * (x / in_width) - pi
    lat = pi * (1 - y / in_height) - pi/2

    return lon, lat

def plane_to_pixel(x, y):
    px = int(round(out_width  * ((x - min_x)/(max_x - min_x))))
    py = int(round(out_height * ((y - min_y)/(max_y - min_y))))

    return px, out_height - py

if __name__ == "__main__":
    im = Image.open(image_file)
    out = Image.new("RGB", (out_width, out_height), "white")

    in_width, in_height = im.size
    pix_in = im.load()
    pix_out = out.load()

    #for ix in range(in_width):
    #    print(ix)
    #    for iy in range(in_height):
    #        lon, lat = image_to_coordinate(ix, iy)
    #        x, y = mercator(lon, lat)

    #        if not (isnan(x) or isnan(y)):
    #            px, py = plane_to_pixel(x, y)
    #            if px >= 0 and px < out_width and py >= 0 and py < out_height:
    #                pix_out[px, py] = pix_in[ix, iy]

    for ox, oy in ((a,b) for a in range(out_width) for b in range(out_height)):
        px = 2*(max_x-min_x) * (ox/out_width) - min_x
        py = (max_y-min_y) * (1 - oy/out_height) - min_y/2

        lon, lat = inverse_mercator(px, py)
        ix = int(round(out_width * (lon + pi)/(2*pi)))
        iy = int(round(out_height * (lat + pi/2) / pi))
        
        print(ox,oy, ix, iy)

        pix_out[ox, oy] = pix_in[ix, out_height - iy]

    out.save("mercator.png")
    out.show()


