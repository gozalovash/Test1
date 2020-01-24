class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, lh, rl):
        self.lh = lh
        self.rl = rl

    def get_area(self):
        return abs((self.rl.x - self.lh.x) * (self.rl.y - self.lh.y))


if __name__ == "__main__":

    def get_min(a, b):
        if a < b:
            return a
        else:
            return b


    def get_max(a, b):
        if a > b:
            return a
        else:
            return b

    # points
    lh1 = Point(5, 13)  # left-high point
    rl1 = Point(10, 4)  # right- low point
    lh2 = Point(8, 7)
    rl2 = Point(15, 3)
    rect1 = Rectangle(lh1, rl1)  # rectangles using given points
    rect2 = Rectangle(lh2, rl2)

    # calculating....

    sum_area = rect1.get_area() + rect2.get_area()  # not taking intersecting into account

    # intersection area  is x range of intersection multiplied by y range

    area_intersection = abs(
        (get_min(rect1.rl.x, rect2.rl.x) - get_max(rect1.lh.x, rect2.lh.x))  # x range
        *
        (get_min(rect1.lh.y, rect2.lh.y) - get_max(rect1.rl.y, rect2.rl.y)))  # y range

    total_area = sum_area - area_intersection

    print(area_intersection)

    print(total_area)
