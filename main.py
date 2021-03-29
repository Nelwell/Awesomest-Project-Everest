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
    new_trip_data = display.get_trip_info()
    try:
        new_trip_data.insert_artist()
    except:
        print('This artist is already in the database.')


def quit_program():
    display.message('\nThanks for checking out the store!')


if __name__ == '__main__':
    main()
