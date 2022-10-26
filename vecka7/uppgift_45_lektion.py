import random


class Point:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 3:
            dx, dy, dz = other
            return Point(self.x + dx, self.y+dy, self.z+dz)

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x*other, self.y*other, self.z*other)



def random_point():
    return Point(random.randint(0, 100),
                 random.randint(0, 100),
                 random.randint(0, 100))



if __name__ == '__main__':
    p = random_point()
    print(p)
    p2 = p + (10, 0, 0)
    print(p2)
    p3 = p2 *10
    print(p3)
