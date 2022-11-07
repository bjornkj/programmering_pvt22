class PhysicsObject:
    pos: tuple[float, float]
    vel: tuple[float, float]

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel


class Player(PhysicsObject):
    def jump(self):
        self.vel = self.vel[0], -80

    def go_left(self):
        self.vel = -10, self.vel[1]

    def go_right(self):
        self.vel = 10, self.vel[1]


class PhysicsSim:
    objects: list[PhysicsObject]
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.objects = []
        self.width = width
        self.height = height

    def update(self, dt: float):
        for po in self.objects:
            po.vel = po.vel[0], po.vel[1] + 9.82 * dt
            po.pos = po.pos[0] + po.vel[0] * dt, po.pos[1] + po.vel[1] * dt

            if po.pos[1] > self.height - 10:
                po.pos = po.pos[0], 768 - 10
