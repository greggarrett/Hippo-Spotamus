from maxheap import maxheap
import time
from tkinter import *
from PIL import Image, ImageTk
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
        self.showImg()

    def showImg(self):
        loadBlack = Image.open("black.png")
        renderBlack = ImageTk.PhotoImage(loadBlack)

        imgBlack = Label(self, image=renderBlack)
        imgBlack.image = renderBlack
        imgBlack.place(x=0, y=0)

        loadGreen = Image.open("green.png")
        renderGreen = ImageTk.PhotoImage(loadGreen)

        imgGreen = Label(self, image=renderGreen)
        imgGreen.image = renderGreen
        imgGreen.place(x=25, y=25)

    def showGraphText(self):
        text = Label(self, text="Now Generating Your Playlist!")
        text.place(x=50, y=50)
    def showHeapText(self):
        text = Label(self, text="Now Generating Your Playlist!")
        text.place(x=50, y=50)

    def client_exit(self):
        exit()
    def max_heap(self):
        self.showHeapText()
        print("Call Max-Heap Builder", 12)
    def graph(self):
        self.showGraphText()
        print("Call Graph Builder")
    def searchID(self):
        print("Call searchID function")
    def searchName(self):
        print("Call searchName function")

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()