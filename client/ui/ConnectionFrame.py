from tkinter import *
from tkinter import ttk

from client.ui.MyFrame import MyFrame


class ConnectionFrame(MyFrame):

    def init(self):
        self.root.title("Connect")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0,)

        #Nickname field
        self.usernameLabel = ttk.Label(self.mainframe, text="Username : ")
        self.usernameLabel.grid(column=1, row=1,sticky=W)
        self.usernameField= ttk.Entry(self.mainframe, width=14, textvariable=self.model.userNameString)
        self.usernameField.grid(column=2,row=1,sticky=(W, E))

        #Connection field
        self.hostnameLabel = ttk.Label(self.mainframe, text="Hostname : ")
        self.hostnameLabel.grid(column=1, row=2, sticky=W)
        self.hostnameField = ttk.Entry(self.mainframe, width=21, textvariable=self.model.hostname)
        self.hostnameField.grid(column=2, row=2, sticky=(W, E))
        self.portLabel = ttk.Label(self.mainframe, text="Port : ")
        self.portLabel.grid(column=3, row=2, sticky=W)
        self.portField = ttk.Entry(self.mainframe, width=7, textvariable=self.model.port)
        self.portField.grid(column=4,row=2)
        self.connectButton = ttk.Button(self.mainframe, text="Connect", command=self.model.connect)
        self.connectButton.grid(column=5, row=2,sticky=W)
        self.statusLabel = ttk.Label(self.mainframe, textvariable=self.model.statusString)
        self.statusLabel.grid(column=1, row=3)
        self.usernameField.focus()
        self.root.bind('<Return>', self.onReturnPressed)


        #Starting eventLoop
        self.root.mainloop()

    def onReturnPressed(self,event):
        self.model.connect()
