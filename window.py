from maxheap import maxheap
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Project 3")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the Data Structure menu object
        DataStructure = Menu(menu)

        # Adds Sub-Options for Data Structures Tab
        DataStructure.add_command(label="Max-Heap", command=self.max_heap)
        DataStructure.add_command(label="Graph", command=self.graph)

        # Adds Data Structure Tab to menu
        menu.add_cascade(label="Data Structure", menu=DataStructure)

        # create the Search menu object
        search = Menu(menu)

        # Adds Sub-Options for Search Tab
        search.add_command(label="Search for a Song Using ID", command = self.searchID)
        search.add_command(label="Search for an ID Using a Song", command = self.searchName)

        # Adds Search Tab to menu
        menu.add_cascade(label="Search", menu=search)


    def client_exit(self):
        exit()
    def max_heap(self):
        print("Call Max-Heap Builder")
    def graph(self):
        print("Call Graph Builder")
    def searchID(self):
        print("Call searchID function")
    def searchName(self):
        print("Call searchName function")

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()