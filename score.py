from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.number = 0
        with open("high_score.txt", "r") as file_high_score:
            self.high_score = int(file_high_score.read())
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.number},  High Score: {self.high_score}", move=False, align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
        
        

    def increase(self):
        self.number = self.number + 1
        self.clear()
        self.write(f"Score: {self.number},  High Score: {self.high_score}", move=False, align="center", font=("Arial", 18, "normal"))

    
    def reset(self):
        global file
        if self.number > self.high_score:
            self.high_score = self.number
            with open("high_score.txt", "w") as file_high_score:
                file_high_score.write(str(self.high_score))


        self.number = 0