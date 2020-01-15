import tkinter as tk
from tkinter import ttk
from board import Board

LARGE_FONT = ("Verdana", 12)  # police. to be put in game config class


class LudoApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry('1000x750')

        tk.Tk.wm_title(self, "Test Jeu de ludo")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Board):  # <- add the newly created page here

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]  # cont = container
        frame.tkraise()  # raise the container "cont" to the top


# useful code to create a new page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        #tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="visit page 1",
                            command=lambda: controller.show_frame(Board))
        button.pack()


if __name__ == "__main__":
    app = LudoApp()
    app.mainloop()
