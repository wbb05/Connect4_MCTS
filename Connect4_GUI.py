from tkinter import *
from tkinter import ttk

from Connect4_Solver import Connect4_Solver

# TODO: Make board size flexible?
class Connect4_GUI:
    def __init__(self, root):

        # Main window
        root.title("Connect 4")
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Grid layout
        mainframe.rowconfigure(1, weight= 1)
        mainframe.rowconfigure(2, weight= 5)
        mainframe.rowconfigure(3, weight= 1)

        # Select buttons
        ttk.Button(mainframe, text= "Select 0", command= self.select0).grid(column= 1, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 1", command= self.select1).grid(column= 2, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 2", command= self.select2).grid(column= 3, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 3", command= self.select3).grid(column= 4, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 4", command= self.select4).grid(column= 5, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 5", command= self.select5).grid(column= 6, row = 2, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 6", command= self.select6).grid(column= 7, row = 2, sticky=(N, W, E, S))

        # Canvas
        canvas_width = 550
        canvas_height = 500
        self.board_rows = 6
        self.board_cols = 7
        self.canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid(column= 0, row = 3, columnspan= 7, sticky = (N, W, E, S))

        # Add circles (ovals)
        self.cells = [[0 for _ in range(self.board_cols)] for _ in range(self.board_rows)]

        padding = 20
        x0 = padding
        y0 = padding
        x1 = canvas_width / self.board_cols - padding
        y1 = canvas_height / self.board_rows - padding
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                self.cells[row][col] = self.canvas.create_oval(x0, y0, x1, y1, fill= "white")
                # Next col
                x0 = x1 + padding * 2
                x1 += canvas_width / self.board_cols

            # Next row    
            y0 = y1 + padding * 2
            y1 += canvas_height / self.board_rows
            x0 = padding
            x1 = canvas_width / self.board_cols - padding

        # Reset button
        ttk.Button(mainframe, text= "Reset", command= self.reset).grid(column= 1, row = 1, sticky=(N, W, E, S))

        # Text box
        self.turn_text = StringVar()
        self.turn_text.set("Red's Turn")
        ttk.Label(mainframe, textvariable= self.turn_text).grid(column=2, row=1, sticky=W)

        # Play AI checkbox
        self.ai_play = StringVar()
        ttk.Checkbutton(mainframe, text='Play AI',variable=self.ai_play, onvalue=1, offvalue=0).grid(column= 3, row= 1, sticky= (N, W, E, S))

        # AI level combobox
        self.ai_level = StringVar()
        ai_level_combobox = ttk.Combobox(mainframe, textvariable=self.ai_level, 
                                         values= ('Easy', 'Medium', 'Hard'))
        ai_level_combobox.grid(column=4, row= 1, columnspan=2, sticky= W)
        self.ai_level.set('Medium')

        # Event listener
        ai_level_combobox.bind("<<ComboboxSelected>>", self.change_ai_level)

        # State variable: turn
        # 0: Red 
        # 1: Yellow
        self.turn = 0

        # AI
        self.AI = Connect4_Solver()

        # END Init

    # Button functions
    def select0(self):
        self.select_button_pressed(0)
    def select1(self):
        self.select_button_pressed(1)
    def select2(self):
        self.select_button_pressed(2)
    def select3(self):
        self.select_button_pressed(3)
    def select4(self):
        self.select_button_pressed(4)
    def select5(self):
        self.select_button_pressed(5)
    def select6(self):
        self.select_button_pressed(6)

    # Handles any select button press
    def select_button_pressed(self, col: int):

        # Check win condition
        if self.AI.game.won(1):
            self.turn_text.set("Red Won!")
            return
        elif self.AI.game.won(2):
            self.turn_text.set("Yellow Won!")
            return

        # Add either red or yellow piece
        if not self.turn:
            self.AI.add_player_piece(col)
        else:
            self.AI.add_ai_piece(col)

        # Add player piece
        self.add_piece(col)

        # Add AI piece
        if self.ai_play.get() == "1":            
            ai_col = self.AI.ai_predict()
            self.AI.add_ai_piece(ai_col)
            self.add_piece(ai_col)

        # Check win condition again
        if self.AI.game.won(1):
            self.turn_text.set("Red Won!")
            return
        elif self.AI.game.won(2):
            self.turn_text.set("Yellow Won!")
            return

    # Adds piece to col
    def add_piece(self, col: int):

        # Make sure col isn't full
        if self.canvas.itemcget(self.cells[0][col], 'fill') != "white":
            return

        # Find first unoccupied row
        row = self.board_rows-1
        while row > 0 and self.canvas.itemcget(self.cells[row][col], "fill") != "white":
            row -= 1

        # Red's turn
        if not self.turn:
            self.canvas.itemconfig(self.cells[row][col], fill= "red")
            self.turn_text.set("Yellow's Turn")
        else:
            # Yellow's turn
            self.canvas.itemconfig(self.cells[row][col], fill= "yellow")
            self.turn_text.set("Red's Turn")

        self.turn = not self.turn

    def change_ai_level(self, event):
        self.AI.change_level(self.ai_level.get())

    # Resets board
    def reset(self):
        # Reset AI
        self.AI.reset()
        self.AI.change_level(self.ai_level.get())

        # Reset turn
        self.turn = 0
        self.turn_text.set("Red's Turn")

        # Reset board
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                self.canvas.itemconfig(self.cells[row][col], fill= "white")



        

