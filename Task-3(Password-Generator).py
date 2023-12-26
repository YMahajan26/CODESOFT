# Random Password Generator
import random
from tkinter import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pwd():
    try:
        n_letters = int(letters_entry.get())
        n_symbols = int(symbols_entry.get())
        n_numbers = int(numbers_entry.get())
    except ValueError:
        messagebox.showinfo(title="Oops",
                            message="Invalid input. Please enter non-negative values or don't leave any field blank.")
    else:
        pwd_entry.delete(0,'end')
        if n_letters <= 0 and n_symbols <= 0 and n_numbers <= 0 :
            messagebox.showinfo(title="Oops",
                                message="Invalid input. Please enter non-negative values or don't leave any field blank.")
            letters_entry.delete(0,'end')
            symbols_entry.delete(0,'end')
            numbers_entry.delete(0,'end')

    password_list = []
    for i in range(0, n_letters):
        password_list.append(random.choice(letters))
    for i in range(0, n_numbers):
        password_list.append(random.choice(numbers))
    for i in range(0, n_symbols):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    pwd = "".join(password_list)
    pwd_entry.insert(0,f"{pwd}")


FONT = ('Constantia',20,'italic','bold')
FONT2 = ('Constantia',13,'italic')
B_FONT = ('Constantia',15,'normal')
W_BG = 'light steel blue'
B_BG = 'light steel blue4'
FG = 'Black'

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50,background=W_BG)

label1=Label(text="WELCOME \nTO\n PASSWORD GENERATOR",font=FONT,background=W_BG)
label1.grid(row=0,column=0,columnspan =2,pady=10)

letters_label = Label(text="How many letters would you like in your password ?",font=FONT2,background=W_BG)
letters_label.grid(row=1,column=0,padx=10,pady=10)
letters_entry = Entry(justify='center')
letters_entry.grid(row=1,column=1,padx=10,pady=10)

symbols_label = Label(text="How many symbols would you like in your password ?",font=FONT2,background=W_BG)
symbols_label.grid(row=2,column=0,padx=10,pady=10)
symbols_entry = Entry(justify='center')
symbols_entry.grid(row=2,column=1,padx=10,pady=10)

numbers_label = Label(text="How many numbers would you like in your password ?",font=FONT2,background=W_BG)
numbers_label.grid(row=3,column=0,padx=10,pady=10)
numbers_entry = Entry(justify='center')
numbers_entry.grid(row=3,column=1,padx=10,pady=10)

generate_button =Button(text="Generate Password",command=generate_pwd,font=B_FONT,background=B_BG,fg='white')
generate_button.grid(row=4,column=0,columnspan =2,padx=10,pady=10)

pwd_label =Label(text="Your random Password is : ",font=FONT2,background=W_BG)
pwd_label.grid(row=5,column=0,padx=10,pady=10)
pwd_entry = Entry(width=18,justify='center',font=B_FONT)
pwd_entry.grid(row=5,column=1,padx=10,pady=10)

window.mainloop()

