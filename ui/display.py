def display_menu(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ').upper()  # makes the quit option case insensitive
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def get_location_info():
    """ Create new Location object from name and email provided by user
     :returns: an Artist created from the name and email. """
    name = input('Enter artist\'s name: ')
    email = input('Enter artist\'s email: ')
    return Artist(name, email)


def display_data():
    pass
