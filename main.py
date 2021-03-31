from ui import display
from ui import objects


def main():
    menu = create_menu()

    while True:
        choice = display.display_menu(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = objects.Menu()
    menu.add_option('1', 'Start New Trip', get_trip_data)
    # menu.add_option('2', 'Save Current Trip', bookmark_trip)
    # menu.add_option('3', 'View Saved Trips', show_frequent_trips)
    # menu.add_option('4', 'Delete Saved Trips', delete_saved_trip)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def get_trip_data():
    start_lat_lon, end_lat_lon = display.get_trip_locs()
    # would grab eta as well once working
    etd_uber = display.get_uber_times(start_lat_lon, end_lat_lon)


def bookmark_trip():
    pass


def show_frequent_trips():
    pass


def delete_saved_trip():
    pass


def quit_program():
    quit_msg = '\nGoodbye!'
    display.message(quit_msg)


if __name__ == '__main__':
    main()
