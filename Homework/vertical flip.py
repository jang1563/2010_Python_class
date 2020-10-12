from cs1media import *


def ver(img):
    w,h = img.size()
    new_img = create_picture(w, h)
    for y in range(h):
        for x in range(w):
            new_img.set(x, y, img.get(x, h-y-1))
    return new_img


b = load_picture("C:/cs101/yuna.jpg")
ver(b).show()