import bricks
import subprocess
import display
import slider
import ball

class setup:
    def __init__(self):
        
        self.display1 = display.display() 
        self.ball1 = ball.ball(34,61)
        self.slider = slider.slider(35,57)
     

    def createlvl1(self):
    

        self.layout = []
        self.layout.append(bricks.bricklvl1(10,1))
        self.layout.append(bricks.bricklvl1(10,6))
        self.layout.append(bricks.bricklvl1(10,11))
        self.layout.append(bricks.bricklvl1(10,16))
        self.layout.append(bricks.bricklvl1(10,21))
        self.layout.append(bricks.bricklvl1(10,26))
        self.layout.append(bricks.bricklvl1(10,31))
        self.layout.append(bricks.bricklvl1(10,36))
        self.layout.append(bricks.bricklvl1(10,41))
        self.layout.append(bricks.bricklvl1(10,46))
        self.layout.append(bricks.bricklvl1(10,51))
        self.layout.append(bricks.bricklvl1(10,56))
        self.layout.append(bricks.bricklvl1(10,61))
        self.layout.append(bricks.bricklvl1(10,66))
        self.layout.append(bricks.bricklvl1(10,71))
        self.layout.append(bricks.bricklvl1(10,76))
        self.layout.append(bricks.bricklvl1(10,81))
        self.layout.append(bricks.bricklvl1(10,86))
        self.layout.append(bricks.bricklvl1(10,91))
        self.layout.append(bricks.bricklvl1(10,96))
        self.layout.append(bricks.bricklvl1(10,101))
        self.layout.append(bricks.bricklvl1(10,106))
        self.layout.append(bricks.bricklvl1(10,111))
        self.layout.append(bricks.bricklvl1(10,116))
        self.layout.append(bricks.bricklvl2(12,1))
        self.layout.append(bricks.bricklvl2(12,6))
        self.layout.append(bricks.bricklvl2(12,11))
        self.layout.append(bricks.bricklvl2(12,16))
        self.layout.append(bricks.bricklvl2(12,21))
        self.layout.append(bricks.bricklvl2(12,26))
        self.layout.append(bricks.bricklvl2(12,31))
        self.layout.append(bricks.bricklvl2(12,36))
        self.layout.append(bricks.bricklvl2(12,41))
        self.layout.append(bricks.bricklvl2(12,46))
        self.layout.append(bricks.bricklvl2(12,51))
        self.layout.append(bricks.bricklvl2(12,56))
        self.layout.append(bricks.bricklvl2(12,61))
        self.layout.append(bricks.bricklvl2(12,66))
        self.layout.append(bricks.bricklvl2(12,71))
        self.layout.append(bricks.bricklvl2(12,76))
        self.layout.append(bricks.bricklvl2(12,81))
        self.layout.append(bricks.bricklvl2(12,86))
        self.layout.append(bricks.bricklvl2(12,91))
        self.layout.append(bricks.bricklvl2(12,96))
        self.layout.append(bricks.bricklvl2(12,101))
        self.layout.append(bricks.bricklvl2(12,106))
        self.layout.append(bricks.bricklvl2(12,111))
        self.layout.append(bricks.bricklvl2(12,116))
        self.layout.append(bricks.bricklvl3(14,1))
        self.layout.append(bricks.bricklvl3(14,6))
        self.layout.append(bricks.bricklvl3(14,11))
        self.layout.append(bricks.bricklvl3(14,16))
        self.layout.append(bricks.bricklvl3(14,21))
        self.layout.append(bricks.bricklvl3(14,26))
        self.layout.append(bricks.bricklvl3(14,31))
        self.layout.append(bricks.bricklvl3(14,36))
        self.layout.append(bricks.bricklvl3(14,41))
        self.layout.append(bricks.bricklvl3(14,46))
        self.layout.append(bricks.bricklvl3(14,51))
        self.layout.append(bricks.bricklvl3(14,56))
        self.layout.append(bricks.bricklvl3(14,61))
        self.layout.append(bricks.bricklvl3(14,66))
        self.layout.append(bricks.bricklvl3(14,71))
        self.layout.append(bricks.bricklvl3(14,76))
        self.layout.append(bricks.bricklvl3(14,81))
        self.layout.append(bricks.bricklvl3(14,86))
        self.layout.append(bricks.bricklvl3(14,91))
        self.layout.append(bricks.bricklvl3(14,96))
        self.layout.append(bricks.brickExp(13,46))
        self.layout.append(bricks.brickExp(13,51))
        self.layout.append(bricks.brickExp(13,56))
        self.layout.append(bricks.brickExp(13,61))
        self.layout.append(bricks.brickExp(13,66))
        self.layout.append(bricks.brickExp(13,71))
        self.layout.append(bricks.brickExp(13,76))
        self.layout.append(bricks.brickExp(13,81))
        self.layout.append(bricks.brickExp(13,86))
        self.layout.append(bricks.brickExp(13,91))
        self.layout.append(bricks.brickExp(13,96))
        self.layout.append(bricks.bricklvl3(14,101))
        self.layout.append(bricks.bricklvl3(14,106))
        self.layout.append(bricks.bricklvl3(14,111))
        self.layout.append(bricks.bricklvl3(14,116))
        self.layout.append(bricks.brickfixed(9,1))
        self.layout.append(bricks.brickfixed(9,21))
        self.layout.append(bricks.brickfixed(9,41))
        self.layout.append(bricks.brickfixed(9,61))
        self.layout.append(bricks.brickfixed(9,81))
        self.layout.append(bricks.brickfixed(9,101))
        self.layout.append(bricks.brickfixed(15,6))
        self.layout.append(bricks.brickfixed(15,16))
        self.layout.append(bricks.brickfixed(15,26))
        self.layout.append(bricks.brickfixed(15,36))
        self.layout.append(bricks.brickfixed(15,46))
        self.layout.append(bricks.brickfixed(15,56))
        self.layout.append(bricks.brickfixed(15,66))
        self.layout.append(bricks.brickfixed(15,76))
        self.layout.append(bricks.brickfixed(15,86))
        self.layout.append(bricks.brickfixed(15,96))
        self.layout.append(bricks.brickfixed(15,106))
        self.layout.append(bricks.brickfixed(15,116))
        self.layout.append(bricks.brickExp(16,46))
        self.layout.append(bricks.brickExp(16,51))
        self.layout.append(bricks.brickExp(16,56))
        self.layout.append(bricks.brickExp(16,61))
        self.layout.append(bricks.brickExp(16,66))
        self.layout.append(bricks.brickExp(16,71))
        self.layout.append(bricks.brickExp(16,76))
        self.layout.append(bricks.brickExp(16,81))
        self.layout.append(bricks.brickExp(16,86))
        self.layout.append(bricks.brickExp(16,91))
        self.layout.append(bricks.brickExp(16,96))

        self.display1.createlvl(self.layout)
        self.display1.updateSlider(self.slider)
        self.display1.updateBall(self.display1 ,self.ball1,0,0)
       
        