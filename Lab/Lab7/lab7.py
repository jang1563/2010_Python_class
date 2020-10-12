from cs1media import *

def scale(img):
    w,h = img.size()
    new_img = create_picture(w/4,h/4)
    norm = 4 ** 2
    for y in range(h/4):
        for x in range(w/4):
            r, g, b = 0, 0, 0
            x1 = x * 4
            y1 = y * 4
            for a1 in range(4):
                for a2 in range(4):
                    r0,g0,b0 = img.get(x1+a1,y1+a2)
                    r, g, b = r+r0, g+g0, b+b0
            r, g, b = r/norm, g/norm, b/norm
            new_img.set(x, y, (r, g, b))
    return new_img


def crossfade(img1, img2):
    yuna = scale(img1)
    wonbin = scale(img2)
    w,h = img1.size()
    new_img = create_picture(w,h)
    for j in range(4):
        for i in range(4):
            for y in range(h/4):
                for x in range(w/4):
                    r1,g1,b1 = yuna.get(x,y)
                    r2,g2,b2 = wonbin.get(x,y)
                    r1, g1, b1 = r1*((15-(4*i+j))/15.0), g1*((15-(4*i+j))/15.0), b1*((15-(4*i+j))/15.0)
                    r2,g2,b2 = r2*((4*i+j)/15.0),g2*((4*i+j)/15.0),b2*((4*i+j)/15.0)
                    r, g, b = r1 + r2, g1 + g2, b1 + b2
                    new_img.set(x+j*w/4,y+i*h/4,(r,g,b))
    new_img.show()
crossfade(load_picture("yuna.jpg"), load_picture("wonbin.jpg"))




