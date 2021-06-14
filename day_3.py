from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Registration Form')
window.geometry("400x400")
window.configure(background = "grey94")

Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Gender = Label(window,text="Gender").grid(row = 2, column = 0)
var = IntVar()
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 4,column = 0)
Address = Label(window,text = "Address").grid(row =5, column =0)
City = Label(window,text = "City").grid(row = 6, column = 0)
State = Label(window,text = "State").grid(row = 7, column = 0)
Pincode = Label(window,text = "Pincode").grid(row = 8, column = 0)
Country = Label(window,text = "Country").grid(row = 9, column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Radiobutton(window, text = "Male",variable = var, value = 1).grid(row = 2,column = 1)
Radiobutton(window, text ="Female",variable = var, value = 2).grid(row = 2,column = 2)
Mobile1 = Entry(window).grid(row = 3,column = 1)
Email1 = Entry(window).grid(row = 4,column = 1)
Address1 = Entry(window).grid(row = 5, column = 1)
City1 = Entry(window).grid(row = 6, column =1)
State1 = Entry(window).grid(row = 7, column = 1)
Pincode1 = Entry(window).grid(row = 8, column = 1)
Country = Entry(window).grid(row = 9, column = 1)


def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text = res)
btn = ttk.Button(window ,text = "Submit").grid(row = 10,column = 0)
window.mainloop()
