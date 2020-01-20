#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import ttk
from player import Player
from board import Board
from game_config import *


class Engine:

    cx = None
    cy = None
    player_turn = RED
    turn = True
    rolls_list = []
    num_rolls = 0
    dice = 0
    dice1 = 0
    dice2 = 0
    rolls_index = 0


    def __init__(self, canvas):
        # super().__init__()
        self.canvas = canvas

        self.red_player = Player(master=canvas, image_file_path=RED_PAWN, color=RED, width=PAWN_WIDTH,
                                 height=PAWN_HEIGHT, turn=True)
        self.blue_player = Player(master=canvas, image_file_path=BLUE_PAWN, color=BLUE, width=PAWN_WIDTH,
                                  height=PAWN_HEIGHT)
        self.yellow_player = Player(master=canvas, image_file_path=YELLOW_PAWN, color=YELLOW, width=PAWN_WIDTH,
                                    height=PAWN_HEIGHT)
        self.green_player = Player(master=canvas, image_file_path=GREEN_PAWN, color=GREEN, width=PAWN_WIDTH,
                                   height=PAWN_HEIGHT)

        self.canvas.bind_all("<Button-1>", self.left_click)

        roll_button = tk.Button(self.canvas, text="ROLL", relief="raised", font=LARGE_FONT, command=self.rolls)
        roll_button.pack(in_=self.canvas)
        roll_button.place(x=800, y=120)

        self.display_turn()

    def left_click(self, event):
        Engine.cx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        Engine.cy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        print("#########left_click######")
        print("clicked at", Engine.cx, Engine.cy)

        self.game(cx=Engine.cx, cy=Engine.cy)  # The game is on each time we make a left click

    def set_label(self, text, font_color, font, x_coor, y_coor, master=None):
        label = tk.Label(master, text=text, fg=font_color, font=font)
        label.pack()  # in_=master
        label.place(x=x_coor, y=y_coor)
        return label

    def next_player(self, player):
        print("__entering next_player function___")
        print("Before, turn__: ", Engine.player_turn)
        if player.color == RED:
            Engine.player_turn = BLUE
            print("After, turn__: ", Engine.player_turn)
            self.clean()
        if player.color == BLUE:
            Engine.player_turn = YELLOW
            print("After, turn__: ", Engine.player_turn)
            self.clean()
        if player.color == YELLOW:
            Engine.player_turn = GREEN
            print("After, turn__: ", Engine.player_turn)
            self.clean()
        if player.color == GREEN:
            Engine.player_turn = RED
            print("After, turn__: ", Engine.player_turn)
            self.clean()

    # Team turn handlers
    def display_turn(self):
        if self.player_turn == RED:
            self.label1 = self.set_label(text=" Red player turn ", font_color="Black", font=LARGE_FONT,
                                         x_coor=770, y_coor=50)
        if self.player_turn == BLUE:
            self.label1 = self.set_label(text=" Blue player turn ", font_color="Black",
                                         font=LARGE_FONT, x_coor=770, y_coor=50)
        if self.player_turn == YELLOW:
            self.label1 = self.set_label(text=" Yellow player turn ", font_color="Black",
                                         font=LARGE_FONT, x_coor=770, y_coor=50)
        if self.player_turn == GREEN:
            self.label1 = self.set_label(text=" Green player turn ", font_color="Black",
                                         font=LARGE_FONT, x_coor=770, y_coor=50)

    def rolls(self):
        if Engine.turn:
            # print("turn: ", Engine.turn)

            Engine.num_rolls = Engine.num_rolls + 1
            # print("Number of rolls: ", Engine.num_rolls)

            if Engine.num_rolls == 1:
                # print("i'm in")
                Engine.dice = random.randint(1, 6)
                self.label2 = self.set_label(master=self.canvas, text=Engine.dice, font_color="Black",
                                             font=LARGE_FONT, x_coor=800, y_coor=200)
                # print("dice:", Engine.dice)
                Engine.rolls_list.append(Engine.dice)
                if Engine.dice != 6:
                    Engine.num_rolls = 0
                    Engine.turn = False
                    # print(Engine.turn)
                    print("Next player turn")
            print("num_rolls: ", Engine.num_rolls)

            if Engine.num_rolls == 2:
                if Engine.dice == 6:
                    Engine.dice1 = random.randint(1, 6)
                    # print("dice1: ", Engine.dice1)
                    self.label3 = self.set_label(master=self.canvas, text=Engine.dice1, font_color="Black",
                                                 font=LARGE_FONT, x_coor=800, y_coor=250)
                    # print("dice1: ", Engine.dice1)
                    Engine.rolls_list.append(Engine.dice1)
                    if Engine.dice1 != 6:
                        Engine.num_rolls = 0
                        Engine.turn = False
                        # print("turn1: ", Engine.turn)
                        # print("Next player turn")

            if Engine.num_rolls == 3:
                if Engine.dice1 == 6:
                    Engine.dice2 = random.randint(1, 6)
                    print("dice2: ", Engine.dice2)
                    self.label4 = self.set_label(master=self.canvas, text=Engine.dice2, font_color="Black",
                                                 font=LARGE_FONT, x_coor=800, y_coor=300)
                    # print("dice2:", Engine.dice2)
                    Engine.rolls_list.append(Engine.dice2)
                    Engine.turn = False
                    print("Next player turn")
                    num_rolls = 0
        print("rolls from rolls' function: ", Engine.rolls_list)

    def check_move(self, player):  # Check if the player can make a move
        print("##############check_move#############")
        a = all(roll == 6 for roll in Engine.rolls_list)
        # print("check dices: ", a)
        if all(roll==6 for roll in Engine.rolls_list) == True: # check if he rolled 6 3 times
            # player.turn = False
            return False

        win = True
        if player.num_saved_pawns != 4:
            win = False

        if (win == False) and (Engine.rolls_list[0] != 6):
            for i in range(len(player.pawns)):
                print("In check_move: ", player.pawns[i])
                if player.pawns[i].curr_index != -1:
                    print("The player can move his avalaible pawns.")
                    return True
                print("The players pawns are all at home. He cannot move")
                return False

        if win == True:
            print("the {}_player won the game.".format(player.color))
            # self.match_ended = True
            return False

    def kill(self, player, bb, opponent1, opponent2, opponent3):
        print("Entering kill_function")
        # check if the game piece is not on a starting point
        if player.box_path[bb].x0 != player.white_boxes[1].x and player.box_path[bb].y0 != player.white_boxes[1].y:
            if player.box_path[bb].x0 != player.white_boxes[14].x and player.box_path[bb].y0 != player.white_boxes[14].y:
                if player.box_path[bb].x0 != player.white_boxes[27].x and player.box_path[bb].y0 != player.white_boxes[27].y:
                    if player.box_path[bb].x0 != player.white_boxes[40].x and player.box_path[bb].y0 != player.white_boxes[40].y:

                        # if the game piece of another color and its on the same block and it is not a double, a
                        # kill is made
                        for i in range(len(opponent1.pawns)):
                            if opponent1.pawns[i].x0 == player.pawns[bb].x:
                                if opponent1.pawns[i].y0 == player.pawns[bb].y:
                                    if not opponent1.pawns[i].double:
                                        opponent1.pawns[i].x0 = opponent1.homes[i].x
                                        opponent1.pawns[i].y0 = opponent1.homes[i].y
                                        opponent1.pawns[i].x = opponent1.homes[i].x + 25
                                        opponent1.pawns[i].y = opponent1.homes[i].y + 25
                                        opponent1.pawns[i].num = -1
                                        opponent1.pawns[i].swap(x_coor=opponent1.pawns[i].x,
                                                                y_coor=opponent1.pawns[i].y,
                                                                master=self.canvas)
                                        print("kill made")
                                        break

                        for i in range(len(opponent2.pawns)):
                            if opponent2.pawns[i].x0 == player.pawns[bb].x:
                                if opponent2.pawns[i].y0 == player.pawns[bb].y:
                                    if not opponent2.pawns[i].double:
                                        opponent2.pawns[i].x0 = opponent2.homes[i].x
                                        opponent2.pawns[i].y0 = opponent2.homes[i].y
                                        opponent2.pawns[i].x = opponent2.homes[i].x + 25
                                        opponent2.pawns[i].y = opponent2.homes[i].y + 25
                                        opponent2.pawns[i].num = -1
                                        opponent2.pawns[i].swap(x_coor=opponent2.pawns[i].x,
                                                                y_coor=opponent2.pawns[i].y,
                                                                master=self.canvas)
                                        print("kill made")
                                        break

                        for i in range(len(opponent3.pawns)):
                            if opponent3.pawns[i].x0 == player.pawns[bb].x:
                                if opponent3.pawns[i].y0 == player.pawns[bb].y:
                                    if not opponent3.pawns[i].double:
                                        opponent3.pawns[i].x0 = opponent1.homes[i].x
                                        opponent3.pawns[i].y0 = opponent1.homes[i].y
                                        opponent3.pawns[i].x = opponent1.homes[i].x + 25
                                        opponent3.pawns[i].y = opponent1.homes[i].y + 25
                                        opponent3.pawns[i].num = -1
                                        opponent3.pawns[i].swap(x_coor=opponent1.pawns[i].x,
                                                                y_coor=opponent1.pawns[i].y,
                                                                master=self.canvas)
                                        print("kill made")
                                        break
        print("Exiting kill_function")

    @staticmethod
    def double_check(player):
        print("__entering double check function___")
        for i in range(len(player.pawns)):
            player.pawns[i].double = False

        for j in range(len(player.pawns)):
            for k in range(len(player.pawns)):
                if player.pawns[j].curr_index == player.pawns[k].curr_index:
                    if j != k:
                        player.pawns[j].double = True
                        player.pawns[k].double = True
        print("__exiting double check function___")

    def clean(self):  # Reset the class and instance's  attributes
        print("____Entering clean_funtion ______")
        print("Before cleaning: ",Engine.num_rolls, Engine.rolls_index, Engine.rolls_list, Engine.turn)
        Engine.num_rolls = 0
        Engine.rolls_index = 0
        Engine.rolls_list = []
        Engine.turn = True
        try:
            self.label2.config(text="")
        except AttributeError:
            pass
        try:
            self.label3.config(text="")
        except AttributeError:
            pass
        try:
            self.label4.config(text="")
        except AttributeError:
            pass
        print("After cleaning: ", Engine.num_rolls, Engine.rolls_index, Engine.rolls_list, Engine.turn)
        print("Cleaned")
        self.display_turn()

    # def move_to_start(self, player, cx, cy, i):
    #     print("ENTERING move_to_start_function")
    #     if ((cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13)):  # Check if click is made on a pawn
    #         if ((cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14)):
    #             if ((player.pawns[i].x0 == player.homes[i].x) and (player.pawns[i].y0 == player.homes[i].y)):
    #                 print("A click was made on a {} pawn and it is in his home.".format(player.color))
    #
    #                 if Engine.rolls_list[Engine.rolls_index] == 6:
    #                     player.pawns[i].x0 = player.box_path[0].x
    #                     player.pawns[i].y0 = player.box_path[0].y
    #                     player.pawns[i].x = player.box_path[0].x + 25
    #                     player.pawns[i].y = player.box_path[0].y + 25
    #                     player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
    #                     print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
    #                     player.pawns[i].swap(x_coor=player.pawns[i].x, y_coor=player.pawns[i].y,
    #                                          master=self.canvas)
    #                     Engine.rolls_index = Engine.rolls_index + 1
    #                     print("FROM move_to_start_function:", Engine.rolls_index)
    #
    #                     a = True
    #                     while a:
    #                         if Engine.rolls_index > len(Engine.rolls_list) - 1:
    #                             self.next_player(player)
    #                         else:
    #                             a = False
    #     print("EXITING move_to_start_function")

    # def move_when_out(self, player, opponent1, opponent2, opponent3, cx, cy, out_x0, out_y0, i):
    #     print("ENTERING move_when_out_function")
    #     print("player's color: ", player.color)
    #     if player.color == RED:
    #         print("In move_when_out_function with color: ", player.color)
    #         print("cx: ", cx)
    #         print("cy: ", cy)
    #         print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i), [player.pawns[i].x0, player.pawns[i].x])
    #         print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i), [player.pawns[i].y0, player.pawns[i].y])
    #         if (cx > player.pawns[i].x0) and (cx < player.pawns[i].x):
    #             if (cy > player.pawns[i].y0) and (cy < player.pawns[i].y):
    #                 if (player.pawns[i].x0 > out_x0) or (player.pawns[i].y0 > out_y0):
    #                     print("A click was made on a {} pawn and it is outside.".format(player.color))
    #                     print("Engine.rolls_index: ", Engine.rolls_index)
    #                     track_index = player.pawns[i].curr_index + Engine.rolls_list[Engine.rolls_index]
    #                     print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
    #                     print("track_index: ", track_index)
    #
    #                     if track_index < 56:
    #                         self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
    #                                   opponent3=opponent3)
    #                         player.pawns[i].x0 = player.box_path[0].x
    #                         player.pawns[i].y0 = player.box_path[0].y
    #                         player.pawns[i].x = player.box_path[0].x + 25
    #                         player.pawns[i].y = player.box_path[0].y + 25
    #                         player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
    #                         print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
    #                         player.pawns[i].swap(x_coor=player.pawns[i].x, y_coor=player.pawns[i].y,
    #                                              master=self.canvas)
    #
    #                         self.double_check(player=player)
    #                         Engine.rolls_index = Engine.rolls_index + 1
    #
    #                     if track_index == 56:
    #                         player.pawns.remove(player.pawns[i])
    #                         player.num_saved_pawns = player.num_saved_pawns + 1
    #                         self.display_turn()
    #
    #                     a = True
    #                     while a:
    #                         if track_index > 56:
    #                             print("Player cannot move, track_index out of range.")
    #                             self.next_player(player)
    #                             # self.display_turn()
    #                         else:
    #                             a = False
    #
    #     if player.color == BLUE:
    #         print("In move_when_out_function with color: ", player.color)
    #         print("cx: ", cx)
    #         print("cy: ", cy)
    #         print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i), [player.pawns[i].x0, player.pawns[i].x])
    #         print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i), [player.pawns[i].y0, player.pawns[i].y])
    #         if (cx > player.pawns[i].x0) and (cx < player.pawns[i].x):
    #             if (cy > player.pawns[i].y0) and (cy < player.pawns[i].y):
    #                 if (player.pawns[i].x0 > out_x0) or (player.pawns[i].y0 < out_y0):
    #                     print("A click was made on a {} pawn and it is outside.".format(player.color))
    #                     print("Engine.rolls_index: ", Engine.rolls_index)
    #                     track_index = player.pawns[i].curr_index + player.rolls[Engine.rolls_index]
    #                     print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
    #                     print("track_index: ", track_index)
    #
    #                     if track_index < 56:
    #                         self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
    #                                   opponent3=opponent3)
    #                         player.pawns[i].x0 = player.box_path[0].x
    #                         player.pawns[i].y0 = player.box_path[0].y
    #                         player.pawns[i].x = player.box_path[0].x + 25
    #                         player.pawns[i].y = player.box_path[0].y + 25
    #                         player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
    #                         print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
    #                         player.pawns[i].swap(x_coor=player.pawns[i].x, y_coor=player.pawns[i].y,
    #                                              master=self.canvas)
    #
    #                         self.double_check(player=player)
    #                         Engine.rolls_index = Engine.rolls_index + 1
    #
    #                     if track_index == 56:
    #                         player.pawns.remove(player.pawns[i])
    #                         player.num_saved_pawns = player.num_saved_pawns + 1
    #                         self.display_turn()
    #
    #                     a = True
    #                     while a:
    #                         if track_index > 56:
    #                             print("Player cannot move, track_index out of range.")
    #                             self.next_player(player)
    #                             # self.display_turn()
    #                         else:
    #                             a = False
    #
    #     if player.color == YELLOW or player.color == GREEN:
    #         print("In move_when_out_function with color: ", player.color)
    #         print("cx: ", cx)
    #         print("cy: ", cy)
    #         print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i,i), [player.pawns[i].x0, player.pawns[i].x])
    #         print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i), [player.pawns[i].y0, player.pawns[i].y])
    #         if (cx > player.pawns[i].x0) and (cx < player.pawns[i].x):
    #             if (cy > player.pawns[i].y0) and (cy < player.pawns[i].y):
    #                 if (player.pawns[i].x0 < out_x0) or (player.pawns[i].y0 < out_y0):
    #                     print("A click was made on a {} pawn and it is outside.".format(player.color))
    #                     print("Engine.rolls_index: ", Engine.rolls_index)
    #                     track_index = player.pawns[i].curr_index + player.rolls[Engine.rolls_index]
    #                     print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
    #                     print("track_index: ", track_index)
    #
    #                     if track_index < 56:
    #                         self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
    #                                   opponent3=opponent3)
    #                         player.pawns[i].x0 = player.box_path[0].x
    #                         player.pawns[i].y0 = player.box_path[0].y
    #                         player.pawns[i].x = player.box_path[0].x + 25
    #                         player.pawns[i].y = player.box_path[0].y + 25
    #                         player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
    #                         print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
    #                         player.pawns[i].swap(x_coor=player.pawns[i].x, y_coor=player.pawns[i].y,
    #                                              master=self.canvas)
    #
    #                         self.double_check(player=player)
    #                         Engine.rolls_index = Engine.rolls_index + 1
    #
    #                     if track_index == 56:
    #                         player.pawns.remove(player.pawns[i])
    #                         player.num_saved_pawns = player.num_saved_pawns + 1
    #                         self.display_turn()
    #
    #                     a = True
    #                     while a:
    #                         if track_index > 56:
    #                             print("Player cannot move, track_index out of range.")
    #                             self.next_player(player)
    #                             # self.display_turn()
    #                         else:
    #                             a = False

    def player_move(self, player, opponent1, opponent2, opponent3, cx, cy, out_x0, out_y0):
        print("#######################{}_player_move_function############".format(player.color))
        print(cx)
        print(cy)
        print("[x0, x]: ", [player.pawns[0].x0, player.pawns[0].x])
        print("[y0, y]: ", [player.pawns[0].y0, player.pawns[0].y])
        print([player.pawns[0].x0, player.homes[0].x], [player.pawns[0].y0, player.homes[0].y])
        rolls = Engine.rolls_list
        print("rolls from player_game: ", rolls)

        if Engine.player_turn == player.color:  # It's this player's turn (according to it's color)
            for i in range(len(player.pawns)):  # Check if click is made on a pawn
                print("ENTERING move_to_start_function")
                if ((cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13)):  # Check if click is made on a pawn
                    print("on start 1")
                    if ((cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14)):
                        print("on start 2")
                        if ((player.pawns[i].x0 == player.homes[i].x) and (player.pawns[i].y0 == player.homes[i].y)):
                            print("A click was made on a {} pawn and it is in his home.".format(player.color))

                            if Engine.rolls_list[Engine.rolls_index] == 6:
                                player.pawns[i].x0 = player.box_path[0].x
                                player.pawns[i].y0 = player.box_path[0].y
                                player.pawns[i].x = player.box_path[0].x + 25
                                player.pawns[i].y = player.box_path[0].y + 25
                                player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
                                print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                player.pawns[i].swap(x_coor=player.pawns[i].x, y_coor=player.pawns[i].y,
                                                     master=self.canvas)
                                Engine.rolls_index = Engine.rolls_index + 1
                                print("FROM move_to_start_function:", Engine.rolls_index)

                                if Engine.rolls_index > len(Engine.rolls_list) - 1:
                                    self.next_player(player)
                                break

                # print("red: ", player.pawns[i].x0, player.pawns[i].y0)
                # print("red: ", player.pawns[i].x, player.pawns[i].y)

                print("ENTERING move_when_out_function")
                print("player's color: ", player.color)
                if player.color == RED:
                    print("In move_when_out_function with color: ", player.color)
                    print("cx: ", cx)
                    print("cy: ", cy)
                    print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i), [player.pawns[i].x0, player.pawns[i].x])
                    print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i), [player.pawns[i].y0, player.pawns[i].y])
                    if (cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13):
                        print("out 1")
                        if (cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14):
                            print("out 2")
                            if (player.pawns[i].x0 > out_x0) or (player.pawns[i].y0 > out_y0):
                                print("out 3")
                                print("A click was made on a {} pawn and it is outside.".format(player.color))
                                print("Engine.rolls_index: ", Engine.rolls_index)
                                track_index = player.pawns[i].curr_index + Engine.rolls_list[Engine.rolls_index]
                                print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
                                print("track_index: ", track_index)

                                if track_index < 56:
                                    print("track_index<56")
                                    self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
                                              opponent3=opponent3)
                                    player.pawns[i].x0 = player.box_path[track_index].x
                                    player.pawns[i].y0 = player.box_path[track_index].y
                                    player.pawns[i].x = player.box_path[track_index].x + 25
                                    player.pawns[i].y = player.box_path[track_index].y + 25
                                    player.pawns[i].curr_index = track_index  # updating the pawn position on board
                                    print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                    player.pawns[i].swap(x_coor=player.pawns[i].x0, y_coor=player.pawns[i].y0,
                                                         master=self.canvas)

                                    self.double_check(player=player)
                                    Engine.rolls_index = Engine.rolls_index + 1

                                    print(" in player_move_function: ", Engine.rolls_index)

                                if track_index == 56:
                                    player.pawns.remove(player.pawns[i])
                                    player.num_saved_pawns = player.num_saved_pawns + 1
                                    self.next_player(player)
                                    self.display_turn()

                                # a = True
                                # while a:
                                if track_index > 56:
                                    print("Player cannot move, track_index out of range.")
                                    self.next_player(player)
                                    break
                                    # self.display_turn()
                                    # else:
                                    #     a = False
                                if Engine.rolls_index > len(Engine.rolls_list) - 1:
                                    print("next player turn (in player move function)")
                                    self.next_player(player)
                                break


                if player.color == BLUE:
                    print("In move_when_out_function with color: ", player.color)
                    print("cx: ", cx)
                    print("cy: ", cy)
                    print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i),
                          [player.pawns[i].x0, player.pawns[i].x])
                    print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i),
                          [player.pawns[i].y0, player.pawns[i].y])
                    if (cx > player.pawns[i].x0 +13) and (cx < player.pawns[i].x+13):
                        print("out 1")
                        if (cy > player.pawns[i].y0+14) and (cy < player.pawns[i].y+14):
                            print("out 2")
                            if (player.pawns[i].x0 > out_x0) or (player.pawns[i].y0 < out_y0):
                                print("out 3")
                                print("A click was made on a {} pawn and it is outside.".format(player.color))
                                print("Engine.rolls_index: ", Engine.rolls_index)
                                track_index = player.pawns[i].curr_index + player.rolls[Engine.rolls_index]
                                print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
                                print("track_index: ", track_index)

                                if track_index < 56:
                                    self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
                                              opponent3=opponent3)
                                    player.pawns[i].x0 = player.box_path[track_index].x
                                    player.pawns[i].y0 = player.box_path[track_index].y
                                    player.pawns[i].x = player.box_path[track_index].x + 25
                                    player.pawns[i].y = player.box_path[track_index].y + 25
                                    player.pawns[i].curr_index = track_index  # updating the pawn position on board
                                    print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                    player.pawns[i].swap(x_coor=player.pawns[i].x0, y_coor=player.pawns[i].y0,
                                                         master=self.canvas)

                                    self.double_check(player=player)
                                    Engine.rolls_index = Engine.rolls_index + 1

                                    print(" in player_move_function: ", Engine.rolls_index)

                                if track_index == 56:
                                    player.pawns.remove(player.pawns[i])
                                    player.num_saved_pawns = player.num_saved_pawns + 1
                                    self.next_player(player)
                                    self.display_turn()

                                    # a = True
                                    # while a:
                                if track_index > 56:
                                    print("Player cannot move, track_index out of range.")
                                    self.next_player(player)
                                    break
                                    # self.display_turn()
                                    # else:
                                    #     a = False
                                if Engine.rolls_index > len(Engine.rolls_list) - 1:
                                    print("next player turn (in player move function)")
                                    self.next_player(player)
                                break

                if player.color == YELLOW or player.color == GREEN:
                    print("In move_when_out_function with color: ", player.color)
                    print("cx: ", cx)
                    print("cy: ", cy)
                    print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i),
                          [player.pawns[i].x0, player.pawns[i].x])
                    print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i),
                          [player.pawns[i].y0, player.pawns[i].y])
                    if (cx > player.pawns[i].x0+13) and (cx < player.pawns[i].x+13):
                        print("out 1")
                        if (cy > player.pawns[i].y0+14) and (cy < player.pawns[i].y+14):
                            print("out 2")
                            if (player.pawns[i].x0 < out_x0) or (player.pawns[i].y0 < out_y0):
                                print("out 3")
                                print("A click was made on a {} pawn and it is outside.".format(player.color))
                                print("Engine.rolls_index: ", Engine.rolls_index)
                                track_index = player.pawns[i].curr_index + player.rolls[Engine.rolls_index]
                                print("Engine.rolls_list[Engine.rolls_index]: ", Engine.rolls_list[Engine.rolls_index])
                                print("track_index: ", track_index)

                                if track_index < 56:
                                    self.kill(player=player, bb=track_index, opponent1=opponent1, opponent2=opponent2,
                                              opponent3=opponent3)
                                    player.pawns[i].x0 = player.box_path[track_index].x
                                    player.pawns[i].y0 = player.box_path[track_index].y
                                    player.pawns[i].x = player.box_path[track_index].x + 25
                                    player.pawns[i].y = player.box_path[track_index].y + 25
                                    player.pawns[i].curr_index = track_index  # updating the pawn position on board
                                    print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                    player.pawns[i].swap(x_coor=player.pawns[i].x0, y_coor=player.pawns[i].y0,
                                                         master=self.canvas)

                                    self.double_check(player=player)
                                    Engine.rolls_index = Engine.rolls_index + 1

                                    print(" in player_move_function: ", Engine.rolls_index)

                                if track_index == 56:
                                    player.pawns.remove(player.pawns[i])
                                    player.num_saved_pawns = player.num_saved_pawns + 1
                                    self.next_player(player)
                                    self.display_turn()

                                    # a = True
                                    # while a:
                                if track_index > 56:
                                    print("Player cannot move, track_index out of range.")
                                    self.next_player(player)
                                    break
                                    # self.display_turn()
                                    # else:
                                    #     a = False
                                if Engine.rolls_index > len(Engine.rolls_list) - 1:
                                    print("next player turn (in player move function)")
                                    self.next_player(player)
                                break

    def game(self, cx, cy):

        if self.player_turn == RED and Engine.turn == False:
            print("RED player's turn")

            if self.check_move(player=self.red_player) == False:
                print("In game: ", self.check_move(self.red_player))
                print("Before: ", Engine.player_turn)
                Engine.player_turn = BLUE
                print("After: ", Engine.player_turn)
                self.clean()

            if Engine.player_turn == RED:
                self.player_move(player=self.red_player, opponent1=self.blue_player, opponent2=self.yellow_player,
                                 opponent3=self.green_player, cx=cx, cy=cy, out_x0=270, out_y0=270)

        if self.player_turn == BLUE and Engine.turn == False:
            print("BLUE player's turn")
            if self.check_move(player=self.blue_player) == False:
                print("In game: ", self.check_move(self.blue_player))
                print("Before: ", Engine.player_turn)
                Engine.player_turn = YELLOW
                print("After: ", Engine.player_turn)
                self.clean()

            if Engine.player_turn == BLUE:
                self.player_move(player=self.blue_player, opponent1=self.yellow_player, out_x0=270, out_y0=470,
                                 opponent2=self.green_player, opponent3=self.red_player, cx=cx, cy=cy)

        if self.player_turn == YELLOW and Engine.turn == False:
            print("YELLOW player's turn")
            if self.check_move(player=self.yellow_player) == False:
                print("In game: ", self.check_move(self.yellow_player))
                print("Before: ", Engine.player_turn)
                Engine.player_turn = GREEN
                print("After: ", Engine.player_turn)
                self.clean()

            if Engine.player_turn == YELLOW:
                self.player_move(player=self.yellow_player, opponent1=self.green_player, out_x0=470, out_y0=470,
                                 opponent2=self.red_player, opponent3=self.blue_player, cx=cx, cy=cy)

        if self.player_turn == GREEN and Engine.turn == False:
            print("GREEN player's turn")
            if self.check_move(player=self.green_player) == False:
                print("In game: ", self.check_move(self.green_player))
                print("Before: ", Engine.player_turn)
                Engine.player_turn = RED
                print("After: ", Engine.player_turn)
                self.clean()

            if Engine.player_turn == GREEN:
                self.player_move(player=self.green_player, opponent1=self.red_player, opponent2=self.blue_player,
                                 opponent3=self.yellow_player, cx=cx, cy=cy, out_x0=470, out_y0=470)


if __name__ == "__main__":
    root = tk.Tk()
    d = Board(root)
    d.pack(side="top", fill="both", expand=True)
    e = Engine(d)
    root.mainloop()
