from tkinter import *
from tkinter.ttk import Entry
import os



def listfiles():
    global path
    path = txtfld.get()
    global files
    files = list(os.listdir(path))
    xpos=50
    ypos=80
    for i in files:
        lbl1 = Label(window, text=i, fg='black',font=('Verdana',12))
        lbl1.place(x=xpos,y=ypos)
        ypos+=20


def openNewWindow(path,files):
    newWindow = Tk()
    newWindow.title('Display List of PDF Files')
    pdffiles = list(files.endswith('.pdf'))
    if len(pdffiles) > 0:
        newlbl = Label(newWindow, text = 'There are PDF files in this location to be merged',fg='blue',font=('Helvetica',16))
        newlbl.place(x=50,y=20)
    else:
        newlbl = Label(newWindow, text='There are no PDF files in this location to be merged', fg='blue',
                       font=('Helvetica', 16))
        newlbl.place(x=50, y=20)


window=Tk()
window.title('List Files in the Location Entered')
window.geometry('300x300')
txtfld = Entry(window, text = ' ')
txtfld.place(x=50,y=50)
lbl = Label(window, text='Please Enter the Path here',fg='blue',font=('Helvetica',16))
lbl.place(x=50,y=20)
btn = Button(window, text = 'List Files', command=listfiles)
btn.place(x=200,y=50)
#btn1 = Button(window, text = 'Seach for PDF Files', command=openNewWindow)
#btn1.place(x=300,y=300)
#path = txtfld.get()
window.mainloop()
#openNewWindow(path,files)



