# Alien Invasion Game Chapter 12
# 11.2.2018

class Settings(): 
    """A class to store settings for Alien Invasion."""
    
    def __init__(self):
        """Inititalize the game's static settings."""
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # How quicky the game speeds up.
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
                
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
                              
        # fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1
        
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 20, 20, 20
        self.bullets_allowed = 4
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
