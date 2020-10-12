from cs1media import *



def luminance(p):
    r,g,b = p
    return int(0.299*r + 0.587*g + 0.114*b)
      

def sepia(img):
    w,h = img.size()
    new_img = create_picture(w, h, (0,0,0))
    for y in range(h):
        for x in range(w):
            v = luminance(img.get(x,y))
            r,g,b = v,v,v
            if v<=62:
                r = r*1.1
                b = b*0.9
            if v>63 and v<=191:
                r = r*1.15
                b = b*0.85
            if v>192:
                r = r*1.08
                b = b*0.93
                if r > 255:
                    r = 255
            new_img.set(x, y, (r,g,b))
    return new_img


pict = load_picture("C:/cs101/worlds/1.jpg")
sepia(pict).show()
