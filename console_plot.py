from colorama import Fore, Back, Style
from math import *

class Plot:
    def __init__(self, expresssion, H=26, W=50):
        self.H = H
        self.W = W
        self.expresssion = "-" + expresssion
        self.plot = []
        self.init_plot()
        self.print_plot()


    def print_plot(self):
        for row in self.plot:
            for col in row:
                print(col[1] + col[0], end="")
                print(Style.RESET_ALL, end="")
            print()        

    def init_plot(self):
        self.plot = [[[" ", ""] for _ in range(self.W)] for _ in range(self.H)]

        for i in range(self.H):
            if i == 0:
                self.plot[i][self.W//2] = ["^", Back.GREEN]
            else:
                self.plot[i][self.W//2] = ["#", Back.GREEN]

        for i in range(self.W):
            if i == self.W - 1:
                self.plot[self.H//2][i] = [">", Back.GREEN]
            else:
                self.plot[self.H//2][i] = ["=", Back.GREEN]

        for x in range(-self.W//2, self.W//2):
            try:
                res = eval(self.expresssion)
                res = res if (res - int(res) < 0.5) else res + 1
                self.plot[int(res) - self.H//2][x + self.W//2] = ["$", Fore.RED]
            except TypeError as te:
                pass
            except IndexError as e:
                pass

plot = Plot("2*(x+30)**0.5", W=130, H=50)
