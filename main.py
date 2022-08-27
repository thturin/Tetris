import pgzrun
from tetris import *

#CONSTANTS
WIDTH = 400
HEIGHT = 500
DROP_START = ((WIDTH/2)+1,61)
#flag
pressing_down = False
game_over = False
game = Tetris(20,10)


def draw():
    screen.fill('white')

    for row in game.field:
        print(row)
    print('-------------------------------------------')

    for i in range(game.height): #rows
        for j in range(game.width): #columns
            anchor = (game.x+game.pixel_width * j,game.y+game.pixel_width*i)
            box_lw = (game.pixel_width,game.pixel_width)
            box = Rect(anchor, box_lw)
            screen.draw.rect(box, 'grey')  # Rect((left,top),(width,height))

            #the lines of code below draw the piece that has reached the last line
            if game.field[i][j]>0:
                box = Rect((game.x+game.pixel_width * j+1,game.y+game.pixel_width * i+1 ),(game.pixel_width-2,game.pixel_width-1))
                screen.draw.filled_rect(box,colors[game.field[i][j]])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j #p stanads for pixel in 4x4 figure square
                """
                [0  1  2  3  i=0, j=0,1,2,3
                 4  5  6  7  i=1 j=0,1,2,3
                 8  9 10 11
                12  13 14 15]
                """
                if p in game.figure.image(): #if p exists in the chosen array of numbers, it will be drawn in with a color and giving movement
                    """
                    use figures[0][0] as an example: [1,5,9,13] at i=0 and j=1, p=1 which exists in the list. This will be colored in.
                    """
                    anchor = (game.x + game.pixel_width * (j+game.figure.x)+1,game.y + game.pixel_width * (i+game.figure.y)+1)
                    print("anchor={}".format(anchor))
                    #the anchor coordinates is how the piece moves with game.figure.x and game.figure.y
                    box_lw = (game.pixel_width-2,game.pixel_width-2) #-2 so you can see grey lining of tetris board
                    box = Rect(anchor,box_lw)
                    screen.draw.filled_rect(box,colors[game.figure.color])


def on_mouse_move(pos):
    pass
    #print('position is {}'.format(pos))

def on_key_down(key):
    if key == key.LEFT:
        game.go_side(-1)
    elif key == key.UP:
        game.go_up()
    elif key == key.RIGHT:
        game.go_side(1)
    elif key == key.DOWN:
        game.go_down()
        pressing_down=True

def on_key_up(key):
    if key == key.DOWN:
        pressing_down=False

def spawn_figure():
    if game.figure is None:
        game.new_figure()

def move_piece():
    if game.figure is not None:
        game.go_down()

# if not pressing_down:
#     clock.schedule_interval(move_piece,0.5)

spawn_figure()



pgzrun.go()


"""
bug in the code: when you move down and hit the bottom, the move down 
function is being called in two different places. if they are at the same time,
there is a problem and the tetris piece disappears. This is why you need a 
"pressing_down" boolean
"""