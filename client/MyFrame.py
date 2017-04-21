from tkinter import *
from tkinter import ttk
class MyFrame:
    def __init__(self,model):
        self.model = model
        self.root = Tk()

    def refresh(self):
        self.root.update()

    def destroy(self):
        self.root.destroy()