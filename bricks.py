from drawable import drawable
class brick(drawable):
    def __init__(self, y, x):
        super().__init__(y,x)


class bricklvl1(brick):
    def __init__(self, y, x):
        self.isRainbow = False
        self.lvl = 0
        super().__init__(y,x)



class bricklvl2(brick):
    def __init__(self, y, x):
        self.isRainbow = False
        self.lvl = 1
        super().__init__(y,x)


class bricklvl3(brick):
    def __init__(self, y, x):
        self.isRainbow = False
        self.lvl = 2
        super().__init__(y,x)


class brickfixed(brick):
    def __init__(self,y,x):
        self.isRainbow = False
        self.lvl = 4
        super().__init__(y,x)

class brickExp(brick):
    def __init__(self,y,x):
        self.isRainbow = False
        self.lvl = 69
        super().__init__(y,x)

class brickRainbow(brick):
    def __init__(self,y,x):
        self.isRainbow = True
        self.lvl = 111
        super().__init__(y,x)
