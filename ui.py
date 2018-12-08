import datetime
from objects import Player
from objects import Lineup
from objects import position_available
double_dash_line = "=" * 64
dash_line = "-" * 64


def display_menu():
    print(double_dash_line)
    print("{:^64}".format("Chicago Cubs Baseball Team Manager"))
    print()

    game_date()

    print("MENU OPTIONS")
    print("1 - Display Lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")

def menu_selection():
    while True:
        try:
            selection = int(input("Menu Option: "))
            return selection
        except ValueError:
            print("You entered an invalid integer. Please try again")


def display_lineup(lineup):
    header = ("{:<6}{:<20s}{:^10s}{:^10s}{:^10s}{:^10s}".format(" ", "Player", "POS", "AB", "H", "AVG"))
    player = 0
    print(header)
    print(dash_line)
    for i in lineup:
        player += 1
        if player == 10:
            print(dash_line)
            print("Bench:")
        if int(i.get_at_bats()) == 0:
            average = 0.000
        else:
            average = i.get_average()

        print('{:<6}{:<20s}{:^10s}{:^10}{:^10}{:^10.3f}'.format(player, i.get_name(), i.get_position(), i.get_at_bats(), i.get_hits(), average))


def add_player(lineup):
    new_player = Player()
    new_player.set_name(input("Player Name:\t"))

    new_player.set_position(input("Position:\t"))
    while new_player.get_position() is '':
        print("Please choose a valid position")
        new_player.set_position(input("Position:\t"))

    new_player.set_at_bats(int(input("At bats:\t")))
    while new_player.get_at_bats() < 0:
        print("Can't have negative at bats.")
        new_player.set_at_bats(int(input("At bats:\t")))


    new_player.set_hits(int(input("Hits:\t")))
    while new_player.get_hits() > new_player.get_at_bats() or new_player.get_hits() < 0:
        print("Can't have more hits than at bats.")
        new_player.set_hits(int(input("Hits:\t")))

    new_player.set_at_bats(str(new_player.get_at_bats()))
    new_player.set_hits(str(new_player.get_hits()))

    lineup.add_player(new_player, True)
    print(new_player.get_name() + " was added.")


def remove_player(lineup):
    player_number = int(input("What player (by number) would you like to delete:\t"))
    while player_number > lineup.get_len() or player_number < 1:
        print("Select a player number from the lineup.")
        player_number = int(input("What player (by number) would you like to delete:\t"))
    print(lineup.remove_player(player_number) + " was removed from the lineup")


def move_player(lineup):
    player_number1 = int(input("Which player (by number) would you like to move:\t"))
    while player_number1 > lineup.get_len() or player_number1 < 1:
        print("Select a player number from the lineup.")
        player_number1 = int(input("Which player (by number) would you like to move:\t"))

    new_position = int(input("What position would you like to move the player to:\t"))
    while new_position == player_number1 or new_position > lineup.get_len() or new_position < 1:
        print("Select a player number from the lineup.")
        new_position = int(input("What position would you like to move the player to:\t"))

    print(lineup.move_player(player_number1, new_position) + " was moved")


def edit_position(lineup):
    player = int(input("Which players position is changing:\t"))
    while player > lineup.get_len() or player < 1:
        print("Select a player number from the lineup.")
        player = int(input("Which players position is changing:\t"))

    lineup.get_player(player - 1).set_position(input("What is the new position:\t"))
    while lineup.get_player(player - 1).get_position() not in position_available:
        print("Please choose a valid position")
        lineup.get_player(player - 1).set_position(input("What is the new position:\t"))

    print(lineup.get_player(player - 1).get_name() + " position was changed to " + lineup.get_player(player - 1).get_position())
    db.write_players(lineup)


# finish last two menu options
def edit_stats(lineup):
    player = int(input("Select a player to update stats:\t"))
    print("You selected " + lineup.get_player(player - 1).get_name())

    at_bats = int(input("What is the new number of at bats:\t"))
    while at_bats < 0:
        print("Please enter a non negative number of at bats")
        at_bats = int(input("What is the new number of at bats:\t"))

    hits = int(input("What is the new number of hits:\t"))
    while hits > at_bats or hits < 0:
        print("Please enter a number equal to or less than the number of at bats")
        hits = int(input("What is the new number of hits:\t"))

    lineup.get_player(player - 1).set_at_bats(str(at_bats))
    lineup.get_player(player - 1).set_hits(str(hits))

    print("New stats for " + lineup.get_player(player - 1).get_name() + ":\tAB - " + lineup.get_player(player - 1).get_at_bats() +
          "\t H - " + lineup.get_player(player - 1).get_hits())
    db.write_players(lineup)

def game_date():
    valid_date = False
    todays_date = datetime.date.today()
    print("Current Date:\t\t", todays_date)
    user_date = (input("Game Date:\t\t"))
    if user_date == '':
        return

    while not valid_date:
        try:
            game_day = datetime.date(int(user_date[0:4]), int(user_date[5:7]), int(user_date[8:]))
            valid_date = True
        except ValueError:
            print("Enter a valid date.")
            user_date = (input("Game Date:\t\t"))
            if user_date == '':
                return

    days_until = int((game_day - todays_date).days)
    if days_until > 0:
        print("Days until game:\t" + str(days_until))

