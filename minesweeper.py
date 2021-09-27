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
                if y == 0 and x == 0:
                    NW_tile = None
                    N_tile = None
                    NE_tile = None
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'
                if y == 0 and x == 0:
                    NW_tile = None
                    N_tile = None
                    NE_tile = None
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'
                if y == 0 and x == 0:
                    NW_tile = None
                    N_tile = None
                    NE_tile = None
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'
                if y == 0 and x == 0:
                    NW_tile = None
                    N_tile = None
                    NE_tile = None
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'

                if y == 0 and (x != 0 or x != (width-1)):
                    NW_tile = None
                    N_tile = None
                    NE_tile = None
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'
                if y == (height-1) and (x != 0 or x != (width-1)):
                    NW_tile = f'ID{x-1}{y-1}'
                    N_tile = f'ID{x}{y-1}'
                    NE_tile = f'ID{x+1}{y-1}'
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = None
                    S_tile = None
                    SW_tile = None
                    W_tile = f'ID{x-1}{y}'
                if x == 0 and (y != 0 or y != (width-1)):
                    NW_tile = None
                    N_tile = f'ID{x}{y-1}'
                    NE_tile = f'ID{x+1}{y-1}'
                    E_tile = f'ID{x+1}{y}'
                    SE_tile = f'ID{x+1}{y+1}'
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = None
                    W_tile = None
                if x == (width-1) and (y != 0 or y != (height-1)):
                    NW_tile = f'ID{x-1}{y-1}'
                    N_tile = f'ID{x}{y-1}'
                    NE_tile = None
                    E_tile = None
                    SE_tile = None
                    S_tile = f'ID{x}{y+1}'
                    SW_tile = f'ID{x-1}{y+1}'
                    W_tile = f'ID{x-1}{y}'


                if x < 1: W_tile, NW_tile, SW_tile = None, None, None
                else: W_tile = f'ID{x-1}{y}'

                if y > (height-2): S_tile, SW_tile, SE_tile = None, None, None
                else: S_tile = f'ID{x}{y+1}'

                if x > (width-2): E_tile = None
                else: E_tile = f'ID{x+1}{y}'

                if (y > 0 and x > 0) and (y < (height-1) and x < (width-1)):
                    NE_tile = 
                    SE_tile = 
                    SW_tile = 
                    NW_tile = 

                self.tiles[f'ID{x}{y}']={
                    "N_tile": N_tile,
                    "NE_tile": NE_tile,
                    "E_tile": E_tile,
                    "SE_tile": SE_tile,
                    "S_tile": S_tile,
                    "SW_tile": SW_tile,
                    "W_tile": W_tile,
                    "NW_tile": NW_tile,
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
        print(self.tiles[f'ID{x}{y}'])
        ...

def main():
    window = tk.Tk()
    window.title('Mine Sweeper')
    minesweeper = Game(window)

    window.mainloop()

if __name__ == "__main__":
    main()
