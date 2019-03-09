Product_dictionary =	{
  "banana": 1.19,
  "ice": 2,
  "cereal": 3.19
}

banana_PLU = ("banana")
ice_PLU = ("ice")
cereal_PLU = ("cereal")
user_input = ("")
PLU_list = [banana_PLU, ice_PLU, cereal_PLU,]
sales_list = []
sales_list_dict = {}

#products variables, name and price
banana = float(1.2)
ice = float(2)
cereal = float(3.2)

from tkinter import *

from tkinter import messagebox

root = Tk()
root.title("CASH till operator")
root.geometry('800x600')
leftFrame = Frame(root)
leftFrame.pack(side=LEFT, expand=True, fill='both')
#rightFrame = Frame(root)         in case I need to add something on the right side like display??
#rightFrame.pack(side=RIGHT, expand=True, fill='both')

lbl = Label(leftFrame, text="Choose item", font=("Arial Bold", 40), bg="blue")
lbl.pack(expand=True,fill='both')

txt = Entry(leftFrame, width=10, bg="yellow", font=("Arial Bold", 40), fg="black")
txt.pack(expand=True,fill='both')


def off_sale():
    messagebox.showwarning('auto_finder', 'not found try again')
    return

def register():
    res =  txt.get()
    res2 = spin.get()
    if res == banana_PLU:
        sales_list.append(round(banana * float(res2), 2))
        lbl.configure(text= res2+" " "added to the basket")
    elif res == ice_PLU:
        sales_list.append(ice * float(res2))
        lbl.configure(text= res2+" " "added to the basket")
    elif res == cereal_PLU:
        sales_list.append(cereal * float(res2))
        lbl.configure(text= res2+" " "added to the basket")
    else:
        off_sale()

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

btn1 = Button(leftFrame, text="Add to the basket", font=("Arial Bold", 25), bg="blue", fg="black", command=register)
btn2 = Button(leftFrame, text="Void", font=("Arial Bold", 25), bg="blue", fg="black", command=void)
btn3 = Button(leftFrame, text="Subtotal", font=("Arial Bold", 25), bg="blue", fg="black", command=subtotal)
btn4 = Button(leftFrame, text="Total", font=("Arial Bold", 25), bg="blue", fg="black", command=total)
btn5 = Button(leftFrame, text="Reset", font=("Arial Bold", 25), bg="blue", fg="black", command=reset)

spin = Spinbox(leftFrame, values = (1, 2, 3, 4, 5, 6, 7, 8, 9 ), width=5, font=("Arial Bold", 25))
spin.pack(expand=True,fill='both')

btn1.pack(expand=True,fill='both')
btn2.pack(expand=True,fill='both')
btn3.pack(expand=True,fill='both')
btn4.pack(expand=True,fill='both')
btn5.pack(expand=True,fill='both')


root.mainloop()
