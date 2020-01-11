import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)  # police. to be put in game config class


class Board(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        # label = tk.Label(self, text="Page One", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text="Back to home",
        #                      command=lambda: controller.show_frame(StartPage))
        # button1.pack()

        # blue
        blue_box = tk.PhotoImage(file="img_gif/blue/blue_box.gif")
        blue_pawn = tk.PhotoImage(file="img_gif/blue/blue_pawn.gif")
        blue_side = tk.PhotoImage(file="img_gif/blue/blue_side.gif")
        blue_start = tk.PhotoImage(file="img_gif/blue/blue_start.gif")

        # green
        green_box = tk.PhotoImage(file="img_gif/green/green_box.gif")
        green_pawn = tk.PhotoImage(file="img_gif/green/green_pawn.gif")
        green_side = tk.PhotoImage(file="img_gif/green/green_side.gif")
        green_start = tk.PhotoImage(file="img_gif/green/green_start.gif")

        # red
        red_side = tk.PhotoImage(file="img_gif/red/red_side.gif")
        red_box = tk.PhotoImage(file="img_gif/red/red_box.gif")
        red_pawn = tk.PhotoImage(file="img_gif/red/red_pawn.gif")
        red_start = tk.PhotoImage(file="img_gif/red/red_start.gif")

        # yellow
        yellow_side = tk.PhotoImage(file="img_gif/yellow/yellow_side.gif")
        yellow_box = tk.PhotoImage(file="img_gif/yellow/yellow_box.gif")
        yellow_pawn = tk.PhotoImage(file="img_gif/yellow/yellow_pawn.gif")
        yellow_start = tk.PhotoImage(file="img_gif/yellow/yellow_start.gif")

        # others
        center = tk.PhotoImage(file="img_gif/center.gif")
        head = tk.PhotoImage(file="img_gif/head.gif")
        head1 = tk.PhotoImage(file="img_gif/head1.gif")
        head2 = tk.PhotoImage(file="img_gif/head2.gif")
        head3 = tk.PhotoImage(file="img_gif/head3.gif")
        tail = tk.PhotoImage(file="img_gif/tail.gif")
        tail1 = tk.PhotoImage(file="img_gif/tail1.gif")
        tail2 = tk.PhotoImage(file="img_gif/tail2.gif")
        tail3 = tk.PhotoImage(file="img_gif/tail3.gif")
        white_box = tk.PhotoImage(file="img_gif/white_box.gif")

        # placing board images
        self.set_image(image=blue_side, width=300, height=300, x_coor=-2, y_coor=448)
        self.set_image(image=green_side, width=296, height=296, x_coor=450, y_coor=0)
        self.set_image(image=red_side, width=298, height=298, x_coor=-1, y_coor=-1)
        self.set_image(image=yellow_side, width=294, height=294, x_coor=450, y_coor=450)
        self.set_image(image=center, width=150, height=150, x_coor=298, y_coor=298)

        # drawing white boxes
        self.draw_white_boxes(image=white_box, width=46, height=46, x_start=300, y_start=0, direction="vertical")
        self.draw_white_boxes(image=white_box, width=46, height=46, x_start=300, y_start=450, direction="vertical")
        self.draw_white_boxes(image=white_box, width=46, height=46, x_start=0, y_start=300, direction="horizontal")
        self.draw_white_boxes(image=white_box, width=46, height=46, x_start=450, y_start=300, direction="horizontal")

        # drawing colored boxes
        self.draw_colored_boxes(image=green_box, width=46, height=46, x_start=350, y_start=50, direction="vertical")
        self.draw_colored_boxes(image=yellow_box, width=46, height=46, x_start=450, y_start=350, direction="horizontal")
        self.draw_colored_boxes(image=blue_box, width=46, height=46, x_start=350, y_start=450, direction="vertical")
        self.draw_colored_boxes(image=red_box, width=46, height=46, x_start=50, y_start=350, direction="horizontal")

        # placing starting point
        self.set_image(image=green_start, width=46, height=46, x_coor=400, y_coor=50)
        self.set_image(image=yellow_start, width=46, height=46, x_coor=650, y_coor=400)
        self.set_image(image=red_start, width=46, height=46, x_coor=50, y_coor=300)
        self.set_image(image=blue_start, width=46, height=46, x_coor=300, y_coor=650)

        # placing arrows
        self.set_image(image=head, width=46, height=46, x_coor=250, y_coor=400)
        self.set_image(image=head1, width=46, height=46, x_coor=400, y_coor=450)
        self.set_image(image=head2, width=46, height=46, x_coor=450, y_coor=300)
        self.set_image(image=head3, width=46, height=46, x_coor=300, y_coor=250)
        self.set_image(image=tail, width=46, height=46, x_coor=300, y_coor=450)
        self.set_image(image=tail1, width=46, height=46, x_coor=450, y_coor=400)
        self.set_image(image=tail2, width=46, height=46, x_coor=400, y_coor=250)
        self.set_image(image=tail3, width=46, height=46, x_coor=250, y_coor=300)

    def set_image(self, image, width, height, x_coor, y_coor):
        label_image = tk.Label(self, image=image, width=width, height=height)
        label_image.image = image
        label_image.place(x=x_coor, y=y_coor)

    def draw_board(self):
        pass

    def draw_white_boxes(self, image, width, height, x_start, y_start, direction):
        coord_x = 0  # z
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

    def draw_colored_boxes(self, image, width, height, x_start, y_start, direction):
        coord = 0
        while coord != 250:
            if direction == "vertical":
                self.set_image(image=image, width=width, height=height, x_coor=x_start, y_coor=y_start + coord)
                coord = coord + 50
            if direction == "horizontal":
                self.set_image(image=image, width=width, height=height, x_coor=x_start + coord, y_coor=y_start)
                coord = coord + 50
