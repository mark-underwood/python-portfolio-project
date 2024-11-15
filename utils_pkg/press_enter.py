""" press enter to continue """

from getpass import getpass # for hiding user input

def press_enter_to_continue():
    """ silent pause before continuing """
    # pylint does not complain 'unused variable' if starts with underscore
    _dump_this = getpass(" [ press enter to continue ]\n")
    print('_____________________________')
