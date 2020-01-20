#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from board import Board
from controller import Engine
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)  # police. to be put in game config class


if __name__ == "__main__":
    #global cx, cy
    root = tk.Tk()
    root.wm_title("jeu de ludo")
    root.resizable(width=False, height=False)
    root.geometry('1000x750')
    d = Board(root)
    d.pack()
    e = Engine(d)
    root.mainloop()
    # app = LudoApp()
    # app.mainloop()

# class LudoApp(tk.Tk):
#
#     def __init__(self):
#         super().__init__()
#
#         self.geometry('1000x750')
#
#         tk.Tk.wm_title(self, "Test Jeu de ludo")
#
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for F in (StartPage, Board, Engine):  # <- add the newly created page here
#
#             frame = F(container, self)
#
#             self.frames[F] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame(StartPage)
#
#     def show_frame(self, cont):
#         frame = self.frames[cont]  # cont = controller
#         frame.tkraise()  # raise the container "cont" to the top
#
#
# # useful code to create a new page
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button = ttk.Button(self, text="visit page 1",
#                             command=lambda: controller.show_frame(Engine))
#         button.pack()
#
#         # button1 = ttk.Button(self, text="visit engine",
#         #                     command=lambda: controller.show_frame(Engine))
#         # button1.pack()