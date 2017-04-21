from tkinter import *
from tkinter import ttk
from client.MyFrame import MyFrame

class ChatFrame(MyFrame):
    title = "Chat"

    def initChatFrame(self):
        self.root.title(self.title)
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.root.mainloop()