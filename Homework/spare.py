from cs1media import *
yuna = load_picture("C:/cs101/yuna.jpg")



num = raw_input("Enter a function number (1~5)>  \n1. Flip horizontal \n2. Flip vertical \n3. Rotate on 90 \n4. Rotate on 180 \n5. Rotate on 270 \n \n")
num = int(num)

def flip(img, direction):
   w, h = img.size()
   new_img = create_picture(w, h)
   if direction == "h":
      for y in range(h):
         for x in range(w):
            new_img.set(x, y, img.get(w-x-1,y))
      return new_img
   if direction == "v":
      for y in range(h):
         for x in range(w):
            new_img.set(x, y, img.get(x, h-y-1))
      return new_img
   
   
   
   
def input_check(function_num):
   if function_num < 6 and function_num > 0:
      return True
   else :
      return False

def rotate(img, degrees):
   if degrees == 90:
      h, w = img.size()
      new_image = create_picture(w, h)
      for y in range(h):
         for x in range(w):
            new_image.set(x, y, img.get(y, w-x-1))
      return new_image
   if degrees == 180:
      a = flip(img, "h")
      new_image = flip(a, "v")
      return new_image
   if degrees == 270: 
      h, w = img.size()
      new_image = create_picture(w, h)
      for y in range(h):
         for x in range(w):
            new_image.set(x, y, img.get(h - y - 1, x))
      return new_image
   
def change_img(function_num, img):
   if input_check(function_num) == True:
      if num == int(1):
         return flip(img, "h").show()
      elif num == int(2):
         return flip(img, "v").show()
      elif num == int(3):
         return rotate(img, 90).show()
      elif num == int(4):
         return rotate(img, 180).show()
      elif num == int(5):
         return rotate(img, 270).show()
   else :
      print("Wrong input!!!")
     
change_img(num, yuna)

