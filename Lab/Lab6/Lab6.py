from cs1graphics import *
from time import *
import random

canvas = Canvas(640,580)
canvas.setTitle("Memento")

path = "C:/CS101/images/"
names = ("MinSoo.jpg","Junghwan.jpg","Juyoung.jpg","Yeongjae.jpg","Jinki.jpg","Hyungkyu.jpg")

names2 = ["MinSoo.jpg","MinSoo.jpg","MinSoo.jpg","MinSoo.jpg","Junghwan.jpg","Junghwan.jpg","Junghwan.jpg","Junghwan.jpg","Juyoung.jpg","Juyoung.jpg","Juyoung.jpg","Juyoung.jpg","Yeongjae.jpg","Yeongjae.jpg","Yeongjae.jpg","Yeongjae.jpg","Jinki.jpg","Jinki.jpg","Jinki.jpg","Jinki.jpg","Hyungkyu.jpg","Hyungkyu.jpg","Hyungkyu.jpg","Hyungkyu.jpg"]    

#return a list including 24 Image Object
# Example of creating Image Object
# img = Image(filename)
#
def load_images(filelist):
    cards = []
    for i in range(24):
        img = Image(path+filelist[i])
        temp_tuple = (img,filelist[i])
        cards.append(temp_tuple)
    return cards

#generate a layer object including a Rectangle and Text(number)
#parameter index is used to write a text 
def get_blank_card(index):
    pad = Layer()
    rect = Rectangle(90,120,Point(0,0))
    num = Text(str(index),16,Point(0,0))
    pad.add(rect)
    pad.add(num)

    return pad

# draw parameter cards in global variable canvas
# can use canvas.clear() method to clear the screen of  canvas object
# To arrange each card, you should use moveTo() and canvas.add() 
def draw_cards(cards):
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range( len(cards) ):
        if correct_list[i]==True:
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            bc = get_blank_card(i)
            bc.moveTo(i_w + w, i_h+h)
            canvas.add(bc)
        w += 100    
        if w % 600 == 0:
            w = 0
            h += 130
def draw_cards_1(cards):
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range( len(cards) ):
        cards[i][0].moveTo(i_w + w, i_h+h)
        canvas.add(cards[i][0])
        w += 100    
        if w % 600 == 0:
            w = 0
            h += 130
def draw_cards_2(cards):
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range( len(cards) ):
        if False:
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            bc = get_blank_card(i)
            bc.moveTo(i_w + w, i_h+h)
            canvas.add(bc)
        w += 100    
        if w % 600 == 0:
            w = 0
            h += 130

# main routine ----------------------

cards = load_images(names2)
random.shuffle(cards)

correct_list = []
for i in range(24):
    correct_list.append(False)
    
   
print "### Welcome to the Python Memento game!!! ###"
draw_cards_1(cards)
canvas.clear()
draw_cards_2(cards)
while correct_list.count(True)==6:
    
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if num1==num2 or num1< 0 or num1>23 or num2<0 or num2>23 or correct_list[num1]==True or correct_list[num2]==True:
        continue
    
    if cards[num1][1] == cards[num2][1]:
        print "Good!"
        correct_list[num1]=True
        correct_list[num2]=True

        draw_cards(cards)
    else:
        print "Wrong!"
        correct_list[num1]=True
        correct_list[num2]=True
        draw_cards(cards)
        correct_list[num1]=False
        correct_list[num2]=False
        draw_cards(cards)
        
        
        