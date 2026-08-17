from tkinter import *
from tkinter import ttk

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
        canvas = Canvas(root, width=500, height=500, bg="white")
        canvas.grid(column= 0, row = 2, columnspan= 7, sticky = (N, W, E, S))

        # Add circles (ovals)


        # Text box
        #ttk.Label(mainframe, text= "Hello there").grid(column=1, row=3, sticky=W)

        # END Init

    # Button functions
    def select0(self):
        pass
    def select1(self):
        pass
    def select2(self):
        pass
    def select3(self):
        pass
    def select4(self):
        pass
    def select5(self):
        pass
    def select6(self):
        pass
        



        

