# Alien Invasion Game Chapter 12
# 11.2.2018

class Settings(): 
    """A clas to store settings for Alien Invasion."""
    
    def __init__(self):
        """Inititalize the games settings."""
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 20, 20, 20
        self.bullets_allowed = 4
        

