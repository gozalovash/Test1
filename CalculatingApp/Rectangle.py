class Rectangle:
    def __init__(self, lh, rl):
        self.lh = lh
        self.rl = rl

    def get_area(self):
        return abs((self.rl.x - self.lh.x) * (self.rl.y - self.lh.y))



