import tkinter
from tkinter import *


root = Tk()
root.title('To-Do-List')
root.geometry("400x550+400+100")
root.resizable(False,False)


task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)


    if task:
        with open('C:/Users/suhas/OneDrive/Desktop/Image/tasklist.txt','a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('C:/Users/suhas/OneDrive/Desktop/Image/tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+ '\n')
        listbox.delete(ANCHOR)



def opentaskFile():

    try:
        
        with open('C:/Users/suhas/OneDrive/Desktop/Image/tasklist.txt','r')as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)


    except:
        file=open('tasklist.txt','w')
        file.close()

Image_icon = PhotoImage(file='C:/Users/suhas/OneDrive/Desktop/Image/checklist.png')
root.iconphoto(False, Image_icon)



frame2 = Frame(root, width=400, height=90, bg='silver')
frame2.place(x=0, y=0)

heading=Label(root, text='MY TODO LIST', font=('arial',25,'bold'), fg='black', bg='silver')
heading.place(x=90,y=20)


frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame, width=18, font='arial 20', bd=0)
task_entry.place(x=20,y=7)
task_entry.focus()


button = Button(frame, text='ADD',font='arial 20 bold',width=6, bg='grey', fg='black', bd=0, command=addTask)
button.place(x=300, y=0)


#ListBox

frame1 = Frame(root, bd=3, width=700, height=280, bg='grey')
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=('arial',12),width=40, height=16,bg='grey', fg='black', cursor='hand2', selectbackground='grey')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentaskFile()

#delete

Delete_icon = PhotoImage(file='C:/Users/suhas/OneDrive/Desktop/Image/sign-delete-icon.png')
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=5)



root.mainloop()
