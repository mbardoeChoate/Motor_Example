class Motor:
    def __init__(self):
        self.speed=0.5

    def set_speed(self, speed):
        self.speed = speed

    def speed_up(self):
        self.speed = 2 * self.speed

    def slow_down(self):
        self.speed = 0.5 * self.speed

