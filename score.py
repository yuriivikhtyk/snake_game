from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.number = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.number}", move=False, align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
        
        

    def increase(self):
        self.number = self.number + 1
        self.clear()
        self.write(f"Score: {self.number}", move=False, align="center", font=("Arial", 18, "normal"))