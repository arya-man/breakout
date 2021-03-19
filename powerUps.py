from drawable import drawable
import global_vars as gb
import threading
import time
class powerup(drawable):
    def __init__(self,y,x):
        super().__init__(y,x)
    def dpp(self):
        self.Ycor += 2
        # print(self.Ycor,"Afdsf")
        return self

class powerupExpandPaddle(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12301
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        gb.expandtime = gb.time
        setup.slider.updateLength(9)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(7)

class powerupShrinkPaddle(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12302
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        gb.shrinktime = gb.time
        setup.slider.updateLength(5)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(7)

class powerupBallMultiplier(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12303
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)

class powerupFastBall(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12304
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)

class powerupThruball(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12305
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)

class powerupPaddlegrab(powerup):
    def __init__(self,y,x):
        self.powerupNum = 12306
        super().__init__(y,x)
    def startpu(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)
    def endup(self,setup):
        print(setup.slider,"pufile")
        setup.slider.updateLength(9)