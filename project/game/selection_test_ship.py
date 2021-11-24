
class Selection_Test_Ship:
    def __init__(self):
        self._sprit = "project\images\\test_ship.png"
        self._speed = 150
        self._attack_speed = 0.2
        self._defence = 5

    def get_sprite(self):
        return self._sprit

    def get_speed(self):
        return self._speed

    def get_attack_speed(self):
        return self._attack_speed

    def get_defence(self):
        return self._defence