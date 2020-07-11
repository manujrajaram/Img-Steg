

'''def open():
    askopenfilename()'''

'''def mainscreen():
    screen= Tk()
    screen.geometry("400x300")
    screen.title("File-Chooser")
    Label(text = "Choose a File",fg="blue")
    Button(text="Choose",height="2",width="30",command=askopenfilename).pack()
    
mainscreen()'''

from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =(("PNG Files","*.png"),("All Files","*.*")))
print (root.filename)
