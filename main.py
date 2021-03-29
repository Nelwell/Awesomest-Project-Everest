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
    # menu.add_option('2', 'View Saved Trips', show_all_artist_artwork)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def get_trip_data():
    start_lat_lon, end_lat_lon = display.get_trip_locs()
    etd_uber, eta_uber = display.get_uber_times(start_lat_lon, end_lat_lon)
    # try:
    #     new_trip_data.insert_artist()
    # except:
    #     print('This trip is already in the database.')


def quit_program():
    display.message('\nGoodbye!')


if __name__ == '__main__':
    main()
