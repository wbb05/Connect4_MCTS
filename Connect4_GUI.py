from tkinter import *
from tkinter import ttk

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
        ttk.Button(mainframe, text= "Select 0", command= self.select0).grid(column= 1, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 1", command= self.select1).grid(column= 2, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 2", command= self.select2).grid(column= 3, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 3", command= self.select3).grid(column= 4, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 4", command= self.select4).grid(column= 5, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 5", command= self.select5).grid(column= 6, row = 1, sticky=(N, W, E, S))
        ttk.Button(mainframe, text= "Select 6", command= self.select6).grid(column= 7, row = 1, sticky=(N, W, E, S))

        # Canvas
        canvas_width = 500
        canvas_height = 500
        self.board_rows = 6
        self.board_cols = 7
        self.canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid(column= 0, row = 2, columnspan= 7, sticky = (N, W, E, S))

        # Add circles (ovals)
        # TODO: Add padding    
        self.cells = [[0 for _ in range(self.board_cols)] for _ in range(self.board_rows)]

        x0 = 0
        y0 = 0
        x1 = canvas_width / self.board_cols
        y1 = canvas_height / self.board_rows
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                
                self.cells[row][col] = self.canvas.create_oval(x0, y0, x1, y1, fill= "white")
                # Next col
                x0 = x1
                x1 += canvas_width / self.board_cols

            # Next row    
            y0 = y1
            y1 += canvas_height / self.board_rows
            x0 = 0
            x1 = canvas_width / self.board_cols


        # Reset button
        ttk.Button(mainframe, text= "Reset", command= self.reset_board).grid(column= 1, row = 3, sticky=(N, W, E, S))

        # Text box
        self.turn_text = StringVar()
        self.turn_text.set("Red's Turn")
        ttk.Label(mainframe, textvariable= self.turn_text).grid(column=2, row=3, sticky=W)
        

        # State variable: turn
        # 0: Red 
        # 1: Yellow
        self.turn = 0

        # END Init

    # Button functions
    def select0(self):
        self.add_piece(0)
    def select1(self):
        self.add_piece(1)
    def select2(self):
        self.add_piece(2)
    def select3(self):
        self.add_piece(3)
    def select4(self):
        self.add_piece(4)
    def select5(self):
        self.add_piece(5)
    def select6(self):
        self.add_piece(6)

    # Adds piece to col
    def add_piece(self, col: int):

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

    # Resets board
    def reset_board(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                self.canvas.itemconfig(self.cells[row][col], fill= "white")



        

