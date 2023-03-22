class Motor:
    def __init__(self):
        self.velocity=0.5

    def set_speed(self, speed):
        self.velocity = speed

    def speed_up(self):
        self.velocity = 2 * self.velocity

    def slow_down(self):
        self.velocity = 0.5 * self.velocity

