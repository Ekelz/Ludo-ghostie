#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from game_config import *

# from tkinter import ttk

LARGE_FONT = ("Verdana", 24, "bold")  # police. to be put in game config class


class Board(tk.Canvas):

    def __init__(self, root, *args, **kwargs):  # , parent
        tk.Canvas.__init__(self, root, *args, **kwargs)
        # super().__init__(parent)
        self.configure(width=BOARD_WIDTH, height=BOARD_HEIGHT)

        # red
        self.red_box = tk.PhotoImage(file=RED_BOX)
        self.red_side = tk.PhotoImage(file=RED_SIDE)
        self.red_start = tk.PhotoImage(file=RED_START)

        # blue
        self.blue_box = tk.PhotoImage(file=BLUE_BOX)
        self.blue_side = tk.PhotoImage(file=BLUE_SIDE)
        self.blue_start = tk.PhotoImage(file=BLUE_START)

        # yellow
        self.yellow_box = tk.PhotoImage(file=YELLOW_BOX)
        self.yellow_side = tk.PhotoImage(file=YELLOW_SIDE)
        self.yellow_start = tk.PhotoImage(file=YELLOW_START)

        # green
        self.green_box = tk.PhotoImage(file=GREEN_BOX)
        self.green_side = tk.PhotoImage(file=GREEN_SIDE)
        self.green_start = tk.PhotoImage(file=GREEN_START)

        # others
        self.center = tk.PhotoImage(file=CENTER)
        self.head = tk.PhotoImage(file=HEAD)
        self.head1 = tk.PhotoImage(file=HEAD1)
        self.head2 = tk.PhotoImage(file=HEAD2)
        self.head3 = tk.PhotoImage(file=HEAD3)
        self.tail = tk.PhotoImage(file=TAIL)
        self.tail1 = tk.PhotoImage(file=TAIL1)
        self.tail2 = tk.PhotoImage(file=TAIL2)
        self.tail3 = tk.PhotoImage(file=TAIL3)
        self.white_box = tk.PhotoImage(file=WHITE_BOX)

        self.draw_board()

    def set_image(self, image, width, height, x_coor, y_coor):
        label_image = tk.Label(self, image=image, width=width, height=height)
        label_image.image = image
        label_image.place(x=x_coor, y=y_coor)
        return

    def draw_white_boxes(self, image, width, height, x_start, y_start, direction):
        coord_y = 0  # v
        while coord_y != 300:
            coord_x = 0
            while coord_x != 150:
                if direction == "vertical":
                    self.set_image(image=image, width=width, height=height, x_coor=x_start + coord_x,
                                   y_coor=y_start + coord_y)
                    coord_x = coord_x + 50
                if direction == 'horizontal':
                    self.set_image(image=image, width=width, height=height, x_coor=x_start + coord_y,
                                   y_coor=y_start + coord_x)
                    coord_x = coord_x + 50
            coord_y = coord_y + 50
        return

    def draw_colored_boxes(self, image, width, height, x_start, y_start, direction):
        coord = 0
        while coord != 250:
            if direction == "vertical":
                self.set_image(image=image, width=width, height=height, x_coor=x_start, y_coor=y_start + coord)
                coord = coord + 50
            if direction == "horizontal":
                self.set_image(image=image, width=width, height=height, x_coor=x_start + coord, y_coor=y_start)
                coord = coord + 50

    def draw_board(self):
        # placing board images
        self.set_image(image=self.blue_side, width=300, height=300, x_coor=-2, y_coor=448)
        self.set_image(image=self.green_side, width=296, height=296, x_coor=450, y_coor=0)
        self.set_image(image=self.red_side, width=298, height=298, x_coor=-1, y_coor=-1)
        self.set_image(image=self.yellow_side, width=294, height=294, x_coor=450, y_coor=450)
        self.set_image(image=self.center, width=150, height=150, x_coor=298, y_coor=298)

        # drawing white boxes
        self.draw_white_boxes(image=self.white_box, width=46, height=46, x_start=300, y_start=0, direction="vertical")
        self.draw_white_boxes(image=self.white_box, width=46, height=46, x_start=300, y_start=450, direction="vertical")
        self.draw_white_boxes(image=self.white_box, width=46, height=46, x_start=0, y_start=300, direction="horizontal")
        self.draw_white_boxes(image=self.white_box, width=46, height=46, x_start=450, y_start=300, direction="horizontal")

        # drawing colored boxes
        self.draw_colored_boxes(image=self.green_box, width=46, height=46, x_start=350, y_start=50, direction="vertical")
        self.draw_colored_boxes(image=self.yellow_box, width=46, height=46, x_start=450, y_start=350, direction="horizontal")
        self.draw_colored_boxes(image=self.blue_box, width=46, height=46, x_start=350, y_start=450, direction="vertical")
        self.draw_colored_boxes(image=self.red_box, width=46, height=46, x_start=50, y_start=350, direction="horizontal")

        # placing starting point
        self.set_image(image=self.green_start, width=46, height=46, x_coor=400, y_coor=50)
        self.set_image(image=self.yellow_start, width=46, height=46, x_coor=650, y_coor=400)
        self.set_image(image=self.red_start, width=46, height=46, x_coor=50, y_coor=300)
        self.set_image(image=self.blue_start, width=46, height=46, x_coor=300, y_coor=650)

        # placing arrows
        self.set_image(image=self.head, width=46, height=46, x_coor=250, y_coor=400)
        self.set_image(image=self.head1, width=46, height=46, x_coor=400, y_coor=450)
        self.set_image(image=self.head2, width=46, height=46, x_coor=450, y_coor=300)
        self.set_image(image=self.head3, width=46, height=46, x_coor=300, y_coor=250)
        self.set_image(image=self.tail, width=46, height=46, x_coor=300, y_coor=450)
        self.set_image(image=self.tail1, width=46, height=46, x_coor=450, y_coor=400)
        self.set_image(image=self.tail2, width=46, height=46, x_coor=400, y_coor=250)
        self.set_image(image=self.tail3, width=46, height=46, x_coor=250, y_coor=300)
        return

if __name__ == "__main__":
    root = tk.Tk()
    c = Board(root, width=BOARD_WIDTH, height=BOARD_HEIGHT)
    c.pack(side="top", fill="both", expand=True)
    root.mainloop()
