import random
from cs1graphics import *

img_path="C:/BlackJack/"

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', \
              '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



bj_board = Canvas(600,400,'dark green','Black Jack 101')


""" define the Card class 

"""
class Card(object):
    pass


def create_deck(number = 1):
    deck = []
    
    for j in range(4):
        for i in range(12):
            card = Card()
            card.suit = suit_names[j]
            card.face = face_names[i]
            card.value = value[i]
            card.image = Image(img_path+str(card.suit)+"_"+str(card.face)+".png")
            card.state = True
            deck.append(card)
    random.shuffle(deck)
    return deck
    """ 
    Create a list("deck") of all 52 cards, suffle them and return the list.
    The list 'deck' have to include Card objects
    A Card is represented by a object with four attributes: the face, the suit, value and the image object
    First, Have to define class 'Card'    
    """
    




def hand_value(hand):
    total = 0
    a=False
    b=0
    for card in hand:
        if card.face=="Ace":
            a=True
            b+=1
        total += card.value
    while b>0:
        if total>21:
            total-=10
        b-=1
    return total
    """
    hand is a list including card objects
    Compute the value of the cards in the list "hand"
    
    """





def card_string(card):
    article = "a "
    if card.face in ["8", "Ace"]:
        article = "an "
    return str(article + str(card.face) + " of " + str(card.suit))
    """
    Parameter "card" is a Card object
    Return a nice string to represent a card
    (sucn as "a King of Spades" or "an Ace of Diamonds")
    """
    





def ask_yesno(prompt):
    while True:
        a=raw_input(prompt)
        if a=="y":
            return True
        elif a=="n":
            return False
        else:
            print "I beg your pardon"
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False"
    If the user enters anything else, the function prints "I beg your pardon!", and asks again, repreting this until the user has entered a correct string.
    """





def draw_card(dealer,player):
    
    """
    This funuction add the cards of dealer and player to canvas, bj_board
    If the state of each Card object is false, then you have to show the hidden card image(Back.png). The dealer's first card is hidden state
    The parameter dealer and player are List objects including Card Objects
    
    The start position of dealer's card is (100,100)
    The start position of player's card is (100,300)

    You can use the following methods for positioning images and text:
    Image() Object,Text() Object,  moveTo() method , setDepth() method,

    You should use help function - 
    help('cs1graphics.Image') -> about Image(), moveTo(), setDepth()
    help('cs1graphics.Text') -> about Text(),moveTo(), setDepth()


    """    
    depth = 100
    x0,y0 = 100,100
    x1,y1 = 100,300

    bj_board.clear()
    for i in range(len(dealer)):
        if dealer[i].state==True:
            bj_board.add(dealer[i].image)
            dealer[i].image.moveTo(x0+i*20,y0)
            dealer[i].image.setDepth(depth-10*i)
        elif dealer[i].state==False:
            img=Image(img_path+"Back.png")
            bj_board.add(img)
            img.moveTo(x0+i*20,y0)
            img.setDepth(depth-10*i)
    for i in range(len(player)):
            bj_board.add(player[i].image)
            player[i].image.moveTo(x1+i*20,y1)
            player[i].image.setDepth(depth-10*i)                  
            
    text=Text("Your Total: " + str(hand_value(player)))
    text.moveTo(300,300)
    bj_board.add(text)
    
    if dealer[0].state==True:
        text=Text("Dealer Total: " + str(hand_value(dealer)))
        text.moveTo(300,100)
        bj_board.add(text)
        
def main():

    deck = []

    while True:    
        # prompt for starting a new game and create a deck
        print "Welcome to Black Jack 101!\n"
        if len(deck)<12:
            deck = create_deck()
    
    # create two hands of dealer and player
        dealer = []
        player = []

    # initial two dealings
        card = deck.pop()
        print "You are dealt " + card_string(card)
        player.append(card)

        card = deck.pop()
        print "Dealer is dealt a hidden card"
        card.state=False
        dealer.append(card)

        card = deck.pop()
        print "You are dealt " + card_string(card)
        player.append(card)

        card = deck.pop()
        print "Dealer is dealt " + card_string(card)
        dealer.append(card)

        print "Your total is", hand_value(player)
        draw_card(dealer,player)


    # player's turn to draw cards
        while hand_value(player) < 21 \
                and ask_yesno("Would you like another card? (y/n) "):
        # draw a card for the player
            card = deck.pop()
            print "You are dealt " + card_string(card)
            player.append(card)
            print "Your total is", hand_value(player)
        
            draw_card(dealer,player)
    # if the player's score is over 21, the player loses immediately.     
        if hand_value(player) > 21:
            print "You went over 21! You lost."
            dealer[0].state = True
            draw_card(dealer,player)
        else:
        # draw cards for the dealer while the dealer's score is less than 17
            print "\nThe dealer's hidden card was " + card_string(dealer[0])
            while hand_value(dealer) < 17:
                card = deck.pop()
                print "Dealer is dealt " + card_string(card)
                dealer.append(card)
                print "The dealer's total is", hand_value(dealer)
        
            dealer[0].state = True
            draw_card(dealer,player)
        # summary        
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print "\nYour total is", player_total
            print "The dealer's total is", dealer_total
        
            if dealer_total > 21:
                print "The dealer went over 21! You win!"
            else:
                if player_total > dealer_total:
                    print "You win!"
                elif player_total < dealer_total:
                    print "You lost!"
                else:
                    print "You have a tie!"
            
        if not ask_yesno("\nPlay another round? (y/n) "):
            bj_board.close()
            break



    

main()
