class bullet:
    def __init__(self, y, x):
        self.Xcor = x
        self.Ycor = y
        
    def moveup(self):
        self.Ycor -= 1 
    def disappear(self):
        self.Xcor = 1
        self.Ycor = 1       