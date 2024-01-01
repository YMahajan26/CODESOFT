# To-do list 
from  tkinter import *
import tkinter.messagebox

def addtask():
    def add():
        input_text = entry_task.get(1.0, "end")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text!!")
            add_window.destroy()
        else:
            listbox_task.insert(END, f"  {input_text}")
            add_window.destroy()

    add_window = Tk()
    add_window.title("Add task")
    add_window.config()
    entry_task = Text(add_window, width=40, height=4 ,font=T_FONT)
    entry_task.pack(padx=10,pady=10)
    button_temp = Button(add_window, text="Add task", command=add,bg=B_BG ,font=B_FONT)
    button_temp.pack()
    add_window.mainloop()


def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + " ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# ========================UI===========================

W_BG = "#ECF4D6"
F_BG = "#9AD0C2"
B_BG = "#2D9596"
B_FONT = ("Helvetica",12,"italic")
T_FONT = ("Helvetica",14)
T_BG = "#163020"

window=Tk()
window.title("To-Do List ")
window.config(bg=F_BG,padx=60,pady=20)

img = PhotoImage(file="todo2.png")
canvas = Canvas(width=500 , height=140,highlightthickness=0,bg=F_BG)
canvas.create_image(250,70,image = img)
canvas.pack()

#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack(padx=2,pady=20)

listbox_task=Listbox(frame_task,bg=W_BG,fg=T_BG,height=15,width=50,font = T_FONT)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


#Button
entry_button=Button(window,text="Add task",width=40,command=addtask,bg=B_BG,font=B_FONT)
entry_button.pack(padx=5,pady=10)

delete_button=Button(window,text="Delete selected task",width=40,command=deletetask,bg=B_BG,font=B_FONT)
delete_button.pack(padx=5,pady=5)

mark_button=Button(window,text="Mark as completed ",width=40,command=markcompleted,bg=B_BG,font=B_FONT)
mark_button.pack(padx=5,pady=10)

window.mainloop()
