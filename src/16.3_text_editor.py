from tkinter import filedialog, messagebox
from tkinter import *

filename = "Untitled"

def newFile():
    global filename

    filename = "Untitled"
    text.delete( 0.0, END )

def saveFile():
    global filename

    t = text.get( 0.0, END )
    f = open( filename, 'w' )

    f.write( t )
    f.close()

def saveFileAs():
    file_path = filedialog.asksaveasfilename(  initialdir = "./", title = "Select file", filetypes = [ ('all files', '.*'), ('text files', '.txt') ], defaultextension=".py" )
    
    text_body = text.get( 0.0, END  )
    
    f = open( file_path, "w+" )
    f.write( text_body )
    f.close()

def openFile():
    f = filedialog.askopenfile( mode="r" )
    t = f.read()

    text.delete( 0.0, END )
    text.insert(  0.0, t )

root = Tk()

root.title( "Python Text Editor" )
root.minsize( width=400, height=400 )
root.maxsize( width=400, height=400 )

text = Text( root, width=400, height=400 )
text.pack()

menu_bar = Menu( root )
filemenu = Menu( menu_bar )

filemenu.add_command( label="New", command=newFile )
filemenu.add_command( label="Open", command=openFile )
filemenu.add_command( label="Save", command=saveFile )
filemenu.add_command( label="Save As..", command=saveFileAs )

filemenu.add_separator()

filemenu.add_command( label="Quit", command=root.quit )

menu_bar.add_cascade( label="file", menu=filemenu )

root.config( men=menu_bar )

root.mainloop()