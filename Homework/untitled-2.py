from cs1media import *


def blackwhite(img, threshold):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            v = luminance(img.get(x, y))
            if v > threshold:
                img.set(x, y, white)
            else:
                img.set(x, y, black)
pict = load_picture("C:/cs101/yuna1.jpg")
blackwhite(pict, 100)
pict.show()