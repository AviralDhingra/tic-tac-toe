from tkinter import *

from ttc import ttc

if __name__ == "__main__":
    window = Tk()
    window.title("Tic-Tac-Toe Bot - Aviral Dhingra")
    window.config(bg="#141414")
    window.geometry("470x500")
    window.maxsize(470, 500)
    window.minsize(470, 500)
    ttc(window)
    window.mainloop()
