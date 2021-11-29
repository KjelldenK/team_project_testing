import arcade
from game import constants

class Player_Test_Ship(arcade.Sprite):
    def __init__(self, image_file, scale, bullet_list, time_between_firing):
        super().__init__(image_file, scale)

        self.time_since_last_firing = 0.0 
        self.time_between_firing = time_between_firing

        self.bullet_list = bullet_list
        self.ship_speed = 150
        self.right_movment = False
        self.left_movment = False
        self.shooting = False
        
    def on_update(self, delta_time: 1 / 60):
        """ Update this sprite. """
        if self.left < 0:
            self.left = 1

        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH - 1

        if self.right_movment == True:
            self.center_x += self.ship_speed * delta_time

        if self.left_movment == True:
            self.center_x -= self.ship_speed * delta_time


        self.time_since_last_firing += delta_time
        if self.shooting == True:
            if self.time_since_last_firing >= self.time_between_firing:
                
                # reset bullet timer
                self.time_since_last_firing = 0

                # Fire bullet add it to the list
                bullet = arcade.Sprite("project\images\\testing_bullet.png", scale= 0.1)
                bullet.center_x = self.center_x
                bullet.bottom  = self.top
                bullet.change_y = 15
                self.bullet_list.append(bullet)

        

    def action(self, ship_action, status):
        if ship_action == "right":
            self.right_movment = status

        if ship_action == "left":
            self.left_movment = status

        if ship_action == "shoot":
            self.shooting = status
        
