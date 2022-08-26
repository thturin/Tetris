import random

colors = ['red','blue','green','purple','orange','pink','yellow']

class Figure:
    x=0
    y=0
    figures = [
        [[1,5,9,13],[4,5,6,7]], #rod
        [[4,5,9,10],[2,5,6,9]], #z shape
        [[6,7,9,10],[1,5,6,10]], # z shape
        [[1,2,5,9],[0,4,5,6],[1,5,8,9],[4,5,6,10]], #l-shape
        [[1,2,6,10],[5,6,7,9],[2,6,10,11],[3,5,6,7]], #l-shape
        [[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,9]], #t-shape
        [[1,2,5,6]] #square
    ]

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.type = random.randint(0,len(self.figures)-1) #choose a random shape
        self.color = random.randint(0,len(colors)-1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation+1) % len(self.figures[self.type]) #easy way of traversing through the list

class Tetris:
    level = 2
    score = 0
    state = 'start'
    field = []
    height = 0
    width = 0
    x = 100 #(x,y) is the top left anchor of the tetris board
    y = 60
    pixel_width = 20
    figure = None

    def __init__(self, height,width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        #create the tetris 2-d Array
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
                #print(new_line)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3,0)

    def go_down(self):
        self.figure.y +=1

    def go_side(self,dir):
        self.figure.x +=dir
