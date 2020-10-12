from cs1graphics import *
from time import *
import random

canvas = Canvas(640,580)
canvas.setTitle("Memento")

path = "./images/"

names = ["MinSoo.jpg","MinSoo.jpg","MinSoo.jpg","MinSoo.jpg","Junghwan.jpg","Junghwan.jpg","Junghwan.jpg","Junghwan.jpg","Juyoung.jpg","Juyoung.jpg","Juyoung.jpg","Juyoung.jpg","Yeongjae.jpg","Yeongjae.jpg","Yeongjae.jpg","Yeongjae.jpg","Jinki.jpg","Jinki.jpg","Jinki.jpg","Jinki.jpg","Hyungkyu.jpg","Hyungkyu.jpg","Hyungkyu.jpg","Hyungkyu.jpg"]    

class Cards(object):
    pass

def load_images(filelist):
    cards = []
    if len(filelist)!=24:
        return []

   
    for i in range(24):
        card=Cards()
        card.img = Image(path+filelist[i])
        card.name = filelist[i]
        card.state=True
        cards.append(card)
    
    
    return cards

def gen_blank_card(index):
    pad = Layer()
    rect = Rectangle(90,120,Point(0,0))
    num = Text(str(index),16,Point(0,0))
    pad.add(rect)
    pad.add(num)

    return pad

def draw_cards(cards):
    global canvas
    w = 0
    h = 0
    i_w = 70
    i_h = 90

    if len(cards)!=24:
        return False

    canvas.clear()

    for i in range(24):
        if cards[i].state :
            cards[i].img.moveTo(i_w+w,i_h+h)
            canvas.add(cards[i].img)
        else:
            pad = gen_blank_card(i)
            pad.moveTo(i_w+w,i_h+h)
            canvas.add(pad)

        w+=100
        if w%600 == 0:
            w = 0
            h +=130



    return True

def get_correct_answer(cards):
    count = 0
    for i in range(24):
        if cards[i].state:
            count+=1

    return count

def main():
    
 
    t_count = 0
    cards = load_images(names)    
    random.shuffle(cards)
    
    if not draw_cards(cards):
        print("Can not draw images!! exited!")
        return

    for i in range(24):
        cards[i].state = False

    sleep(2)    
    draw_cards(cards)
    
    while get_correct_answer(cards) < 24:
        
        if t_count == 1:
            print str(t_count) + "st try. You got " + str(get_correct_answer(cards))+" pairs."
        elif t_count == 2:
            print str(t_count) + "nd try. You got " + str(get_correct_answer(cards))+" pairs."
        elif t_count == 3:
            print str(t_count) + "rd try. You got " + str(get_correct_answer(cards))+" pairs."

        else:
            print str(t_count) + "th try. You got " + str(get_correct_answer(cards))+" pairs."

        try:
            num1 = int(raw_input("Input the first card number :"))
            num2 = int(raw_input("Input the secode card number :"))
        except ValueError:
            return
            
        if num1 >23 or num2 >23 :
            print "you have to choose number between 0 and 23"
            continue
        if num1==num2:
            print " you just choose different two numbers"
            continue

        t_count += 1
        cards[num1][2] = True
        cards[num2][2] = True

        if cards[num1][1]==cards[num2][1]:
            draw_cards(cards)
            print "Correct!"
        else:
            draw_cards(cards)
            sleep(1)
            cards[num1][2] = False
            cards[num2][2] = False
            draw_cards(cards)
            print "Wrong............."
                

main()

