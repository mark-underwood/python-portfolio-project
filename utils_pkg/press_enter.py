"""Wait for player to press enter to continue."""

from getpass import getpass # for hiding user input

def press_enter_to_continue():
    """Silent pause before continuing."""
    # pylint does not complain 'unused variable' if starts with underscore
    _dump_this = getpass(" [ press enter to continue ]\n")
