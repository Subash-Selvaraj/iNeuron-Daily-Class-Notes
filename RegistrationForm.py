from tkinter import *
root = Tk()
root.geometry("500x300")
#defining the function for the last message

def getvals():
   print("Form Registration has been Successfully!!!!")

#Heading
B = Label(root,text="Python Registration Form",font="arial 15 bold").grid(row=0,column=3)

#Field Name with packing
Name = Label(root,text="Name").grid(row=1,column=2)
Phone = Label(root,text="Phone").grid(row=2,column=2)
Gender = Label(root,text="Gender").grid(row=3,column=2)
Emergency = Label(root,text="Emergency").grid(row=4,column=2)
Paymentmethod = Label(root,text="Paymentmethod").grid(row=5,column=2)

# B.pack() #for packing will give the output of our input code or else we can mentions the particular row,column where ever our output should display(.grind(row=0,column=3)
# Name.pack()
# Phone.pack()
# Gender.pack()
# Emergency.pack()
# Paymentmethod.pack()

#variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar


#creating entry field with packaing
nameentry = Entry(root,textvariable=namevalue).grid(row=1,column=3)
phoneentry = Entry(root,textvariable=phonevalue).grid(row=2,column=3)
genderentry = Entry(root,textvariable=gendervalue).grid(row=3,column=3)
paymentmoodentry = Entry(root,textvariable=paymentmoodvalue).grid(row=4,column=3)
emergencyentry = Entry(root,textvariable=emergencyvalue).grid(row=5,column=3)


#Creating checkbox and packing
checkbutton = Checkbutton(text = 'Remember me?',variable = checkvalue).grid(row=6,column=3)


#Creating submitting button with packing
Button(text='Submit',command=getvals).grid(row=7,column=3)
root.mainloop()