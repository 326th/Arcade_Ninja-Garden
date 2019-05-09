import arcade
def draw(lives,win):
    if win == False:
        if lives > 0:
            pic = arcade.Sprite('images/GUI/lives.png',scale = 0.75)
            for bomb in range(lives-1):
                pic.set_position(816 -40 - (30*bomb), 600-40)
                pic.draw()
        else:
            pic = arcade.Sprite('images/GUI/Gameover.png',scale = 1.1)
            pic.set_position(408, 300)
            pic.draw()
                                
    
