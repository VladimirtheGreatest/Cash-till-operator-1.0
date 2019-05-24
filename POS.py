
from tkinter import *

from tkinter import messagebox
# noinspection PyUnresolvedReferences
from PIL import ImageTk, Image
import sys #Imports sys, used to end the program later

#Product Dictionary and variables

Product_dictionary =	{
  "banana": 1.2,
  "ice": 2,
  "cereal": 3.2
}

banana_PLU = ("banana")
ice_PLU = ("ice")
cereal_PLU = ("cereal")
user_input = ("")
PLU_list = [banana_PLU, ice_PLU, cereal_PLU,]
sales_list = []
sales_list_dict = {}

banana = float(1.2)
ice = float(2)
cereal = float(3.2)

#Functions (button commands)

def off_sale():
    messagebox.showwarning('auto_finder', 'not found try again')
    return

def subtotal():
    total_PLU = sum(sales_list)
    lbl.configure(text=round(total_PLU, 2))
    return total_PLU

def total():
    try:
        res = txt.get()
        change = float(res) - float(subtotal())
        if change >=0:
            lbl.configure(text=("%.2f" % round(change, 2), "change back to customer"))
            sales_list.clear()
        else:
            messagebox.showwarning('more money', 'you need more money')



    except:
        ValueError
        messagebox.showwarning("how much money?")
        pass


def void():
    try:
        res = txt.get()
        res2 = spin.get()
        if res == banana_PLU:
            sales_list.remove(banana * float(res2))
            lbl.configure(text=sales_list)
        elif res == cereal_PLU:
            sales_list.remove(cereal * float(res2))
            lbl.configure(text=sales_list)
        elif res == ice_PLU:
            sales_list.remove(ice * float(res2))
            lbl.configure(text=sales_list)
    except ValueError:
        messagebox.showwarning('auto_finder', 'not in the basket try again')
        pass

def quantity():
    spin.get()
    return

def reset():
    sales_list.clear()
    lbl.configure(text=sales_list)


def discount():
    res = sales_list[-1]
    res1 = (res / 2)
    sales_list.pop()
    sales_list.append(res1)
    lbl.configure(text=sales_list)

def logout():
    root.destroy()

def find():
    res = txt.get()
    if res in Product_dictionary:
        lbl.configure(text=Product_dictionary[res])
    else:
        messagebox.showwarning('Product not found')

def clear():
    txt.delete(first=0,last=100)

def register():
    res =  txt.get()
    res2 = spin.get()
    if res == banana_PLU:
        sales_list.append(round(banana * float(res2), 2))
        lbl.configure(text= sales_list)

    elif res == ice_PLU:
        sales_list.append(ice * float(res2))
        lbl.configure(text= sales_list)
    elif res == cereal_PLU:
        sales_list.append(cereal * float(res2))
        lbl.configure(text= sales_list)
    else:
        off_sale()


#Tkinter login and main menu

root=Tk() #Declares root as the tkinter main window
top = Toplevel() #Creates the toplevel window

entry1 = Entry(top) #Username entry
entry2 = Entry(top) #Password entry
button1 = Button(top, text="Login", command=lambda:command1()) #Login button
button2 = Button(top, text="Cancel", command=lambda:command2()) #Cancel button
root.title("CASH till operator")
root.geometry('800x600')
leftFrame = Frame(root)
leftFrame.pack(side=LEFT, expand=True, fill='both')
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, expand=True, fill='both')
img = ImageTk.PhotoImage(Image.open(r"C:\Users\Vladimir\Desktop\test.png"))
lbl = Label(leftFrame, text="Choose item", font=("Arial Bold", 40), bg="blue")
lbl.pack(expand=True,fill='both')
txt = Entry(leftFrame, width=10, bg="yellow", font=("Arial Bold", 40), fg="black")
txt.pack(expand=True,fill='both')
btn1 = Button(leftFrame, text="Add to the basket", font=("Arial Bold", 25), bg="blue", fg="black", command=register)
btn2 = Button(leftFrame, text="Void", font=("Arial Bold", 25), bg="blue", fg="black", command=void)
btn3 = Button(leftFrame, text="Subtotal", font=("Arial Bold", 25), bg="blue", fg="black", command=subtotal)
btn4 = Button(leftFrame, text="Total", font=("Arial Bold", 25), bg="blue", fg="black", command=total)
btn5 = Button(rightFrame, text="Reset", font=("Arial Bold", 25), bg="red", fg="black", command=reset)
btn7 = Button(rightFrame, text="Discount 50%", font=("Arial Bold", 25), bg="blue", fg="black", command=discount)
btn8 = Button(rightFrame, text="Find price", font=("Arial Bold", 25), bg="blue", fg="black", command=find)
btn9 = Button(rightFrame, text="Log out", font=("Arial Bold", 25), bg="blue", fg="black", command=logout)
btn10 = Button(rightFrame, image=img)
btn11 = Button(rightFrame, text="Clear", font=("Arial Bold", 25), bg="blue", fg="black", command=clear)

spin = Spinbox(leftFrame, values = (1, 2, 3, 4, 5, 6, 7, 8, 9 ), width=5, font=("Arial Bold", 25))
spin.pack(expand=True,fill='both')

btn1.pack(expand=True,fill='both')
btn2.pack(expand=True,fill='both')
btn3.pack(expand=True,fill='both')
btn4.pack(expand=True,fill='both')
btn5.pack(expand=True,fill='both')
btn7.pack(expand=True,fill='both')
btn8.pack(expand=True,fill='both')
btn9.pack(expand=True,fill='both')
btn10.pack(expand=True,fill='both')
btn11.pack(expand=True,fill='both')


#Functions login

def command1():
    if entry1.get() == "user" and entry2.get() == "password": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


entry1.pack() #These pack the elements, this includes the items for the main window
entry2.pack()
button1.pack()
button2.pack()


root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window
























