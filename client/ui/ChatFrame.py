from tkinter import *
from tkinter import ttk

from client.ui.MyFrame import MyFrame


class ChatFrame(MyFrame):

    def init(self):
        self.root.title(self.model.statusString.get())

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.chatFrame = ttk.Labelframe(self.mainframe, text='Chat',width = 800,height = 800)
        self.chatFrame.grid(column = 0,row = 0,columnspan = 12)
        self.chatField = Text(self.chatFrame)
        self.chatField.grid(column = 0,row = 0)
        self.chatField.config(state=DISABLED)

        self.messagelabel = ttk.Label(self.mainframe, text="Answer : ")
        self.messagelabel.grid(column=0, row=1,sticky=W)
        self.messagefield = ttk.Entry(self.mainframe, width=90, textvariable=self.model.currentmessage)
        self.messagefield.grid(column=1, row=1)
        self.sendbutton = ttk.Button(self.mainframe,text="Send",command = self.model.sendMessage)
        self.sendbutton.grid(column=3,row=1)

    
        self.root.bind('<Return>', self.onReturnPressed)
        self.messagefield.focus()
        self.root.mainloop()

    def onReturnPressed(self, event):
        self.model.sendMessage()
