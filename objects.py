import db_2
position_available = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF")

class Player:

    def __init__(self, player_name = "PLACEHOLDER", position = '', at_bats = -1, hits = -1):
        self.__name = player_name
        self.__position = position
        self.__at_bats = at_bats
        self.__hits = hits

    def get_average(self):
        try:
            return (int)(self.__hits) / (int)(self. __at_bats)
        except ZeroDivisionError:
            # although there are checks to make sure the user enters valid at bats value
            # if the file contains the error at read time an error would occur
            print("At bats can't be 0. Division by zero error.")
            return None

    def get_name(self):
        return self.__name
    def get_position(self):
        return self.__position
    def get_at_bats(self):
        return self.__at_bats
    def get_hits(self):
        return self.__hits
    def set_name(self, new_name):
        self.__name = new_name
    def set_position(self, position):
        self.__position = position
    def set_at_bats(self, new_value):
        self.__at_bats = new_value
    def set_hits(self, new_value):
        self.__hits = new_value
    def add_game_performance(self, at_bats, hits):
        self.__at_bats += at_bats
        self.__hits += hits
    def print_player(self):
        return (self.get_name() + "," + self.get_position() + "," + str(self.get_at_bats()) + "," + str(self.get_hits()))

#######################################################################################################################

class Lineup:
    def __init__(self):
        self.starters = []
        self.__count = 0

    def add_player(self, new_player, adddb= False):
        self.starters.append(new_player)
        if adddb:
            db_2.add_player(new_player)

    def remove_player(self, value):
        removed_player = self.starters.pop(value - 1)
        db_2.delete_player(value)
        return removed_player.get_name()

    def move_player(self, initial_location, new_location):
        temp_player = self.starters.pop(initial_location - 1)
        self.starters.insert(new_location - 1, temp_player)
        return temp_player.get_name()

    def edit_player(self, player_number, name, position, at_bats, hits):
        new_player = Player(name, position, at_bats, hits)
        self.lineup[player_number] = new_player
        db_2.update_player(player_number, position, at_bats, hits)

    def __iter__(self):
        return self

    def __next__(self):
        temp=self.__count
        self.__count += 1
        try:
            return self.starters[temp]
        except IndexError:
            self.__count = 0
            raise StopIteration

    def get_len(self):
        return len(self.starters)

    def get_player(self, value):
        return self.starters[value]
