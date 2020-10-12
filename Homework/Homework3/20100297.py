from cs1graphics import *


#################################
# Global variables

index_list = [ ( 0, (0, 0) ), ( 1, (0, 2) ), ( 2, (2, 0) ),  ( 3, (2, 4) ),  ( 4, (4, 2) ) ]

word_list = [ ( 'ACROSS', 0, (0, 0), 3, 'BAA'  ), ( 'ACROSS', 2, (2, 0), 5, 'SOLID' ), ( 'ACROSS', 4, (4, 2), 3, 'WIT' ), ( 'DOWN', 0, (0, 0), 3, 'BUS' ), ( 'DOWN', 1, (0, 2), 5, 'ALLOW' ), ( 'DOWN', 3, (2, 4), 3, 'DOT' ) ]
word_description = [ ( 'ACROSS', 0, 'Sheep sound' ), ( 'ACROSS', 2, 'Neither liquid nor gas' ), ( 'ACROSS', 4, 'Humour' ), ( 'DOWN', 0, 'Road passenger transport' ), ( 'DOWN', 1, 'Permit' ), ( 'DOWN', 3, 'Shortened form of Dorothy' ) ]

word_state = [ 0, 0, 0, 0, 0, 0 ]

cell_size = 70

row_size = 5
col_size = 5

canvas_width = cell_size * col_size
canvas_height = cell_size * row_size

canvas = Canvas( canvas_width, canvas_height, 'black', 'CS101 - Crossword Puzzle' )



def draw_indices( _canvas, _index_list, _cell_size ) :
        for i in range( len( _index_list ) ) :
                a_word_index = Text(str(_index_list[i][0]),15)
                x_pos, y_pos = a_word_index.getDimensions()
                if i == 0:
                        x_pos = x_pos/2 + _cell_size*(0)
                        y_pos = y_pos/2 + _cell_size*(0)
                elif i == 1:
                        x_pos = x_pos/2 + _cell_size*(2)
                        y_pos = y_pos/2 + _cell_size*(0)
                elif i == 2:
                        x_pos = x_pos/2 + _cell_size*(0)
                        y_pos = y_pos/2 + _cell_size*(2)
                elif i == 3:
                        x_pos = x_pos/2 + _cell_size*(4)
                        y_pos = y_pos/2 + _cell_size*(2)
                elif i == 4:
                        x_pos = x_pos/2 + _cell_size*(2)
                        y_pos = y_pos/2 + _cell_size*(4)
                a_word_index.setFontColor("black")        
                a_word_index.moveTo(x_pos,y_pos)
                a_word_index.setDepth(10)
                _canvas.add( a_word_index )
               
                

def draw_horizontal_line( _canvas, _row_size, _cell_size ) :
        _canvas_width = _canvas.getWidth()
        
        for y in range( 1, _row_size ) :
                line = Path(Point(0,y*_cell_size), Point(canvas_width, y*_cell_size))
                line.setBorderColor("dark gray")
                line.setDepth(10)
                _canvas.add( line )
                            
                

def draw_vertical_line( _canvas, _col_size, _cell_size ) :
        _canvas_height = _canvas.getHeight()
        
        for x in range( 1, _col_size ) :
                line = Path(Point((x*_cell_size),0),Point((x*_cell_size),canvas_height))
                line.setBorderColor("dark gray")
                line.setDepth(10)
                _canvas.add(line)
                               
                

def get_a_word( _length, _word, _cell_size, _direction, _empty ) :
        a_word = Layer()
        
        for i in range( _length ) :
                a_word_cell = Square(_cell_size)
                a_word_cell.setFillColor("white")
                a_word_text = Text(_word[i] , 20)
                a_word_text.setDepth(30)
                x_pos = cell_size/2
                y_pos = cell_size/2
                if _direction == "ACROSS":
                        a_word_cell.moveTo(x_pos+i*cell_size,y_pos)
                        a_word_text.moveTo(x_pos+i*cell_size,y_pos)
                else :
                        a_word_cell.moveTo(x_pos,y_pos+i*cell_size)
                        a_word_text.moveTo(x_pos,y_pos+i*cell_size)
                             
                a_word.add( a_word_cell )
                
                if not _empty :
                        a_word.add( a_word_text )
        
        if not _empty :
                a_word.setDepth( 30 )
        
        return a_word

def draw_a_word( _canvas, _row, _col, _a_word, _cell_size ) :
        _a_word.moveTo( _cell_size*_col, _cell_size*_row )        
        _canvas.add( _a_word )
        
def draw_word_list( _canvas, _word_list, _word_state, _cell_size ) :
        for i in range( len( _word_list ) ) :
                a_word = get_a_word( _word_list[i][3], _word_list[i][4], _cell_size, _word_list[i][0], ( _word_state[i] == 0 ) )
                draw_a_word( _canvas, _word_list[i][2][0], _word_list[i][2][1], a_word, _cell_size )

def is_all_found( _word_state ) :
        all_found = False
        if _word_state.count(0) == 0:
                all_found = True
        return all_found
        
        

def print_description( _word_state, _word_description ) :
        for i in range(6):
                if _word_state[i]==0:
                        print _word_description[i][0]+"_"+str(_word_description[i][1]) + " : " + _word_description[i][2]                       
        

def is_right_choice( _user_choice, _word_description, _word_state ) :
        right_input = False
        len_des = len(_word_description)
        list1 = []
        list2 = []
        num1 = 0
        for i in range(len_des):
                if _word_description[i][0] == _word_description[0][0]:
                        list1.append(_word_description[i][1])
                        num1 += 1
                else :
                        list2.append(_word_description[i][1])
        if "_" in _user_choice:
                _user_choice = _user_choice.split("_")
                for i in range(len_des):
                        if _user_choice[0] in _word_description[i]:
                                if int(_user_choice[1]) in _word_description[i]:
                                        if i<num1:
                                                num2 = list1.index(int(_user_choice[1]))
                                        else:
                                                num2 = num1 + list2.index(int(_user_choice[1]))  
                                        if _word_state[num2] == 0:
                                                right_input = True
                        
        
        
       
                        
        return right_input

def is_right_word( _user_word, _user_choice, _word_list, _word_state ) :
        right_word = False
        len_des = len(_word_list)
        list1 = []
        list2 = []
        num1 = 0
        for i in range(len_des):
                if _word_list[i][0] == _word_list[0][0]:
                        list1.append(_word_list[i][1])
                        num1 += 1
                else :
                        list2.append(_word_list[i][1])
        if "_" in _user_choice:
                _user_choice = _user_choice.split("_")
                for i in range(len_des):
                        if _user_choice[0] in _word_list[i]:
                                if int(_user_choice[1]) in _word_list[i]:
                                        if _user_word in _word_list[i]:
                                                if i<num1:
                                                        num2 = list1.index(int(_user_choice[1]))
                                                else:
                                                        num2 = num1 + list2.index(int(_user_choice[1]))  
                                                _word_state[num2] = 1
                                                right_word = True
        return right_word
    


print 'Welcome to CS101 Crossword Puzzle!'
print ''

while not is_all_found(word_state) :
        canvas.clear()
        
        draw_indices( canvas, index_list, cell_size )        
        draw_horizontal_line( canvas, row_size, cell_size )
        draw_vertical_line( canvas, col_size, cell_size )
        draw_word_list( canvas, word_list, word_state, cell_size )
        
        print_description( word_state, word_description )
        print ''
        
        user_choice = raw_input( 'Enter a direction and number : ' )
        user_choice = user_choice.upper()
        if is_right_choice( user_choice, word_description, word_state ) :
                user_word = raw_input( 'Enter a word : ' )
                user_word = user_word.upper()
                if not is_right_word( user_word, user_choice, word_list, word_state ) :
                        print 'Please, enter a word, correctly!'
                
        else :
                print 'Please, enter a direction and number, correctly!'
        
        print ''

print 'Game complete!'
print ''

draw_indices( canvas, index_list, cell_size )        
draw_horizontal_line( canvas, row_size, cell_size )
draw_vertical_line( canvas, col_size, cell_size )
draw_word_list( canvas, word_list, word_state, cell_size )