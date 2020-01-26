#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from board import Board
from controller import Engine
from tkinter import ttk
from tkinter import Menu

LARGE_FONT = ("Verdana", 12)  # police. to be put in game config class


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("jeu de ludo")
    root.resizable(width=False, height=False)
    root.geometry('1025x760')
    d = Board(root)
    d.pack()
    e = Engine(d)
    
    menubar = Menu(root) 
    root.config(menu=menubar) 
    menufichier = Menu(menubar,tearoff=0) 
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_command(label="Nouvelle partie", underline=1, command=e.new)
    menufichier.add_command(label="Sauvegarder", underline=1, command=e.save)
    menufichier.add_command(label="Charger", underline=1, command=e.load)
    menufichier.add_separator()
    menufichier.add_command(label="Quitter", underline=1, command=exit)
    root.mainloop()
