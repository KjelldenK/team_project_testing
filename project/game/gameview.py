import arcade
from game.player_text_ship import Player_Test_Ship
from game import constants
class GameView(arcade.View):
    def __init__(self, ship):
        super().__init__()
        
        self.left = False
        self.right = False
        self.player = None
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.menu_Background = "project\images\menu_background.jpg"

        self.set_up(ship)
        


    def set_up(self, ship):
        self.bullet_list = arcade.SpriteList()

        self.player_list = arcade.SpriteList()
        if ship == 0:
            player = Player_Test_Ship("project\images\\test_ship.png", scale= 0.5 , bullet_list= self.bullet_list, time_between_firing= 2.0)
            player.center_x = 450
            player.center_y = 700
            self.player_list.append(player)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture(self.menu_Background))

        self.player_list.draw()

    def on_update(self, delta_time):
        # Call update on all sprites
        self.player_list.on_update(delta_time)
        self.player_list.update()


    def on_key_press(self, key, _modifiers):
        for ship in self.player_list:
            if key == arcade.key.LEFT:
                ship.movment("left", True)

            if key == arcade.key.RIGHT:
                ship.movment("right", True)

        

    def on_key_release(self, key, _modifiers):
        # checks to see if a key was released so it can stop moving the player
        for ship in self.player_list:

            if key == arcade.key.LEFT:
                ship.movment("left", False)

            if key == arcade.key.RIGHT:
                ship.movment("right", False)
