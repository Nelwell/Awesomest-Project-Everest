import ui.objects
from api import location


def display_menu(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('What to do? ').upper()  # makes the quit option case insensitive
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print """
    print(msg)


def get_trip_info():
    """ Create new Location object from name and email provided by user
     :returns: an Artist created from the name and email. """
    start_st_address, start_city, start_state = '', '', ''
    # end_st_address, end_city, end_state = '', '', ''
    while len(start_st_address) == 0:
        start_st_address = input('Enter the departure street address: ').title().strip()

    while len(start_city) == 0:
        start_city = input('Enter departure the city: ').title().strip()

    while len(start_state) != 2 or not start_state.isalpha():
        start_state = input('Enter the 2-letter departure state abbreviation: ').upper().strip()
    #
    # while len(end_st_address) == 0:
    #     end_st_address = input('Enter the destination street address: ').title().strip()
    #
    # while len(end_city) == 0:
    #     end_city = input('Enter destination the city: ').title().strip()
    #
    # while len(end_state) != 2 or not end_state.isalpha():
    #     end_state = input('Enter the 2-letter destination state abbreviation: ').upper().strip()

    start_address = f'{start_st_address}, {start_city}, {start_state}'
    print(start_address)
    # end_address = f'{end_st_address}, {end_city}, {end_state}'
    start_lat, start_lon = location.convert_to_lat_lon(start_address)  # pass start address to lat/lon conversion function
    # end_lat, end_lon = location.convert_to_lat_lon(end_address)  # same for end address
    start_location = ui.objects.Location(start_lat, start_lon)
    # end_location = ui.objects.Location(end_lat, end_lon)

    return start_location


def display_data():
    pass
