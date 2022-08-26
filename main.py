import pgzrun
from tetris import *

#CONSTANTS
WIDTH = 400
HEIGHT = 500
DROP_START = ((WIDTH/2)+1,61)
#flag
game_over = False
game = Tetris(20,10)

# for cell in game.field:
#     print(cell)

def draw():
    screen.fill('white')
    for i in range(game.height): #rows
        for j in range(game.width): #columns
            anchor = (game.x+game.pixel_width * j,game.y+game.pixel_width*i)
            box_lw = (game.pixel_width,game.pixel_width)
            box = Rect(anchor, box_lw)
            screen.draw.rect(box, 'grey')  # Rect((left,top),(width,height))
            # if game.field[i][j]>0:
            #     box = Rect((game.x+game.zoom * j+1,game.y+game.zoom * i +1),(game.zoom-2,game.zoom-1))
            #     screen.draw.filled_rect(box,colors[game.field[i][j]])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j #p stanads for pixel in 4x4 figure square
                if p in game.figure.image():
                    #print('game.figure.x={}'.format(game.figure.x))
                    anchor = (game.x + game.pixel_width * (j+game.figure.x)+1,game.y + game.pixel_width * (i+game.figure.y)+1)
                    #the anchor coordinates is how the piece moves
                    print("anchor={}".format(anchor))
                    box_lw = (game.pixel_width-2,game.pixel_width-2) #-2 so you can see grey lining of tetris board
                    box = Rect(anchor,box_lw)
                    screen.draw.filled_rect(box,colors[game.figure.color])
        game.go_down()


def on_mouse_move(pos):
    pass
    #print('position is {}'.format(pos))

def on_key_down(key):
    if key == key.LEFT:
        game.go_side(-1)
    elif key == key.UP:
        print('^')
    elif key == key.RIGHT:
        game.go_side(1)
    elif key == key.DOWN:
        game.go_down()

def spawn_figure():
    if game.figure is None:
        game.new_figure()

clock.schedule(spawn_figure,3.0)




pgzrun.go()