class Void:
    def __init__(self, display, num, coor):
        self.display = display
        self.num = num
        self.type = "void"
        self.x = coor[0]
        self.y = coor[1]
    def check(self, player):
        return True if player[0] >= self.x and player[1] <= self.y else False