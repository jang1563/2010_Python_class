from cs1media import *


def hor(img):
    w,h = img.size()
    r = create_picture(w, h)
    for y in range(h):
        for x in range(w):
            r.set(x, y, img.get(w-x-1,y))
    return r


b = load_picture("C:/cs101/yuna.jpg")
hor(b).show()