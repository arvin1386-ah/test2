from tkinter import *
from tkinter import messagebox
from class_databace import Database
root = Tk()
root.title('')
root.geometry('575x450')
root.resizable(0,0)

bd=Database('d:\Python6.db')


s= Scrollbar(root, bg= 'red',)
s.place(x =5, y = 125, height=200)

def select(event):
    try:
        global selected
        global index
        index = lb.curselection()
        selected = lb.get(index)
        selected=selected.split()
        e1.delete(0,END)
        e1.insert(END,selected[1])
        e2.delete(0,END)
        e2.insert(END,selected[2])
        e3.delete(0,END)
        e3.insert(END,selected[3])
        e4.delete(0,END)
        e4.insert(END,selected[4])
    except IndexError:
        pass

lb= Listbox(root,yscrollcommand=s.set,borderwidth=10)
lb.place(x= 25, y=125,width=525,height=200)
s.config(command=lb.yview)
lb.bind('<<ListboxSelect>>',select)
# for i in range(1,21):
#     lb.insert(END, i)

def bring_back():
    bg=bd.fetch()
    return bg
r2=bring_back()
 
for i in r2:
    lb.insert(END, f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}')
def delete(): 
    bd.remove(selected[0])
    clear()
    lb.delete(index)
def add():
    if e1.get()==''or e2.get()==''or e3.get()==''or e4.get()=='':
        messagebox.showerror('ERROR','please enter everything completely')
        return
    try:
        int(e4.get())
    except:
        messagebox.showerror('ERROR','invalid phone number')
        return
    bd.insert(e1.get(), e2.get(), e3.get(), e4.get())
    es =f'{e1.get()} {e2.get()} {e3.get()} {e4.get()}'
    lb.insert(0,es)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
def exit1 ():
    root.destroy()

l1= Label(root,text = 'Fname:')
l1.place(x=25,y=25,width=50)
l2= Label(root,text = 'Lname:')
l2.place(x=300,y=25,width=50)
l3= Label(root,text = 'Address:')
l3.place(x=25,y=75, width=50)
l4= Label(root,text = 'Phone:')
l4.place(x=300,y=75,width=50)
e1 = Entry(root,bg = 'white', fg = "black",border = 2)
e1.place(x = 75, y = 25,height=25,width=200)
e2 = Entry(root,bg = 'white', fg = "black",border = 2)
e2.place(x = 350, y = 25,height=25,width=200)
e3 = Entry(root,bg = 'white', fg = "black",border = 2)
e3.place(x = 75, y = 75,height=25,width=200)
e4 = Entry(root,bg = 'white', fg = "black",border = 2)
e4.place(x = 350, y = 75,height=25,width=200)
e5 = Entry(root,bg = 'white', fg = "black",border = 2,font='Ariel 10 bold')
e5.place(x = 162.5, y = 390,height=25,width=250)
b1 = Button(root,text='insert',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold ',border=3,cursor='spider',command=add)
b1.place(x = 25, y= 335,width=112.5)
b2 = Button(root,text='clear',bg = '#C0C0C0', fg = 'black' ,font='Ariel 10 bold',border=3,cursor='spider',command=clear)
b2.place(x =162.5, y= 335,width=112.5)
b3 = Button(root,text='delete',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=delete)
b3.place(x = 300, y= 335,width=112.5)
b4 = Button(root,text='update',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',)
b4.place(x = 432.5, y= 335,width=112.5)
b5 = Button(root,text='search:',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',)
b5.place(x = 25, y= 385,width=112.5)
b6 = Button(root,text='exit',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=exit1)
b6.place(x = 432.5, y= 385,width=112.5)










root.mainloop()