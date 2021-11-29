class Selection_Attack_Ship:
    
    def __init__(self):
        self._sprit = "project\images\Galaga_ship_attack.png"
        self._speed = 200
        self._attack_speed = 0.1
        self._defence = 3

    def get_sprite(self):
        return self._sprit

    def get_speed(self):
        return self._speed

    def get_attack_speed(self):
        return self._attack_speed

    def get_defence(self):
        return self._defence