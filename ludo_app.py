#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from board import Board
from controller import Engine
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)  # police. to be put in game config class


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("jeu de ludo")
    root.resizable(width=False, height=False)
    root.geometry('1000x750')
    d = Board(root)
    d.pack()
    e = Engine(d)
    root.mainloop()
