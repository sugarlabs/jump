import olpcgames

# Class name must match 'class' property in activity/activity.info:
class JumpActivity(olpcgames.PyGameActivity):
    """An example of using a Pygame game as a Sugar activity."""
    
    game_name = 'Jump'        # game_name must match name of your Pygame module
    game_title = 'Jump'
    game_size = (1200,825)