import tkinter as tk
import random
import time

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
        information = ['mines', '']
        # for item in information:

        # info_frame = tk.Frame(
        #     master=self.game_window,

        # )
        ...

    def CreateMinefield(self, width=10, height=10, mines = 20):
        self.tiles = {}
        self.mines = mines
        for x in range(width):
            for y in range(height):
                if y == 0: top_tile = None
                else: top_tile = f'ID{x}{y-1}'
                if y == (height-1): bottom_tile = None
                else: bottom_tile = f'ID{x}{y+1}'
                if x == 0: left_tile = None
                else: left_tile = f'ID{x-1}{y}'
                if x == (width-1): right_tile = None
                else: right_tile = f'ID{x+1}{y}'
                self.tiles[f'ID{x}{y}']={
                    "top_tile": top_tile,
                    "right_tile": right_tile,
                    "bottom_tile": bottom_tile,
                    "left_tile": left_tile,
                    "mine_location": False
                }
                self.mine_field = tk.Frame(
                    master=self.game_window,
                    relief=tk.RAISED,
                    borderwidth=0
                    )
                self.mine_field.grid(row=y, column=x)
                self.button = tk.Button(master=self.mine_field, text=f'{x}{y}', command=lambda x_pos=x, y_pos=y:self.donothing(x_pos,y_pos))
                self.button.pack()
        ...

    def donothing(self,x,y):
        print(f'Tile ID is {x},{y}')
        ...

def main():
    window = tk.Tk()
    window.title('Mine Sweeper')
    minesweeper = Game(window)

    window.mainloop()

if __name__ == "__main__":
    main()
