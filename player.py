#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from box import Box
from game_config import RED, BLUE, YELLOW, GREEN
from tkinter import ttk


class Player:

    def __init__(self, master, image_file_path, color, width, height, turn=False):  # roll,
        self.color = color
        self.master = master

        # Initialisation of the lists of coordinates of the game pieces
        if color == RED:
            self.pawns = self.init_pawns(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=100, ref_y=100, size=25)
        if color == BLUE:
            self.pawns = self.init_pawns(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=100, ref_y=550, size=25)
        if color == YELLOW:
            self.pawns = self.init_pawns(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=550, ref_y=550, size=25)
        if color == GREEN:
            self.pawns = self.init_pawns(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=550, ref_y=100, size=25)

        # Initialisation of the lists of coordinates of the home boxes
        if color == RED:
            self.homes = self.init_homes(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=100, ref_y=100)
        if color == BLUE:
            self.homes = self.init_homes(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=100, ref_y=550)
        if color == YELLOW:
            self.homes = self.init_homes(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=550, ref_y=550)
        if color == GREEN:
            self.homes = self.init_homes(image_file_path=image_file_path, width=width, height=height, master=master,
                                         ref_x=550, ref_y=100)

        # Initialisation of the lists of coordinates of the white boxes (the outer boxes)
        self.white_boxes = self.init_list_white_boxes(image_file_path=image_file_path, width=width, height=height,
                                                      master=master)

        # Initialisation of the path (the lists represent the "path" on the board for each game piece according to its color
        if color == RED:
            self.box_path = self.init_list_box_path(image_file_path=image_file_path, width=width, height=height, master=master,
                                                 corresp_index=1)
        if color == BLUE:
            self.box_path = self.init_list_box_path(image_file_path=image_file_path, width=width, height=height, master=master,
                                                 corresp_index=40)
        if color == YELLOW:
            self.box_path = self.init_list_box_path(image_file_path=image_file_path, width=width, height=height, master=master,
                                                 corresp_index=27)
        if color == GREEN:
            self.box_path = self.init_list_box_path(image_file_path=image_file_path, width=width, height=height, master=master,
                                                 corresp_index=14)

        self.turn = turn
        #self.roll = roll  # a list
        self.num_saved_pawns = 0
        self.rolls = [0, 0, 0]
        self.win = False

    def init_pawns(self, image_file_path, width, height, master, ref_x, ref_y, size):
        pawns = []
        for i in range(4):
            pawns.append(Box(image_file_path=image_file_path, width=width, height=height, master=master, init=True))
        for i in range(2):
            pawns[i].x0 = (ref_x + (100 * i))
            pawns[i].y0 = ref_y
            pawns[i].x = pawns[i].x0 + size
            pawns[i].y = pawns[i].y0 + size
            pawns[i].swap(x_coor=pawns[i].x, y_coor=pawns[i].y, master=self.master)
        for i in range(2, 4):
            pawns[i].x0 = ref_x + (100 * (i - 2))
            pawns[i].y0 = ref_y + 100
            pawns[i].x = pawns[i].x0 + size
            pawns[i].y = pawns[i].y0 + size
            pawns[i].swap(x_coor=pawns[i].x, y_coor=pawns[i].y, master=self.master)
        return pawns

    @staticmethod
    def init_homes(image_file_path, width, height, master, ref_x, ref_y):
        homes = []
        for i in range(4):
            homes.append(Box(image_file_path=image_file_path, width=width, height=height, master=master))
        for i in range(2):
            homes[i].x = (ref_x + (100 * i))
            homes[i].y = ref_y
        for i in range(2, 4):
            homes[i].x = ref_x + (100 * (i - 2))
            homes[i].y = ref_y + 100
        return homes

    @staticmethod
    def init_list_white_boxes(image_file_path, width, height, master):
        white_boxes = []
        for i in range(52):
            white_boxes.append(Box(image_file_path=image_file_path, width=width, height=height, master=master))
        for i in range(6):
            white_boxes[i].x = 0 + (50 * i)
            white_boxes[i].y = 300
        for i in range(6, 12):
            white_boxes[i].x = 300
            white_boxes[i].y = 250 - (50 * (i - 6))
    
        white_boxes[12].x = 350
        white_boxes[12].y = 0
    
        for i in range(13, 19):
            white_boxes[i].x = 400
            white_boxes[i].y = 0 + (50 * (i - 13))
        for i in range(19, 25):
            white_boxes[i].x = 450 + (50 * (i - 19))
            white_boxes[i].y = 300
    
        white_boxes[25].x = 700
        white_boxes[25].y = 350
    
        for i in range(26, 32):
            white_boxes[i].x = 700 - (50 * (i - 26))
            white_boxes[i].y = 400
        for i in range(32, 38):
            white_boxes[i].x = 400
            white_boxes[i].y = 450 + (50 * (i - 32))
    
        white_boxes[38].x = 350
        white_boxes[38].y = 700
    
        for i in range(39, 45):
            white_boxes[i].x = 300
            white_boxes[i].y = 700 - (50 * (i - 39))
        for i in range(45, 51):
            white_boxes[i].x = 250 - (50 * (i - 45))
            white_boxes[i].y = 400
    
        white_boxes[51].x = 0
        white_boxes[51].y = 350
    
        return white_boxes

    def init_list_box_path(self, image_file_path, width, height, master, corresp_index):
        path = []
        for i in range(57):
            path.append(Box(image_file_path=image_file_path, width=width, height=height, master=master))
        if corresp_index == 1:
            for i in range(52):
                if corresp_index > 51:
                    corresp_index = 0
                path[i].x = self.white_boxes[corresp_index].x
                path[i].y = self.white_boxes[corresp_index].y
                corresp_index = corresp_index + 1
    
            corresp_index2 = 50
            for i in range(7):
                path[corresp_index2].x = 0 + (50 * i)
                path[corresp_index2].y = 350
                corresp_index2 = corresp_index2 + 1
    
        if corresp_index == 14:
            for i in range(52):
                if corresp_index > 51:
                    corresp_index = 0
                path[i].x = self.white_boxes[corresp_index].x
                path[i].y = self.white_boxes[corresp_index].y
                corresp_index = corresp_index + 1
    
            corresp_index2 = 50
            for i in range(7):
                path[corresp_index2].x = 350
                path[corresp_index2].y = 0 + (50 * i)
                corresp_index2 = corresp_index2 + 1
    
        if corresp_index == 27:
            for i in range(52):
                if corresp_index > 51:
                    corresp_index = 0
                path[i].x = self.white_boxes[corresp_index].x
                path[i].y = self.white_boxes[corresp_index].y
                corresp_index = corresp_index + 1
    
            corresp_index2 = 50
            for i in range(7):
                path[corresp_index2].x = 700 - (50 * i)
                path[corresp_index2].y = 350
                corresp_index2 = corresp_index2 + 1

        if corresp_index == 40:
            for i in range(52):
                if corresp_index > 51:
                    corresp_index = 0
                path[i].x = self.white_boxes[corresp_index].x
                path[i].y = self.white_boxes[corresp_index].y
                corresp_index = corresp_index + 1
    
            corresp_index2 = 50
            for i in range(7):
                path[corresp_index2].x = 350
                path[corresp_index2].y = 700 - (50 * i)
                corresp_index2 = corresp_index2 + 1

        return path

