from ui import display
from ui.objects import Menu
# from artwork import Artwork

# artwork_store = ArtworkStore()


def main():
    menu = create_menu()

    while True:
        choice = display.display_menu(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Artist', add_artist)
    # menu.add_option('2', 'See All Artist\'s Artwork', show_all_artist_artwork)
    # menu.add_option('3', 'See Artist\'s Available Artwork', show_artist_available_artwork)
    # menu.add_option('4', 'Add Artist\'s Artwork', add_artwork)
    # menu.add_option('5', 'Delete Artwork', delete_artwork)
    # menu.add_option('6', 'Change Artwork Availability Status', change_availability)
    # menu.add_option('Q', 'Quit', quit_program)

    return menu


def add_artist():
    new_artist = display.get_location_info()
    try:
        new_artist.insert_artist()
    except:
        print('This artist is already in the database.')


if __name__ == '__main__':
    main()
