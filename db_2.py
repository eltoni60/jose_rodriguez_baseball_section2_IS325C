import sqlite3
from contextlib import closing
import objects

#conn = sqlite3.connect("player_roster.db")
#c = conn.cursor()
#query = '''SELECT * FROM PLAYER WHERE playerID = ?'''
FILENAME = "player_roster.db"

print()

def read_players():
        lineup = objects.Lineup()
        conn = sqlite3.connect(FILENAME)
        with closing(conn.cursor()) as c:
            query = '''SELECT * FROM PLAYER ORDER BY playerID ASC'''
            c.execute(query)
            temp_lineup = c.fetchall()
        for row in temp_lineup:
            player = objects.Player(row[2] + ' ' + row[3], row[4], row[5], row[6])
            lineup.add_player(player)
        return lineup

def add_player(player, batOrder = 99):
    space_char_loc = player.get_name().find(' ')
    conn = sqlite3.connect(FILENAME)
    with closing(conn.cursor()) as c:
        query = '''INSERT INTO PLAYER(batOrder, firstname, lastname, position, atbats, hits) 
                    VALUES (?, ?, ?, ?, ?, ?)'''
        c.execute(query, (batOrder,player.get_name()[:space_char_loc], player.get_name()[(space_char_loc + 1):], player.get_position(), player.get_at_bats(), player.get_hits()))
        conn.commit()


def delete_player(playerId):
    conn = sqlite3.connect(FILENAME)
    with closing(conn.cursor()) as c:
        query = ''' DELETE FROM Player WHERE playerId = ?'''
        c.execute(query, (playerId,))
        conn.commit()

#this updates the players batting order based on their average
def update_batOrder():
    conn = sqlite3.connect(FILENAME)
    with closing(conn.cursor()) as c:
        query_1 = '''create table bats as select playerID from player order by player.hits * 1.0 / player.atBats desc;'''
        query_2 = '''update player set batorder = (select rowid from bats where playerID = player.playerid) where playerId in (select playerID from bats);'''
        query_3 = '''drop table bats;'''
        c.execute(query_1, query_2, query_3)
        conn.commit()

def update_player(playerID, position, atBats, hits):
    conn = sqlite3.connect(FILENAME)
    with closing(conn.cursor()) as c:
        query = '''UPDATE Player SET position = ?, atBats= ?, hits= ? WHERE playerID = ?'''
        c.execute(query, (position, atBats, hits, playerID))
        conn.commit()

def get_player(id):
    conn = sqlite3.connect(FILENAME)
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM PLAYER WHERE playerID=?'''
        c.execute(query, (id,))
        player = c.fetchall()
    return player


def write_players(lineup):
    return None
#     with open(FILENAME, "w") as file:
#         for player in lineup:
#             file.write(player.print_player() + "\n")
