#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
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

        # tk.messagebox.showinfo(title=None, message="TO START GAME PRESS OKAY & TO EXIT PRESS CROSS UP IN THE WINDOW")

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

        roll_button = tk.Button(self.canvas, text="Roll", relief="raised", font=LARGE_FONT, command=self.rolls)
        roll_button.pack(in_=self.canvas)
        roll_button.place(x=800, y=120)


        self.display_turn()

    def left_click(self, event):
        Engine.cx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        Engine.cy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        print("#########left_click######")
        print("clicked at", Engine.cx, Engine.cy)

        self.game(cx=Engine.cx, cy=Engine.cy)  # The game is on each time we make a left click

    def set_label(self, text, font_color, font, x_coor, y_coor):
        label = tk.Label(text=text, fg=font_color, font=font)
        label.pack()
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
            self.label1 = self.set_label(text="Red player turn", font_color="Black", font=LARGE_FONT, x_coor=770,
                                         y_coor=50)
        if self.player_turn == BLUE:
            self.label1 = self.set_label(text="Blue player turn", font_color="Black", font=LARGE_FONT, x_coor=770,
                                         y_coor=50)
        if self.player_turn == YELLOW:
            self.label1 = self.set_label(text="Yellow player turn", font_color="Black", font=LARGE_FONT, x_coor=770,
                                         y_coor=50)
        if self.player_turn == GREEN:
            self.label1 = self.set_label(text="Green player turn", font_color="Black", font=LARGE_FONT, x_coor=770,
                                         y_coor=50)

    def rolls(self):
        if Engine.turn:
            # print("turn: ", Engine.turn)

            Engine.num_rolls = Engine.num_rolls + 1
            # print("Number of rolls: ", Engine.num_rolls)

            if Engine.num_rolls == 1:
                # print("i'm in")
                Engine.dice = random.randint(1, 6)
                self.label2 = self.set_label(text=Engine.dice, font_color="Black", font=LARGE_FONT, x_coor=800,
                                             y_coor=200)
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
                    self.label3 = self.set_label(text=Engine.dice1, font_color="Black", font=LARGE_FONT, x_coor=800,
                                                 y_coor=250)
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
                    self.label4 = self.set_label(text=Engine.dice2, font_color="Black", font=LARGE_FONT, x_coor=800,
                                                 y_coor=300)
                    # print("dice2:", Engine.dice2)
                    Engine.rolls_list.append(Engine.dice2)
                    Engine.turn = False
                    print("Next player turn")
                    num_rolls = 0
        print("rolls from rolls' function: ", Engine.rolls_list)

    def check_move(self, player):  # Check if the player can make a move
        print("##############in_check_move#############")
        a = all(roll == 6 for roll in Engine.rolls_list)
        print("check if 3 6 in a roll, dices: ", a)
        if a == True:  # check if he rolled 6 3 times
            return False

        win = True
        if player.num_saved_pawns != 4:
            win = False

        if (win == False) and (Engine.rolls_list[0] != 6):
            print(len(player.pawns))
            for i in range(len(player.pawns)):
                a = player.pawns[i].curr_index
                print("In check_move: \n player.pawns[{", i, "}].curr_index : ", a)
                if player.pawns[i].curr_index != -1:
                    print("The player can move his avalaible pawns.")
                    return True
                print("The players pawns are all at home. He cannot move")
            return False

        if win == True:
            print("the {}_player won the game.".format(player.color))
            self.label1.config(text="{} wins!".format(player.color))
            tk.messagebox.showinfo("CONGRATULATIONS!",
                                   "It's the end... The {} player won the game.".format(player.color))
            self.canvas.master.quit()
            return False
        print("#######exiting check_move function###########")

    @staticmethod
    def kill(player, bb, opponent1, opponent2, opponent3):
        print("Entering kill_function")
        # check if the game piece is not on a starting point
        if player.box_path[bb].x0 != player.white_boxes[1].x and player.box_path[bb].y0 != player.white_boxes[1].y:
            if player.box_path[bb].x0 != player.white_boxes[14].x and player.box_path[bb].y0 != player.white_boxes[
                14].y:
                if player.box_path[bb].x0 != player.white_boxes[27].x and player.box_path[bb].y0 != player.white_boxes[
                    27].y:
                    if player.box_path[bb].x0 != player.white_boxes[40].x and player.box_path[bb].y0 != \
                            player.white_boxes[40].y:

                        # if the game piece of another color and its on the same block and it is not a double, a
                        # kill is made
                        for i in range(len(opponent1.pawns)):
                            if opponent1.pawns[i].x0 == player.box_path[bb].x:
                                if opponent1.pawns[i].y0 == player.box_path[bb].y:
                                    if not opponent1.pawns[i].double:
                                        opponent1.pawns[i].x0 = opponent1.homes[i].x
                                        opponent1.pawns[i].y0 = opponent1.homes[i].y
                                        opponent1.pawns[i].x = opponent1.homes[i].x + 25
                                        opponent1.pawns[i].y = opponent1.homes[i].y + 25
                                        opponent1.pawns[i].curr_index = -1
                                        opponent1.pawns[i].swap()
                                        print("kill made")
                                        break

                        for i in range(len(opponent2.pawns)):
                            if opponent2.pawns[i].x0 == player.box_path[bb].x:
                                if opponent2.pawns[i].y0 == player.box_path[bb].y:
                                    if not opponent2.pawns[i].double:
                                        opponent2.pawns[i].x0 = opponent2.homes[i].x
                                        opponent2.pawns[i].y0 = opponent2.homes[i].y
                                        opponent2.pawns[i].x = opponent2.homes[i].x + 25
                                        opponent2.pawns[i].y = opponent2.homes[i].y + 25
                                        opponent2.pawns[i].curr_index = -1
                                        opponent2.pawns[i].swap()
                                        print("kill made")
                                        break

                        for i in range(len(opponent3.pawns)):
                            if opponent3.pawns[i].x0 == player.box_path[bb].x:
                                if opponent3.pawns[i].y0 == player.box_path[bb].y:
                                    if not opponent3.pawns[i].double:
                                        opponent3.pawns[i].x0 = opponent3.homes[i].x
                                        opponent3.pawns[i].y0 = opponent3.homes[i].y
                                        opponent3.pawns[i].x = opponent3.homes[i].x + 25
                                        opponent3.pawns[i].y = opponent3.homes[i].y + 25
                                        opponent3.pawns[i].curr_index = -1
                                        opponent3.pawns[i].swap()
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
        print("Before cleaning: ", Engine.num_rolls, Engine.rolls_index, Engine.rolls_list, Engine.turn)
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

    def player_move(self, player, opponent1, opponent2, opponent3, cx, cy, out_x0, out_y0):
        print("#######################{}_player_move_function############".format(player.color))
        print(cx)
        print(cy)
        print("[x0, x]: ", [player.pawns[0].x0, player.pawns[0].x])
        print("[y0, y]: ", [player.pawns[0].y0, player.pawns[0].y])
        print([player.pawns[0].x0, player.homes[0].x], [player.pawns[0].y0, player.homes[0].y])
        # rolls = Engine.rolls_list
        # print("rolls from player_game: ", rolls)

        if Engine.player_turn == player.color:  # It's this player's turn (according to it's color)
            for i in range(len(player.pawns)):  # Check if click is made on a pawn
                print("ENTERING move_to_start_function")
                if (cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13):  # Check if click is made on a pawn
                    print("on start 1")
                    if (cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14):
                        print("on start 2")
                        if (player.pawns[i].x0 == player.homes[i].x) and (player.pawns[i].y0 == player.homes[i].y):
                            print("A click was made on a {} pawn and it is in his home.".format(player.color))

                            if Engine.rolls_list[Engine.rolls_index] == 6:
                                player.pawns[i].x0 = player.box_path[0].x
                                player.pawns[i].y0 = player.box_path[0].y
                                player.pawns[i].x = player.box_path[0].x + 25
                                player.pawns[i].y = player.box_path[0].y + 25
                                player.pawns[i].curr_index = 0  # "placing" pawn on the starting point
                                print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                player.pawns[i].swap()
                                Engine.rolls_index = Engine.rolls_index + 1
                                print("FROM move_to_start_function:", Engine.rolls_index)

                                if Engine.rolls_index > len(Engine.rolls_list) - 1:
                                    self.next_player(player)
                                break

                print("ENTERING move_when_out_function")
                print("player's color: ", player.color)
                if player.color == RED:
                    print("In move_when_out_function with color: ", player.color)
                    print("cx: ", cx)
                    print("cy: ", cy)
                    print("[player.pawns[{}].x0, player.pawns[{}].x]".format(i, i),
                          [player.pawns[i].x0, player.pawns[i].x])
                    print("[player.pawns[{}].y0, player.pawns[{}].y]".format(i, i),
                          [player.pawns[i].y0, player.pawns[i].y])
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
                                    player.pawns[i].curr_index = track_index
                                    print("player.pawns[{}].curr_index: {}".format(i, player.pawns[i].curr_index))
                                    player.pawns[i].swap()  # updating the pawn position on board

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
                    if (cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13):
                        print("out 1")
                        if (cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14):
                            print("out 2")
                            if (player.pawns[i].x0 > out_x0) or (player.pawns[i].y0 < out_y0):
                                print("out 3")
                                print("A click was made on a {} pawn and it is outside.".format(player.color))
                                print("Engine.rolls_index: ", Engine.rolls_index)
                                track_index = player.pawns[i].curr_index + Engine.rolls_list[Engine.rolls_index]
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
                                    player.pawns[i].swap()

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
                    if (cx > player.pawns[i].x0 + 13) and (cx < player.pawns[i].x + 13):
                        print("out 1")
                        if (cy > player.pawns[i].y0 + 14) and (cy < player.pawns[i].y + 14):
                            print("out 2")
                            if (player.pawns[i].x0 < out_x0) or (player.pawns[i].y0 < out_y0):
                                print("out 3")
                                print("A click was made on a {} pawn and it is outside.".format(player.color))
                                print("Engine.rolls_index: ", Engine.rolls_index)
                                track_index = player.pawns[i].curr_index + Engine.rolls_list[Engine.rolls_index]
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
                                    player.pawns[i].swap()

                                    self.double_check(player=player)
                                    Engine.rolls_index = Engine.rolls_index + 1

                                    print(" in player_move_function: ", Engine.rolls_index)

                                if track_index == 56:
                                    player.pawns.remove(player.pawns[i])
                                    player.num_saved_pawns = player.num_saved_pawns + 1
                                    self.next_player(player)
                                    self.display_turn()

                                if track_index > 56:
                                    print("Player cannot move, track_index out of range.")
                                    self.next_player(player)
                                    break

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

    def save(self):
        tk.messagebox.showinfo("Save game",  'Do you want to save the game? Press "OK" if yes.')
        saved_data = [{"player_turn": Engine.player_turn}]

        red_player = self.save_data(self.red_player)
        blue_player = self.save_data(self.blue_player)
        yellow_player = self.save_data(self.yellow_player)
        green_player = self.save_data(self.green_player)

        saved_data.append(red_player)
        saved_data.append(blue_player)
        saved_data.append(yellow_player)
        saved_data.append(green_player)

        with open('saved_data_file.json', 'a') as save_file:
            json.dump(saved_data, save_file, sort_keys=False, indent=12, separators=(',', ':'), ensure_ascii=False)

        self.canvas.master.quit()

    @staticmethod
    def save_data(player):
        dico = {
            "color": player.color,
            "num_saved_pawns": player.num_saved_pawns,
            "pawns": []
        }

        for pawn in player.pawn:
            m = dict(x0_y0=[pawn.x0, pawn.y0], x_y=[pawn.x, pawn.y], curr_index=pawn.curr_index, double=pawn.double)
            dico["pawns"].append(m)
        return dico

    def load(self):  # load the most recent game
        tk.messagebox.showinfo("Load game", "Are you sure? ")
        print("............loading started............")
        with open('saved_data_file.json', 'r') as save_file:
            data = json.load(save_file)

            Engine.player_turn = data[0]["player_turn"]
            self.display_turn()

            red_p = data[1]
            blue_p = data[2]
            yellow_p = data[3]
            green_p = data[4]

            self.load_data(self.red_player, red_p)
            self.load_data(self.blue_player, blue_p)
            self.load_data(self.yellow_player, yellow_p)
            self.load_data(self.green_player, green_p)
        print("............loading ended............")

    @staticmethod
    def load_data(player, dico):
        player.num_saved_pawns = dico["num_saved_pawns"]
        i = 0
        for pawn in player.pawns:
            pawn.x0 = dico["pawns"][i]["x0_y0"][0]
            pawn.y0 = dico["pawns"][i]["x0_y0"][1]
            pawn.x = dico["pawns"][i]["x_y"][0]
            pawn.y = dico["pawns"][i]["x_y"][1]
            pawn.curr_index = dico["pawns"][i]["curr_index"]
            pawn.out = dico["pawns"][i]["out"]
            pawn.double = dico["pawns"][i]["double"]
            pawn.swap()
            i = i + 1

    def exit(self):
        tk.messagebox.showinfo("Exit game", "You are quitting... :(")
        self.canvas.master.quit()
        
    def new(self):   
        # Ongoing         
        self.red_player.pawns = self.red_player.init_pawns(image_file_path=RED_PAWN, width=PAWN_WIDTH, height=PAWN_HEIGHT, master=self.canvas,
        ref_x=100, ref_y=100, size=25)
        self.blue_player.pawns.clear()
        self.yellow_player.pawns.clear()
        self.green_player.pawns.clear()
        
        # self.red_player = Player(master=self.canvas, image_file_path=RED_PAWN, color=RED, width=PAWN_WIDTH,
        #                          height=PAWN_HEIGHT, turn=True)
        # self.blue_player = Player(master=self.canvas, image_file_path=BLUE_PAWN, color=BLUE, width=PAWN_WIDTH,
        #                           height=PAWN_HEIGHT)
        # self.yellow_player = Player(master=self.canvas, image_file_path=YELLOW_PAWN, color=YELLOW, width=PAWN_WIDTH,
        #                             height=PAWN_HEIGHT)
        # self.green_player = Player(master=self.canvas, image_file_path=GREEN_PAWN, color=GREEN, width=PAWN_WIDTH,
        #                            height=PAWN_HEIGHT)
        


if __name__ == "__main__":
    root = tk.Tk()
    d = Board(root)
    d.pack(side="top", fill="both", expand=True)
    e = Engine(d)
    # menubar = Menu(root) 
    # root.config(menu=menubar) 
    # menufichier = Menu(menubar,tearoff=0) 
    # menubar.add_cascade(label="Fichier", menu=menufichier)
    # menufichier.add_command(label="Nouvelle partie", underline=1, command=e.new)
    # menufichier.add_command(label="Sauvegarder", underline=1, command=e.save)
    # menufichier.add_command(label="Charger", underline=1, command=e.load)
    # menufichier.add_separator()
    # menufichier.add_command(label="Quitter", underline=1, command=exit)
    root.mainloop()
