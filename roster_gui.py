import tkinter as tk
from tkinter import ttk
import db_2

class PlayerRosterFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        self.playerID = tk.IntVar()
        self.firstName = tk.StringVar()
        self.lastName = tk.StringVar()
        self.position = tk.StringVar()
        self.atBats = tk.IntVar()
        self.hits = tk.IntVar()
        self.batAvg = tk.StringVar()

        self.width = 28


        ttk.Label(self, text='Player ID:').grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.playerID).grid(column=1, row=0)
        ttk.Button(self, text='Get Player', command=self.clicked_getPlayer).grid(column=2, row=0)

        ttk.Label(self, text='First Name:').grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.firstName).grid(column=1, row=1)

        ttk.Label(self, text='Last Name:').grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.lastName).grid(column=1, row=2)

        ttk.Label(self, text='Position:').grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.position).grid(column=1, row=3)

        ttk.Label(self, text='At Bats:').grid(column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.atBats).grid(column=1, row=4)

        ttk.Label(self, text='Hits:').grid(column=0, row=5, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.hits).grid(column=1, row=5)

        ttk.Label(self, text='Batting Average:').grid(column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=self.width, textvariable=self.batAvg, state='readonly').grid(column=1, row=6)

        ttk.Button(self, text='Save Changes', command=self.clicked_saveChanges).grid(column=1, row=7, sticky=tk.W)
        ttk.Button(self, text='Cancel', command=self.clicked_cancel).grid(column=1, row=7, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clicked_getPlayer(self):
        temp_ID = self.playerID.get()
        if temp_ID == 0:
            return None
        if temp_ID > roster_lineup.get_len():
            return None
        player = roster_lineup.get_player(temp_ID - 1)
        temp_name = player.get_name()
        space_char = temp_name.find(' ')
        self.firstName.set(temp_name[:space_char])
        self.lastName.set(temp_name[(space_char + 1):])
        self.position.set(player.get_position())
        self.atBats.set(player.get_at_bats())
        self.hits.set(player.get_hits())
        self.batAvg.set(float("{0:.3f}".format(player.get_hits()*1.0 / player.get_at_bats())))

    def clicked_saveChanges(self):
        temp_position = self.position.get()
        temp_atBats = self.atBats.get()
        temp_hits = self.hits.get()
        temp_ID = self.playerID.get()
        db_2.update_player(temp_ID, temp_position, temp_atBats, temp_hits)
        roster_lineup.get_player(temp_ID - 1).set_at_bats(temp_atBats)
        roster_lineup.get_player(temp_ID - 1).set_position(temp_position)
        roster_lineup.get_player(temp_ID - 1).set_hits(temp_hits)
        self.batAvg.set(float("{0:.3f}".format(temp_hits * 1.0 / temp_atBats)))


    def clicked_cancel(self):
        temp_ID = self.playerID.get()
        if temp_ID == 0:
            return None
        if temp_ID > roster_lineup.get_len():
            return None
        player = roster_lineup.get_player(temp_ID - 1)
        temp_name = player.get_name()
        space_char = temp_name.find(' ')
        self.firstName.set(temp_name[:space_char])
        self.lastName.set(temp_name[(space_char + 1):])
        self.position.set(player.get_position())
        self.atBats.set(player.get_at_bats())
        self.batAvg.set(float("{0:.3f}".format(player.get_hits() * 1.0 / player.get_at_bats())))


if __name__ == "__main__":
    roster_lineup = db_2.read_players()
    root = tk.Tk()
    root.title("Player Roster")
    PlayerRosterFrame(root)
    root.mainloop()