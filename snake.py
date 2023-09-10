from turtle import Turtle, Screen

MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        for i in range(3):
            self.new_segment((-(i*20)-150, 20))
            self.segments[i].goto(-(i*20)-150, 20)
        
        self.segments[0].color("yellow")

    def new_segment(self, position):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(position)
        self.segments.append(new_seg)


    def general_move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_SPEED)

    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)


    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.__init__()

