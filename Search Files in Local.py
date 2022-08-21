from tkinter import*
from tkinter import filedialog as fd
import os

m = Tk()
m.geometry("1000x500")

#search function
def searchfile():
    # get the inputs
    finput = searchinputvalue.get()
    sinput = extensionvalue.get()

    #concat the file name with extension
    fileName = finput+sinput
    print(fileName)

    #open the file
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    m.filename = fd.askopenfilename(
        initialdir="C:\Users\subas\Documents",
        title="Open Text file",
        filetypes=filetypes)

#title
heading=Label(m,text="Search the files by entering the file names",font="arial 15 bold").grid(row=0,column=3)

#label
seachinput = Label(m,text="Enter the file name").grid(row=1,column=2)
extension = Label(m,text="Enter the ectension").grid(row=2,column=2)

#variable type
searchinputvalue = StringVar()
extensionvalue = StringVar()


#input entry
searchEntry = Entry(m,textvariable=searchinputvalue).grid(row=1,column=3)
extensionEntry = Entry(m,textvariable=extensionvalue).grid(row=2,column=3)


#search Button
name = Button(m,text="Open File",font="arial 10 bold",command=searchfile).grid(row=3,column=3)

#packing
m.mainloop()