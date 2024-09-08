from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("calculator")
root.geometry('550x625')
root.resizable(0,0)
place = 0
place1 = 0
counter = 0
reverse = ''
p = 0
p1 = 0
def n1():
    global place
    global place1
    if place < 48:
        e1.insert(place, '1')
        place += 1
    elif 48<= place< 96 :
        e2.insert(place1, '1')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n2():
    global place
    global place1
    if place < 48:
        e1.insert(place, '2')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '2')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n3():
    global place
    global place1
    if place < 48:
        e1.insert(place, '3')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '3')
        place1 += 1 
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n4():
    global place
    global place1
    if place < 48:
        e1.insert(place, '4')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '4')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n5():
    global place
    global place1
    if place < 48:
        e1.insert(place, '5')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '5')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n6():
    global place
    global place1
    if place < 48:
        e1.insert(place, '6')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '6')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n7():
    global place
    global place1
    if place < 48:
        e1.insert(place, '7')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '7')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n8():
    global place
    global place1
    if place < 48:
        e1.insert(place, '8')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '8')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n9():
    global place
    global place1
    if place < 48:
        e1.insert(place, '9')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '9')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def n0():
    global place
    global place1
    if place < 48:
        e1.insert(place, '0')
        place += 1
    elif 48<= place< 96      :
        e2.insert(place1, '0')
        place1 += 1
        place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def np():
    global place 
    global place1
    global counter
    text2 = e1.get()
    text3 = e2.get()
    text2 = ' '.join(text2)
    text2 = text2.split()
    text3 = ' '.join(text3)
    text3 = text3.split()
    text3.insert(0, 0)
    text2.insert(0, 0)
    if place < 48:
        if text2[place]== '+' or text2[place]== '-' or text2[place]== '/' or  text2[place ]== '*':
            e1.insert(place, '(')
            place +=1
            counter += 1
        elif counter == 0:
            e1.insert(place, '(')
            place +=1
            counter += 1

        elif counter > 0:     
            e1.insert(place, ')')
            place +=1
            counter -=1

    elif 48<= place< 96     :
        if place == 48 and(text2[place - 1]== '+' or text2[place - 1]== '-' or text2[place - 1]== '/' or  text2[place - 1]== '*'):
                e2.insert(place1, '(')
                counter += 1
                place += 1
                place1 += 1
                text3.remove(0)
        elif text3[place1 ]== '+' or text3[place1 ]== '-' or text3[place1 ]== '/' or  text3[place1]== '*':    
            place1 += 1
            e2.insert(place1, '(')
            counter += 1
            place +=1
            text3.remove(0)
        elif counter == 0:
            e2.insert(place1, '(')
            place1 +=1
            counter += 1
            place +=1 
            text3.remove(0)
        elif counter > 0:     
            e2.insert(place1, ')')
            place1 +=1
            counter -=1
            place +=1
            text3.remove(0)
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nj():
    global place
    global place1
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    text1.insert(0, 0)
    if place < 48:
        if place == 0 or text[place - 1]== '(':
            pass
        elif more == '**(':
            e1.delete(place-3,place)
            e1.insert(place-3, '+') 
            place -= 2
        elif text[place - 1]== '+' or text[place - 1]== '-' or text[place - 1]== '/' or  text[place - 1]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '+')
        else:  
            e1.insert(place, '+')
            place += 1
    elif 48<= place< 95      :
        if text1[place1]== '(':
            pass
        elif more1 == '**(':
            e2.delete(place1-3,place1)
            e2.insert(place1-3, '+') 
            place1 -= 2
            place 
        elif text1[place1]== '+' or text1[place1]== '-' or text1[place1]== '/' or  text1[place1 ]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '+')
        else:  
            e2.insert(place1, '+')
            place1 += 1
            place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nm():
    global place
    global place1
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    text1.insert(0, 0)
    text.insert(0, 0)
    if place < 48:
        if text[place ]== '+' or text[place ]== '-' or text[place ]== '/' or  text[place ]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '-')
        else:  
            e1.insert(place, '-')
            place += 1
    elif 48<= place< 95      :
        if text1[place1]== '+' or text1[place1 ]== '-' or text1[place1 ]== '/' or  text1[place1]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '-')
        else:  
            e2.insert(place1, '-')
            place1 += 1
            place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')            
def nz():
    global place
    global place1
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    text1.insert(0, 0)
    if place < 48:
        if place == 0 or text[place - 1]== '(':
            pass
        elif more == '**(':
            e1.delete(place-3,place)
            e1.insert(place-3, '*') 
            place -= 2
        elif text[place - 1]== '+' or text[place - 1]== '-' or text[place - 1]== '/' or  text[place - 1]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '*')
        else:  
            e1.insert(place, '*')
            place += 1
    elif 48<= place< 95      :
        if text1[place1]== '(':
            pass
        elif more1 == '**(':
            e2.delete(place1-3,place1)
            e2.insert(place1-3, '*') 
            place1 -= 2
            place -=2
        elif text1[place1]== '+' or text1[place1]== '-' or text1[place1 ]== '/' or  text1[place1]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '*')
        else:  
            e2.insert(place1, '*')
            place1 += 1
            place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nt():
    global place
    global place1
    global counter
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    text1.insert(0, 0)
    if place < 46:
        if place == 0 or text[place - 1]== '(':
            pass
        elif more == '**(':
            e1.delete(place-3,place)
            e1.insert(place-3, '**(')
            counter += 1
        elif text[place - 1]== '+' or text[place - 1]== '-' or text[place - 1]== '/' or  text[place - 1]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '**(')
            place += 2
            counter += 1
        else:  
            e1.insert(place, '**(')
            place += 3
            counter += 1
    elif 48<= place< 93      :
        if text1[place1 - 1]== '(':
            pass
        elif more1 == '**(':
            e2.delete(place1-3,place1)
            e2.insert(place1-3, '**(')
            counter += 1
        elif text1[place1]== '+' or text1[place1 ]== '-' or text1[place1 ]== '/' or  text1[place1]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '**(')
            place1 += 2
            place +=2
            counter += 1
        else:  
            e2.insert(place1, '**(')
            place1 += 3
            place +=3
            counter += 1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nta():
    global place
    global place1
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    text1.insert(0, 0)
    if place < 48:
        if place == 0 or text[place - 1]== '(':
            pass
        elif more == '**(':
            e1.delete(place-3,place)
            e1.insert(place-3, '/') 
            place -= 2
        elif text[place - 1]== '+' or text[place - 1]== '-' or text[place - 1]== '/' or  text[place - 1]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '/')
        else:  
            e1.insert(place, '/')
            place += 1
    elif 48<= place< 95      :
        if text1[place1 ]== '(':
            pass
        elif more1 == '**(':
            e2.delete(place1-3,place1)
            e2.insert(place1-3, '/') 
            place1 -= 2
            place -= 2
        elif text1[place1 ]== '+' or text1[place1 ]== '-' or text1[place1 ]== '/' or  text1[place1]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '/')
        else:  
            e2.insert(place1, '/')
            place1 += 1
            place +=1
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nc():
    global place
    global place1
    global counter
    e1.delete(0,END)
    e2.delete(0,END)
    place = 0
    place1 = 0
    counter = 0
def nd():
    global place
    global place1
    global counter
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    more2 =''.join(text[place -7 : place])
    more3 =''.join(text1[place1 -7 : place1])
    text.insert(0, 0)
    text1.insert(0, 0)
    if 1<=place <=48 :
        if more == '**(':
            e1.delete(place -3,place)
            place -= 3
            counter -= 1
        elif more2 == '**(1/2)':
            e1.delete(place-7,place)
            place -= 7
        elif text[place] == '(':
            counter -= 1
            place -= 1
            e1.delete(place,place+1)
        elif text[place] == ')':
            counter += 1
            place -= 1
            e1.delete(place,place+1)
        else:
            place -= 1
            e1.delete(place,place+1)
    elif place == 1:
        e1.delete(0,END)
        place = 0
    elif 48<place<=96:
        if more1 == '**(':
            e2.delete(place1 -3,place1)
            place -= 3
            place1 -= 3
            counter -= 1
        elif more3 == '**(1/2)':
            e2.delete(place1-7,place1)
            place -= 7
            place1 -= 7
        elif text1[place1] == '(':
            counter -= 1
            place1 -= 1
            place -= 1
            e2.delete(place1,place1+1)
        elif text1[place1] == ')':
            counter += 1
            place1 -= 1
            place -= 1
            e2.delete(place1,place1+1)
        else:
            place -= 1
            place1 -= 1
            e2.delete(place1,place1+1)
    elif place == 49:
        if more1 == '**(':
            e2.delete(place1 -3,place1)
            place -= 3
            place1 -= 3
        else:
            e2.delete(0,END)
            place -= 1
            place1 = 0
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nra():
    global place
    global place1
    global counter
    text = e1.get()
    text = ' '.join(text)
    text = text.split()
    more =''.join(text[place -3 : place])
    text1 = e2.get()
    text1 = ' '.join(text1)
    text1 = text1.split()
    more1 =''.join(text1[place1 -3 : place1])
    more2 =''.join(text[place -7 : place])
    more3 =''.join(text1[place1 -7 : place1])
    text1.insert(0, 0)
    if place < 42:
        if place == 0 or text[place - 1]== '(':
            pass
        elif more == '**(':
            e1.delete(place-3,place)
            e1.insert(place-3, '**(1/2)')
            place += 4
        elif more2 == '**(1/2)':
            e1.delete(place-7,place)
            e1.insert(place-7, '**(1/2)')
        elif text[place - 1]== '+' or text[place - 1]== '-' or text[place - 1]== '/' or  text[place - 1]== '*':
            e1.delete(place-1,place)
            e1.insert(place, '**(1/2)')
            place += 6
        else:  
            e1.insert(place, '**(1/2)')
            place += 7
    elif 48<= place< 90      :
        if text1[place1 - 1]== '(':
            pass
        elif more3 == '**(1/2)':
            e2.delete(place1-7,place1)
            e2.insert(place1-7, '**(1/2)')
        elif more1 == '**(':
            e2.delete(place1-3,place1)
            e2.insert(place1-3, '**(1/2)')
            place += 4
        elif text1[place1]== '+' or text1[place1 ]== '-' or text1[place1 ]== '/' or  text1[place1]== '*':
            e2.delete(place1-1,place1)
            e2.insert(place1, '**(1/2)')
            place1 += 6
            place +=6
        else:  
            e2.insert(place1, '**(1/2)')
            place1 += 7
            place +=7
    else:
        messagebox.showerror('ERROR','you cant add any other number')
def nresult():
    global place
    global place1
    global counter
    global reverse
    global p
    global p1
    p += place
    p1 += place1
    try:
        place = 0
        place1 = 0
        text = e1.get()
        text1 = e2.get()
        textf = text + text1
        textf += counter * ')'
        counter = 0
        result = str(eval(textf))
        e1.delete(0,END)
        e2.delete(0,END)
        reverse = 0
        reverse = result
        if len(result)< 48:
            e1.insert(0,result)
            place += len(result) 
            b21.config(text=result)
        elif 48<=len(result)<96:
            e1.insert(0, result[0:47])
            e2.insert(0, result[47:95])
            place = len(result)+1
            place1 = len(result)-47
        if 48 <= len(result) < 64:                
            b21.config(text=result,font='Ariel 12 bold')
        if 64<= len(result)<80:
            b21.config(text=result,font='Ariel 10 bold')
        if 80 <= len(result)<96:
            b21.config(text=result,font='Ariel 7 bold')
        if len(result)>=96:
            messagebox.showinfo('long answer',f'{result}')
    except:
        place += p
        place1 += p1
def nrev():
    global place
    global place1
    global counter
    global reverse
    place = 0
    place1 = 0
    counter = 0
    e1.delete(0,END)
    e2.delete(0,END)
    if len(reverse)< 48:
        e1.insert(0,reverse)
        place = len(reverse)
    elif 48<=len(reverse)<=96:
        e1.insert(0, reverse[0:47])
        e2.insert(0, reverse[47:95])
        place = len(reverse)+1
        place1 = len(reverse) -47
    
    
                    
    
    
        

        
        
    
        
        
        
        
    
e1 = Entry(root,bg = 'white', fg = "black" ,border = 2, width = 11,font='Ariel 15 bold')
e1.place(x = 5, y = 75,height=50,width=540)
e2 = Entry(root,bg = 'white', fg = "black",border = 2, width = 11,font='Ariel 15 bold')
e2.place(x = 5, y = 130,height=50,width=540)
b1 = Button(root,text='1',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold' ,border=5,cursor='spider',command=n1)
b1.place(x = 29, y= 209,height=75,width=75)
b2= Button(root,text='2',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n2)
b2.place(x = 133, y= 209,height=75,width=75)
b3 = Button(root,text='3',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n3)
b3.place(x = 237, y= 209,height=75,width=75)
b4= Button(root,text='()',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=np)
b4.place(x = 341, y= 209,height=75,width=75)
b5= Button(root,text='d',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nd)
b5.place(x = 445, y= 209,height=75,width=75)
b6= Button(root,text='4',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n4)
b6.place(x = 29, y= 313,height=75,width=75)
b7= Button(root,text='5',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n5)
b7.place(x = 133, y= 313,height=75,width=75)
b8= Button(root,text='6',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n6)
b8.place(x = 237, y= 313,height=75,width=75)
b9= Button(root,text='-',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nm)
b9.place(x = 341, y= 313,height=75,width=75)
b10= Button(root,text='r',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command =nra)
b10.place(x = 445, y= 313,height=75,width=75)
b11= Button(root,text='7',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n7)
b11.place(x = 29, y= 417,height=75,width=75)
b12= Button(root,text='8',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n8)
b12.place(x = 133, y= 417,height=75,width=75)
b13= Button(root,text='9',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n9)
b13.place(x = 237, y= 417,height=75,width=75)
b14= Button(root,text='x',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nz)
b14.place(x = 341, y= 417,height=75,width=75)
b15= Button(root,text='xx',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nt)
b15.place(x = 445, y= 417,height=75,width=75)
b16= Button(root,text='0',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=n0)
b16.place(x = 29, y= 521,height=75,width=75)
b17= Button(root,text='+',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nj)
b17.place(x = 133, y= 521,height=75,width=75)
b18= Button(root,text='/',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command=nta)
b18.place(x = 237, y= 521,height=75,width=75)
b19= Button(root,text='=',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider',command = nresult)
b19.place(x = 341, y= 521,height=75,width=75)
b20= Button(root,text='c',bg = '#C0C0C0', fg = 'black',font='Ariel 35 bold',border=5,cursor='spider', command=nc)
b20.place(x = 445, y= 521,height=75,width=75)
b21= Button(root,text='',bg = 'white', fg = "black" , width = 11,font='Ariel 15 bold',border=5,cursor='spider', command = nrev)
b21.place(x = 5, y = 5,height=65,width=540)








root.mainloop()