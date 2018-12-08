import ui #function for each menu selection
import db_2   #Functions to read and write to files
import datetime

def main():
    # Read the file into a list of list and check for file not found
    lineup = db_2.read_players()
    if lineup == None:
        print("The file was not found.")
        return 0
    #Display the menu selection to the user
    ui.display_menu()
    print()
    print("POSITIONS\n" + str(ui.position_available))
    print(ui.double_dash_line)
    #Ask user for initial menu selection to enter the loop
    menu_selection = ui.menu_selection()
    #Loop that goes through the user's menu selection until exit is selected
    while menu_selection != 7:

        if menu_selection == 1:
            ui.display_lineup(lineup)
        elif menu_selection == 2:
            ui.add_player(lineup)
        elif menu_selection == 3:
            ui.remove_player(lineup)
        elif menu_selection == 4:
            ui.move_player(lineup)
        elif menu_selection == 5:
            ui.edit_position(lineup)
        elif menu_selection == 6:
            ui.edit_stats(lineup)
        else:
            print("Please select a valid menu options")
        #ask the user to select another option from the menu
        print()
        menu_selection = int(input("Menu Option: "))




if  __name__ == "__main__":
    main()