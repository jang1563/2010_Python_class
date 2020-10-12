from cs1graphics import *
import random

canvas = Canvas(300, 300)
canvas.setTitle("AMOLED bird")
canvas.setBackgroundColor('lightblue')

colorlist = ["aliceblue", "antiquewhite", "antiquewhite1", "antiquewhite2", "antiquewhite3", "antiquewhite4", "aquamarine", "aquamarine1", "aquamarine2", "aquamarine3", 
"aquamarine4", "azure", "azure1", "azure2", "azure3", "azure4", "beige", "bisque", "bisque1", "bisque2", 
"bisque3", "bisque4", "black", "blanchedalmond", "blue", "blue1", "blue2", "blue3", "blue4", "blueviolet", 
"brown", "brown1", "brown2", "brown3", "brown4", "burlywood", "burlywood1", "burlywood2", "burlywood3", "burlywood4", 
"cadetblue", "cadetblue1", "cadetblue2", "cadetblue3", "cadetblue4", "chartreuse", "chartreuse1", "chartreuse2", "chartreuse3", "chartreuse4", 
"chocolate", "chocolate1", "chocolate2", "chocolate3", "chocolate4", "coral", "coral1", "coral2", "coral3", "coral4", 
"cornflowerblue", "cornsilk", "cornsilk1", "cornsilk2", "cornsilk3", "cornsilk4", "cyan", "cyan1", "cyan2", "cyan3", 
"cyan4", "darkblue", "darkcyan", "darkgoldenrod", "darkgoldenrod1", "darkgoldenrod2", "darkgoldenrod3", "darkgoldenrod4", "darkgray", "darkgreen", 
"darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkolivegreen1", "darkolivegreen2", "darkolivegreen3", "darkolivegreen4", "darkorange", "darkorange1", 
"darkorange2", "darkorange3", "darkorange4", "darkorchid", "darkorchid1", "darkorchid2", "darkorchid3", "darkorchid4", "darkred", "darksalmon", 
"darkseagreen", "darkseagreen1", "darkseagreen2", "darkseagreen3", "darkseagreen4", "darkslateblue", "darkslategray", "darkslategray1", "darkslategray2", "darkslategray3", 
"darkslategray4", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deeppink1", "deeppink2", "deeppink3", "deeppink4", "deepskyblue", 
"deepskyblue1", "deepskyblue2", "deepskyblue3", "deepskyblue4", "dimgray", "dimgrey", "dodgerblue", "dodgerblue1", "dodgerblue2", "dodgerblue3", 
"dodgerblue4", "firebrick", "firebrick1", "firebrick2", "firebrick3", "firebrick4", "floralwhite", "forestgreen", "gainsboro", "ghostwhite", 
"gold", "gold1", "gold2", "gold3", "gold4", "goldenrod", "goldenrod1", "goldenrod2", "goldenrod3", "goldenrod4", 
"honeydew", "honeydew1", "honeydew2", "honeydew3", "honeydew4", "hotpink", "hotpink1", "hotpink2", "hotpink3", "hotpink4", 
"indianred", "indianred1", "indianred2", "indianred3", "indianred4", "ivory", "ivory1", "ivory2", "ivory3", "ivory4", 
"khaki", "khaki1", "khaki2", "khaki3", "khaki4", "lavender", "lavenderblush", "lavenderblush1", "lavenderblush2", "lavenderblush3", 
"lavenderblush4", "lawngreen", "lemonchiffon", "lemonchiffon1", "lemonchiffon2", "lemonchiffon3", "lemonchiffon4", "lightblue", "lightblue1", "lightblue2", 
"lightblue3", "lightblue4", "lightcoral", "lightcyan", "lightcyan1", "lightcyan2", "lightcyan3", "lightcyan4", "lightgoldenrod", "lightgoldenrod1", 
"lightgoldenrod2", "lightgoldenrod3", "lightgoldenrod4", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightpink1", "lightpink2", 
"lightpink3", "lightpink4", "lightsalmon", "lightsalmon1", "lightsalmon2", "lightsalmon3", "lightsalmon4", "lightseagreen", "lightskyblue", "lightskyblue1", 
"lightskyblue2", "lightskyblue3", "lightskyblue4", "lightslateblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightsteelblue1", "lightsteelblue2", "lightsteelblue3", 
"lightsteelblue4", "lightyellow", "lightyellow1", "lightyellow2", "lightyellow3", "lightyellow4", "limegreen", "linen", "magenta", "magenta1", 
"magenta2", "magenta3", "magenta4", "maroon", "maroon1", "maroon2", "maroon3", "maroon4", "mediumaquamarine", "mediumblue", 
"mediumorchid", "mediumorchid1", "mediumorchid2", "mediumorchid3", "mediumorchid4", "mediumpurple", "mediumpurple1", "mediumpurple2", "mediumpurple3", "mediumpurple4", 
"mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "mistyrose1", "mistyrose2", 
"mistyrose3", "mistyrose4", "moccasin", "navajowhite", "navajowhite1", "navajowhite2", "navajowhite3", "navajowhite4", "navy", "navyblue", 
"oldlace", "olivedrab", "olivedrab1", "olivedrab2", "olivedrab3", "olivedrab4", "orange", "orange1", "orange2", "orange3", 
"orange4", "orangered", "orangered1", "orangered2", "orangered3", "orangered4", "orchid", "orchid1", "orchid2", "orchid3", 
"orchid4", "palegoldenrod", "palegreen", "palegreen1", "palegreen2", "palegreen3", "palegreen4", "paleturquoise", "paleturquoise1", "paleturquoise2", 
"paleturquoise3", "paleturquoise4", "palevioletred", "palevioletred1", "palevioletred2", "palevioletred3", "palevioletred4", "papayawhip", "peachpuff", "peachpuff1", 
"peachpuff2", "peachpuff3", "peachpuff4", "peru", "pink", "pink1", "pink2", "pink3", "pink4", "plum", 
"plum1", "plum2", "plum3", "plum4", "powderblue", "purple", "purple1", "purple2", "purple3", "purple4", 
"red", "red1", "red2", "red3", "red4", "rosybrown", "rosybrown1", "rosybrown2", "rosybrown3", "rosybrown4", 
"royalblue", "royalblue1", "royalblue2", "royalblue3", "royalblue4", "saddlebrown", "salmon", "salmon1", "salmon2", "salmon3", 
"salmon4", "sandybrown", "seagreen", "seagreen1", "seagreen2", "seagreen3", "seagreen4", "seashell", "seashell1", "seashell2", 
"seashell3", "seashell4", "sienna", "sienna1", "sienna2", "sienna3", "sienna4", "skyblue", "skyblue1", "skyblue2", 
"skyblue3", "skyblue4", "slateblue", "slateblue1", "slateblue2", "slateblue3", "slateblue4", "slategray", "slategray1", "slategray2", 
"slategray3", "slategray4", "slategrey", "snow", "snow1", "snow2", "snow3", "snow4", "springgreen", "springgreen1", 
"springgreen2", "springgreen3", "springgreen4", "steelblue", "steelblue1", "steelblue2", "steelblue3", "steelblue4", "tan", "tan1", 
"tan2", "tan3", "tan4", "thistle", "thistle1", "thistle2", "thistle3", "thistle4", "tomato", "tomato1", 
"tomato2", "tomato3", "tomato4", "turquoise", "turquoise1", "turquoise2", "turquoise3", "turquoise4", "violet", "violetred", 
"violetred1", "violetred2", "violetred3", "violetred4", "wheat", "wheat1", "wheat2", "wheat3", "wheat4", "white", 
"whitesmoke", "yellow", "yellow1"]



class __Background():
    def __init__(self, width=300, height=300):
        self.width = 300
        self.height = 300
        
        
    def draw_scene(self):
        sunBody = Circle(60)
        sunBody.setFillColor('Red')
        sunBody.setBorderColor('darkred')
        sunBody.setBorderWidth(5)
        sunBody.moveTo(300, 0)
                
        sunLight1 = Rectangle(30, 5)
        sunLight1.setFillColor('Red')
        sunLight1.rotate(-10)
        sunLight1.moveTo(205, 20)
        
        sunLight2 = Rectangle(30, 5)
        sunLight2.setFillColor('Red')
        sunLight2.rotate(-45)
        sunLight2.moveTo(230, 60)
        
        sunLight3 = Rectangle(30, 5)
        sunLight3.setFillColor('Red')
        sunLight3.rotate(-80)
        sunLight3.moveTo(275, 85)
        

        Cloud1 = Circle(20, Point(70, 90))
        Cloud1.setFillColor('white')
        Cloud1.setBorderWidth(0)
        #Cloud1.moveTo(70, 90)
        Cloud2 = Circle(20)
        Cloud2.setFillColor('white')
        Cloud2.setBorderWidth(0)
        Cloud2.moveTo(100, 90)
        Cloud3 = Circle(20)
        Cloud3.setFillColor('white')
        Cloud3.setBorderWidth(0)
        Cloud3.moveTo(130, 90)
        
        Cloud4 = Circle(20)
        Cloud4.setFillColor('white')
        Cloud4.setBorderWidth(0)
        Cloud4.moveTo(170,140)
        Cloud5 = Circle(20)
        Cloud5.setFillColor('white')
        Cloud5.setBorderWidth(0)
        Cloud5.moveTo(200,140)
        Cloud6 = Circle(20)
        Cloud6.setFillColor('white')
        Cloud6.setBorderWidth(0)
        Cloud6.moveTo(230,140)
                
        
        canvas.add(sunBody)
        canvas.add(sunLight1)
        canvas.add(sunLight2)
        canvas.add(sunLight3)
        canvas.add(Cloud1)
        canvas.add(Cloud2)
        canvas.add(Cloud3)
        canvas.add(Cloud4)
        canvas.add(Cloud5)
        canvas.add(Cloud6)


class Bird():
    def __init__(self):
        self.layerBird = Layer()


        self.birdBody = Ellipse(50, 20)
        self.birdBody.setFillColor('purple')
        self.birdBody.setDepth(50)
        self.birdBody.moveTo(60, 250)
        
        self.birdHead = Circle(10)
        self.birdHead.setFillColor('royalblue')
        self.birdHead.moveTo(85, 250)
        self.birdEye = Circle(3)
        self.birdEye.setFillColor('white')
        self.birdEye.moveTo(88, 247)
        self.birdEyeS = Circle(1)
        self.birdEyeS.setDepth(-20)
        self.birdEyeS.setFillColor('blue')
        self.birdEyeS.moveTo(88, 247)
        self.birdBeak = Polygon(Point(30, 10), Point(10, 6), Point(10, 14), Point(30, 10))
        self.birdBeak.rotate(10)
        self.birdBeak.setFillColor('lightgoldenrod')
        self.birdBeak.moveTo(115, 255)
        
        self.birdWingR = Ellipse(50, 10)
        self.birdWingR.setFillColor('yellow')
        self.birdWingR.rotate(30)
        self.birdWingR.moveTo(40, 240)
        self.birdWingL = Ellipse(50, 10)
        self.birdWingL.setFillColor('yellow')
        self.birdWingL.setDepth(100)
        self.birdWingL.rotate(30)
        self.birdWingL.moveTo(47, 240)
        
        self.birdTale = Polygon(Point(10, 10), Point(30, 2), Point(30, 18), Point(10, 10))
        self.birdTale.rotate(180)
        self.birdTale.setFillColor('red')
        self.birdTale.moveTo(40, 250)
        self.birdTale.setDepth(100)
        
                
        self.layerBird.add(self.birdBody)
        self.layerBird.add(self.birdHead)
        self.layerBird.add(self.birdEye)
        self.layerBird.add(self.birdEyeS)
        self.layerBird.add(self.birdWingL)
        self.layerBird.add(self.birdWingR)
        self.layerBird.add(self.birdTale)
        self.layerBird.add(self.birdBeak)
        
        self.birdWingL.adjustReference(17, 10)
        self.birdWingR.adjustReference(17, 10)
        
        canvas.add(self.layerBird)
        
    def Fly(self):
        self.layerBird.move(8, 0)
       
    
    def Wing(self):
        self.birdWingL.rotate(-60)
        self.birdWingR.rotate(-60)
        self.birdWingL.rotate(60)
        self.birdWingR.rotate(60)


    def ColorChange(self):
        self.birdBody.setFillColor(random.choice(colorlist))
        self.birdHead.setFillColor(random.choice(colorlist))
        self.birdEye.setFillColor(random.choice(colorlist))
        self.birdEyeS.setFillColor(random.choice(colorlist))
        self.birdWingL.setFillColor(random.choice(colorlist))
        self.birdWingR.setFillColor(random.choice(colorlist))
        self.birdTale.setFillColor(random.choice(colorlist))
        self.birdBeak.setFillColor(random.choice(colorlist))
        
        
    
    
def interact():
    while True:
        user_inp = canvas.wait()
        description = user_inp.getDescription()
        if description == 'keyboard':
            inp_key = user_inp.getKey()
            if inp_key == 'f':
                myBird.Fly()
            elif inp_key == 'w':
                myBird.Wing()
            
            
        elif description == 'mouse click':
            myBird.ColorChange()
    

'''

while True:
    
    for i in range(60):
        birdWingL.rotate(-60)
        birdWingR.rotate(-60)
        birdWingL.rotate(60)
        birdWingR.rotate(60)
        layerBird.move(8, 0)
    
    layerBird.move(100, 0)
    layerBird.flip(180)
    
    for i in range(60):
        birdWingL.rotate(-60)
        birdWingR.rotate(-60)
        birdWingL.rotate(60)
        birdWingR.rotate(60)
        layerBird.move(-8, 0)
        
    layerBird.move(-100, 0)
    layerBird.flip(180)

'''


myBackground = __Background()
myBackground.draw_scene()

myBird = Bird()


interact()






