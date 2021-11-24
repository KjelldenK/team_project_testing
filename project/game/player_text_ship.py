import arcade
from game import constants

class Player_Test_Ship(arcade.Sprite):
    def __init__(self, image_file, scale, bullet_list, time_between_firing):
        super().__init__(image_file, scale)

        self.time_since_last_firing = time_between_firing
        self.bullet_list = bullet_list
        self.right_movment = False
        self.left_movment = False

        
    def on_update(self, delta_time: 1 / 60):
        """ Update this sprite. """
        if self.left < 0:
            self.left = 1
        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH - 1

        if self.right_movment == True:
            self.center_x += 150 * delta_time

        if self.left_movment == True:
            self.center_x -= 150 * delta_time

    def movment(self, direction, status):
        if direction == "right":
            self.right_movment = status

        if direction == "left":
            self.left_movment = status
        
""" 
        # Track time since we last fired
        self.time_since_last_firing += delta_time

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.LEFT:
            self.left = True

        if key == arcade.key.RIGHT:
            self.right = True

    def on_key_release(self, key, _modifiers):
        # checks to see if a key was released so it can stop moving the player
        if key == arcade.key.LEFT:
            self.left = False

        if key == arcade.key.RIGHT:
            self.right = False """