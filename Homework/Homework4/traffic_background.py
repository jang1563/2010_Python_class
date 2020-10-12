from cs1graphics import *

############# background  ################
'''
You can ignore here.
'''

def draw_background(canvas_size):

    canvas_w, road_w = canvas_size
    # canvas settings
    canvas = Canvas(canvas_w, canvas_w, "lightgrey", "Traffic Simulation")

    # road settings
    space_w = canvas_w//2 - road_w//2
    road = Polygon(Point(space_w, 0), Point(space_w, space_w), \
                           Point(0, space_w), Point(0, canvas_w - space_w), \
                           Point(space_w, canvas_w - space_w), Point(space_w, canvas_w),\
                           Point(canvas_w - space_w, canvas_w), Point(canvas_w - space_w, canvas_w - space_w), \
                           Point(canvas_w, canvas_w - space_w), Point(canvas_w, space_w), \
                           Point(canvas_w - space_w, space_w), Point(canvas_w - space_w, 0))
    road.setFillColor("darkgray")
    road.setDepth(100)
    canvas.add(road)

    # centerlines settings
    centerlines = []
    centerlines.append(Path(Point(canvas_w//2, 0), Point(canvas_w//2, space_w)))
    centerlines[0].setBorderWidth(4)
    centerlines[0].setBorderColor("yellow1")
    centerlines[0].adjustReference(0, canvas_w//2)
    centerlines[0].setDepth(99)

    for i in range(3):
        centerlines.append(centerlines[i].clone())
        centerlines[i+1].rotate(90)
        centerlines[i+1].setDepth(99)
    
    for i in range(len(centerlines)):
        canvas.add(centerlines[i])

    return canvas
###############################################

if __name__ == '__main__':
    draw_background(500, 500, 100)
