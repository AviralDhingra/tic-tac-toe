from tkinter import *

from ttc import ttc

if __name__ == "__main__":
    window = Tk()
    window.title("AI Tic-Tac-Toe")
    window.config(bg="#141414")
    window.geometry("470x500")
    # window.maxsize(450, 500)
    # window.minsize(450, 500)
    ttc(window)
    window.mainloop()
