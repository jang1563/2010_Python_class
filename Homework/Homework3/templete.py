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


#################################
# Definition of functions

def draw_indices( _canvas, _index_list, _cell_size ) :
        for i in range( len( _index_list ) ) :
                a_word_index = Text()
                
                '''
                [ Goal ]                
                Draw each index in the '_index_list' on the right location of the crossword game canvas.

                [ Requirements ]
                Each index is represented by a 'Text' object, which has attributes as follows :
                
                (1) The color of a 'Text' object is 'black'.
                (2) The size of a 'Text' object is 15.
                (3) The depth of a 'Text' object is 30.
                (4) The proper index should be set to a 'Text' object.
                (5) The position of a 'Text' object is upper-left corner of the cell.
                
                『 Note : Do not use global variables. Otherwise, you will get penalized.
                
                『 Hint : getDimensions() function returns the size of a 'Text' object by 'tuple' object.
                
                x_pos, y_pos = a_word_index.getDimensions()
                
                x_pos = x_pos/2 + _cell_size * (column_of_the_text_object)
                y_pos = y_pos/2 + _cell_size * (row_of_the_text_object)
                '''
                
                # Do something on here !!!
                
                
                _canvas.add( a_word_index )

def draw_horizontal_line( _canvas, _row_size, _cell_size ) :
        _canvas_width = _canvas.getWidth()
        
        for y in range( 1, _row_size ) :
                line = Path()
                
                '''
                [ Goal ]
                Draw each horizontal line on the right location of the crossword game canvas.

                [ Requirements ]
                Each horizontal line is represented by a 'Path' object, which has attributes as follows :
                
                (1) The border color of a 'Path' object is 'dark gray'.
                (2) The depth of a 'Path' object is 10.
                (3) Each line must stretch from the left-side border of the canvas to the right-side border of the canvas.
                
                『 Note : Do not use global variables. Otherwise, you will get penalized.
                
                『 Hint : addPoint() function is used to add points to a 'Path' object by using 'Point' object.
                '''
                
                # Do something on here !!!
                
                
                _canvas.add( line )

def draw_vertical_line( _canvas, _col_size, _cell_size ) :
        _canvas_height = _canvas.getHeight()
        
        for x in range( 1, _col_size ) :
                line = Path()
                
                '''
                [ Goal ]
                Draw each horizontal line on the right location of the crossword game canvas.
                
                [ Requirements ]
                Each horizontal line is represented by a 'Path' object, which has attributes as follows :
                
                (1) The border color of a 'Path' object is 'dark gray'.
                (2) The depth of a 'Path' object is 10.
                (3) Each line must stretch from the top-side border of the canvas to the bottom-side border of the canvas.
                
                『 Note : Do not use global variables. Otherwise, you will get penalized.
                
                『 Hint : addPoint() function is used to add points to a 'Path' object by using 'Point' object.
                '''
                
                # Do something on here !!!
                
                
                _canvas.add(line)

def get_a_word( _length, _word, _cell_size, _direction, _empty ) :
        a_word = Layer()
        
        for i in range( _length ) :
                a_word_cell = Square()
                a_word_text = Text()
                
                '''
                [ Goal ]
                Draw each word cell on the right location of a word layer.
                
                [ Requirements ]
                Each word cell is represented by a 'Square' object, which has attributes as follows :
                
                (1) The size of a 'Square' object is '_cell_size'.
                (1) A 'Square' object must be filled by 'white' color.
                
                If a word is not empty, there will be a letter on each word cell.
                And each letter is represented by a 'Text' object, wich has attributes as follows :
                
                (1) The font size is 20.
                (2) The font color is 'black'
                (3) The depth of a 'Text' object is 30.
                (4) The proper letter should be set to a 'Text' object.
                
                『 Note : Do not use global variables. Otherwise, you will get penalized.
                
                『 Note : A word layer has a direction 'across' or 'down'.
                
                If the direction of a word layer is 'across', each word cell must be put in 'horizontal' direction.
                If the direction of a word layer is 'down', each word cell must be put in 'vertical' direction.
                
                For example,
                
                the word layer for 'down0' consists of 'B', 'U', and 'S', and the direction of the word layer is 'down'.
                So, the layer must be formed like following :
                 ==
                | B |
                 ==
                | U |
                 ==
                | S |
                 ==
                
                The word layer for 'across2' consists of 'S', 'O', 'L', 'I', and 'D', and the direction of the word layer is 'across'.
                So, the layer must be formed like following :
                 == == == == ==
                | S | O | L |  I  | D |
                 == == == == ==
                
                '''
                
                # Do something on here !!!                
                
                
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
        
        '''
        [ Goal ]
        Check if there is a word not found yet.
        
        [ Requirements ]
        If there are still words left which are not found, 'is_all_found' function should return 'False'.
        If there is no word left which are not found, 'is_all_found' function should return 'True'
        
        『 Note : Do not use global variables. Otherwise, you will get penalized.
        '''
        
        # Do something on here !!!
        
        
        return all_found

def print_description( _word_state, _word_description ) :
        '''
        [ Goal ]
        Print out all the descriptions for the words, which are not found yet.
        
        [ Requirements ]
        Each line should keep the format of 'direction_num : description'.
        
        For example,
        
        if a word 'BAA' for 'across_0' and a word 'BUS' for 'down_0' are not found yet,
        then the text like follwing is expected :
        
        across_0 : Sheep sound
        down_0 : Road passenger transport
        
        『 Note : Do not use global variables. Otherwise, you will get penalized.
        
        『 Note : The descriptions only for the words not found yet should be print out.
        ( Do not print the descriptions for the word which are already found. )
        '''
        
        # Do something on here !!!
        
        

def is_right_choice( _user_choice, _word_description, _word_state ) :
        right_input = False
        
        '''
        [ Goal ]
        Check if an user's choice is correct.
        
        [ Requirements ]
        If an user's choice is in the list of words which are not found yet, 'is_right_choice' function should return 'True'.
        If an user's choice is not in the list of words which are not found yet, 'is_right_choice' function should return 'False'
        
        『 Note : Do not use global variables. Otherwise, you will get penalized.
        '''
        
        # Do something on here !!!
        
        
        return right_input

def is_right_word( _user_word, _user_choice, _word_list, _word_state ) :
        right_word = False
        
        '''
        [ Goal ]
        Check if an user's input word is correct.
        
        [ Requirements ]
        If an user's input word is in the list of words which are not found yet, 'is_right_word' function should return 'True'
        and set the word state of the chosen word from 0 to 1.
        
        If an user's input word is not in the list of words which are not found yet, 'is_right_word' function should return 'False'
        
        『 Note : Do not use global variables. Otherwise, you will get penalized.
        
        『 Note : Do not forget to set the word state of the word found from 0 to 1.
        '''
        
        # Do something on here !!!
        
        
        return right_word
    
#################################
# Run of the program

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
        
        if is_right_choice( user_choice, word_description, word_state ) :
                user_word = raw_input( 'Enter a word : ' )
                
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