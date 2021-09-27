import tkinter as tk
import random
import time
from tkinter.constants import SUNKEN
from itertools import filterfalse, product
from pprint import pprint

class Game:

    states = {
        'default': 0,
        'clicked': 1,
        'flagged': 2,
        'unknown': 3,
    }

    def __init__(self, game_window):
        self.game_window = game_window
        # self.game_window.geometry("400x400")
        self.CreateMenu()
        self.CreateHeader()

        self.CreateMinefield()
        ...

    def CreateMenu(self):
        menu_bar = tk.Menu(self.game_window)
        file_dd = tk.Menu(menu_bar, tearoff=0)
        file_dd.add_command(label='New Game', command=self.donothing)
        help_dd = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='File', menu=file_dd)
        menu_bar.add_cascade(label='Help', menu=help_dd)
        self.game_window.config(menu=menu_bar)

    def CreateHeader(self):
        ...

    def CreateMinefield(self, width=10, height=10, mines = 15):
        self.tiles = {}
        self.locations = list(product(range(width), repeat=2))
        self.mine_locs = random.sample(self.locations, k=mines)
        self.spaces = []
        for x in range(width):
            for y in range(height):
                self.tiles[f'ID-{x}-{y}']={
                    'adj_tiles':{
                        "N_tile": f'ID-{x}-{y-1}',
                        "NE_tile": f'ID-{x+1}-{y-1}',
                        "E_tile": f'ID-{x+1}-{y}',
                        "SE_tile": f'ID-{x+1}-{y+1}',
                        "S_tile": f'ID-{x}-{y+1}',
                        "SW_tile": f'ID-{x-1}-{y+1}',
                        "W_tile": f'ID-{x-1}-{y}',
                        "NW_tile": f'ID-{x-1}-{y-1}',
                    },
                    'value': 0,
                    'pressed': False,
                }

                self.mine_field = tk.Frame(
                    master=self.game_window,
                    relief=tk.RAISED,
                    borderwidth=0
                    )

                self.mine_field.grid(row=y, column=x)
                self.space = tk.Button(master=self.mine_field, text=f'{x}-{y}',width=1, height=1, command=lambda x_pos=x, y_pos=y:self.donothing(x_pos,y_pos, width, height))
                self.space.grid()

        for x in range(width):
            for y in range(height):
                if (x,y) in self.mine_locs:
                    self.tiles[f'ID-{x}-{y}']["value"] = '*'
                    for tiles in self.tiles[f'ID-{x}-{y}']['adj_tiles'].keys():
                        try:
                            self.tiles[self.tiles[f'ID-{x}-{y}']['adj_tiles'][tiles]]['value'] += 1
                        except: pass

    def donothing(self,x,y, width, height):
        tile_id = f"ID-{x}-{y}"
        print(tile_id)
        self.space = tk.Button(text=f'{self.tiles[tile_id]["value"]}', relief=SUNKEN, width=1, height=1)
        self.space.grid(row=y,column=x)
        if self.tiles[tile_id]["value"] == 0 and self.tiles[tile_id]["pressed"] == False:
            self.tiles[tile_id]["pressed"] = True
            adj_tiles = [[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1],[x-1,y]]
            for tile in adj_tiles:
                try:
                    self.donothing(tile[0],tile[1], width, height)
                except:
                    continue


def main():
    window = tk.Tk()
    window.title('Mine Sweeper')
    minesweeper = Game(window)

    window.mainloop()

if __name__ == "__main__":
    main()
