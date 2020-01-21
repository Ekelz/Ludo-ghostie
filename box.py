#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class Box:

    def __init__(self, master, image_file_path, width, height, curr_index=-1, x=0, y=0, x0=0, y0=0, double=False,
                 init=False):
        super().__init__()
        self.curr_index = curr_index
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.double = double
        self.out = False

        if init:
            self.label_image = self.init_image(image=image_file_path, width=width, height=height, x_coor=self.x0 + 13,
                                               y_coor=self.y0 + 14, master=master)

    def swap(self):
        # self.label_image.pack(in_=master)
        self.label_image.place(x=self.x0 + 13, y=self.y0 + 14)

    @staticmethod
    def init_image(image, width, height, x_coor, y_coor, master=None):
        label_image = tk.Label(master=master, width=width, height=height)
        label_image.img = tk.PhotoImage(file=image)
        label_image.pack(in_=master)
        label_image.place(in_=master, x=x_coor, y=y_coor)
        label_image.config(image=label_image.img)
        return label_image
