from tkinter import *
from tkinter import ttk

from client.ui.MyFrame import MyFrame


class ChatFrame(MyFrame):

    def init(self):
        self.root.title(self.model.statusString.get())
        self.root.protocol('WM_DELETE_WINDOW', self.model.exit)
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.chatFrame = ttk.Labelframe(self.mainframe, text='Chat',width = 1000,height = 800)
        self.chatFrame.grid(column = 0,row = 0,columnspan = 12)
        self.chatField = Text(self.chatFrame,width=80)
        self.chatField.grid(column = 0,row = 0)
        self.scrollBar = ttk.Scrollbar(self.chatFrame, orient=VERTICAL, command=self.chatField.yview)
        self.scrollBar.grid(column=1,row=0)
        self.chatField['yscrollcommand'] = self.scrollBar.set
        self.chatField.config(state=DISABLED)

        self.messagelabel = ttk.Label(self.mainframe, text="Answer : ")
        self.messagelabel.grid(column=0, row=1,sticky=W)
        self.channelList = ttk.Combobox(self.mainframe,textvariable = self.model.currentChannel)
        self.channelList['values'] = self.model.channels
        self.channelList.grid(column=1,row=1)
        self.messagefield = ttk.Entry(self.mainframe, width=90, textvariable=self.model.currentmessage)
        self.messagefield.grid(column=2, row=1)
        self.sendbutton = ttk.Button(self.mainframe,text="Send",command = self.model.sendMessage)
        self.sendbutton.grid(column=3,row=1)


        self.root.bind('<Return>', self.onReturnPressed)
        self.messagefield.focus()
        for message in self.model.messages:
            self.chatField.insert('end', str(message))
        self.model.registerListener(self)
        self.model.thread.start()
        self.root.mainloop()

    def onReturnPressed(self, event):
        self.model.sendMessage()

    def notify(self):
        self.chatField.config(state=NORMAL)
        self.chatField.insert('end', str(self.model.messages[len(self.model.messages)-1])+'\n')
        self.chatField.config(state=DISABLED)
        #self.mainframe.update()

