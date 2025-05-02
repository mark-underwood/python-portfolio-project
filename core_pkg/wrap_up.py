"""Conclusions to the game."""

def wrap_up(player):
    """conclude the game"""

    if player.stat['hp'] <= 0:
        # bad endings here
        print("\n GAME OVER\n") # generic game over message
    else:
        # good endings here
        if player.name.lower() == 'you':
            print("\nYou woke up ...\n\n ... and remembered who you are.\n")
        else:
            print(f"\n{player.name} met ol' Trusty the horse",
                    "and rode off into the sunset.\n")
