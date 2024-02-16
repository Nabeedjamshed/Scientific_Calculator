from tkinter import *
from PIL import Image, ImageTk
import math
m = Tk()
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
m.geometry(f"{screen_width}x{screen_height}")
m.title("Scientific Calculator")

u_border = Frame(m,width=330,height=230,bg='black')
u_border.place(x=530,y=100)

upper_image = Image.open('upper image.png') 
new = upper_image.resize((120,40))
upper = ImageTk.PhotoImage(new)
img = Label(m, image=upper)
img.place(x=700,y=120)

ent = Entry(m, width=15,bg='#c0c0c0',font=('Arial',25))
ent.place(x=560,y=210)

def click(to_print):
    old = ent.get()
    ent.delete(0, END)
    ent.insert(0, old+to_print)
    return
def sc(event):
    key = event.widget
    text = key['text']
    no = ent.get()
    result = ''
    if text == 'sin':
        result = str(math.sin(float(no)))
    if text == 'cos':
        result = str(math.cos(float(no)))
    if text == 'tan':
        result = str(math.tan(float(no)))
    if text == 'ln':
        result = str(math.log(float(no)))
    if text == 'log':
        result = str(math.log10(float(no)))
    if text == '√':
        result = str(math.sqrt(float(no)))
    if text == 'x!':
        result = str(math.factorial(float(no))) 
    if text == 'x^-1':
        result = str(1/(float(no)))
    if text == 'pi':
        if no == "":
            result = str(math.pi)
        else:
            result = str(float(no) * math.pi)
    if text == 'EXP':
        if no == "":
            result = str(math.e)
        else:
            result = str(math.e**float(no))
    if text == 'x^2':
        result = str(float(no) ** 2)
    ent.delete(0, END)
    ent.insert(0, result)

def clear():
    ent.delete(0, END)
    return

def delete():
    current = ent.get()
    length = len(current)-1
    ent.delete(length, END)
def evaluate():
    ans = ent.get()
    ans = eval(ans)
    ent.delete(0, END)
    ent.insert(0, ans)


l_border = Frame(m, width=330,height=400,bg='grey')
l_border.place(x=530,y=290)

b1 = Button(m,text=0 ,width=5, height=2,bg='black',fg='white',command=lambda: click("0"))

b1.place(x=550,y=640)

b2 = Button(m,text='.' ,width=5, height=2,bg='black',fg='white',command=lambda: click("."))
b2.place(x=612,y=640)

b3 = Button(m,text='EXP' ,width=5, height=2,bg='black',fg='white')
b3.bind("<Button-1>", sc)
b3.place(x=672,y=640)

b4 = Button(m,text='Ans' ,width=5, height=2,bg='black',fg='white',command=evaluate)
b4.place(x=732,y=640)

b5 = Button(m,text='=' ,width=5, height=2,bg='black',fg='white',command=evaluate)
b5.place(x=792,y=640)

b6 = Button(m,text=1 ,width=5, height=2,bg='black',fg='white',command=lambda: click("1"))
b6.place(x=552,y=587)

b7 = Button(m,text=2 ,width=5, height=2,bg='black',fg='white',command=lambda: click("2"))
b7.place(x=612,y=587)

b8 = Button(m,text=3 ,width=5, height=2,bg='black',fg='white',command=lambda: click("3"))
b8.place(x=672,y=587)
b9 = Button(m,text='+' ,width=5, height=2,bg='black',fg='white',command=lambda: click("+"))
b9.place(x=732,y=587)

b10 = Button(m,text='-' ,width=5, height=2,bg='black',fg='white',command=lambda: click("-"))
b10.place(x=792,y=587)

b11 = Button(m,text=4 ,width=5, height=2,bg='black',fg='white',command=lambda: click("4"))
b11.place(x=552,y=534)

b12 = Button(m,text=5 ,width=5, height=2,bg='black',fg='white',command=lambda: click("5"))
b12.place(x=612,y=534)

b13 = Button(m,text=6 ,width=5, height=2,bg='black',fg='white',command=lambda: click("6"))
b13.place(x=672,y=534)

b14 = Button(m,text='x' ,width=5, height=2,bg='black',fg='white',command=lambda: click("x"))
b14.place(x=732,y=534)

b15 = Button(m,text='/' ,width=5, height=2,bg='black',fg='white',command=lambda: click("/"))
b15.place(x=792,y=534)

b16 = Button(m,text=7 ,width=5, height=2,bg='black',fg='white',command=lambda: click("7"))
b16.place(x=552,y=481)

b17 = Button(m,text=8 ,width=5, height=2,bg='black',fg='white',command=lambda: click("8"))
b17.place(x=612,y=481)

b18 = Button(m,text=9 ,width=5, height=2,bg='black',fg='white',command=lambda: click("9"))
b18.place(x=672,y=481)

b19 = Button(m,text='DEL' ,width=5, height=2,bg='blue',fg='white',command=delete)
b19.place(x=732,y=481)

b20 = Button(m,text='AC' ,width=5, height=2,bg='blue',fg='white',command=clear)
b20.place(x=792,y=481)

b21 = Button(m,text='RCL' ,width=4, height=1,bg='black',fg='white',command=lambda: click("RCL"))
b21.place(x=552,y=445)

b22 = Button(m,text='ENG' ,width=4, height=1,bg='black',fg='white',command=lambda: click("ENG"))
b22.place(x=602,y=445)

b23 = Button(m,text='(' ,width=4, height=1,bg='black',fg='white',command=lambda: click("("))
b23.place(x=652,y=445)

b24 = Button(m,text=')' ,width=4, height=1,bg='black',fg='white',command=lambda: click(")"))
b24.place(x=702,y=445)

b25 = Button(m,text=',' ,width=4, height=1,bg='black',fg='white',command=lambda: click(","))
b25.place(x=752,y=445)

b26 = Button(m,text='M+' ,width=4, height=1,bg='black',fg='white',command=lambda: click("M+"))
b26.place(x=802,y=445)

b27 = Button(m,text='(-)' ,width=4, height=1,bg='black',fg='white',command=lambda: click("(-)"))
b27.place(x=552,y=409)

b28 = Button(m,text='pi' ,width=4, height=1,bg='black',fg='white')
b28.bind("<Button-1>", sc)
b28.place(x=602,y=409)

b29 = Button(m,text='hyp' ,width=4, height=1,bg='black',fg='white',command=lambda: click("hyp"))
b29.place(x=652,y=409)

b30 = Button(m,text='sin' ,width=4, height=1,bg='black',fg='white')
b30.bind("<Button-1>", sc)
b30.place(x=702,y=409)

b31 = Button(m,text='cos' ,width=4, height=1,bg='black',fg='white')
b31.bind("<Button-1>", sc)
b31.place(x=752,y=409)

b32 = Button(m,text='tan' ,width=4, height=1,bg='black',fg='white')
b32.bind("<Button-1>", sc)
b32.place(x=802,y=409)

b33 = Button(m,text='ab/c' ,width=4, height=1,bg='black',fg='white',command=lambda: click("ab/c"))
b33.place(x=552,y=373)

b34 = Button(m,text='√' ,width=4, height=1,bg='black',fg='white')
b34.bind("<Button-1>", sc)
b34.place(x=602,y=373)

b35 = Button(m,text='x^2' ,width=4, height=1,bg='black',fg='white')
b35.bind("<Button-1>", sc)
b35.place(x=652,y=373)

b36 = Button(m,text='^' ,width=4, height=1,bg='black',fg='white',command=lambda: click("^"))
b36.place(x=702,y=373)

b37 = Button(m,text='log' ,width=4, height=1,bg='black',fg='white')
b37.bind("<Button-1>", sc)
b37.place(x=752,y=373)

b38 = Button(m,text='ln' ,width=4, height=1,bg='black',fg='white')
b38.bind("<Button-1>", sc)
b38.place(x=802,y=373)

b39 = Button(m,text='Replay' ,width=8, height=3,bg='black',fg='white',command=lambda: click("Replay"))
b39.place(x=665,y=300)

b40 =Button(m,text='x!' ,width=4, height=1,bg='black',fg='white')
b40.bind("<Button-1>", sc)
b40.place(x=552,y=337)
b41 = Button(m,text='∫d/dx' ,width=4, height=1,bg='black',fg='white')
b41.place(x=602,y=337)

b42 = Button(m,text='x^-1' ,width=4, height=1,bg='black',fg='white')
b42.bind("<Button-1>", sc)
b42.place(x=752,y=337)

b43 = Button(m,text='log₁₀' ,width=4, height=1,bg='black',fg='white')
b43.place(x=802,y=337)

b44 = Button(m,text='SHIFT' ,width=4, height=1,bg='black',fg='white')
b44.place(x=552,y=301)

b45 = Button(m,text='Alpha' ,width=4, height=1,bg='black',fg='white')
b45.place(x=602,y=301)

b46 = Button(m,text='MODE' ,width=4, height=1,bg='black',fg='white')
b46.place(x=752,y=301)

b47 = Button(m,text='ON' ,width=4, height=1,bg='blue',fg='white')
b47.place(x=802,y=301)

l = Label(m, text="Scientific Calculator", bg='black', fg='white',font=('Arial',35))
l.pack(side=TOP,fill=X)

py = Image.open("python-logo.png")
rez = py.resize((250,250))
n_py = ImageTk.PhotoImage(rez)
img1 = Label(m, image=n_py)
img1.place(x=100,y=320) 

py1 = Image.open("python-logo.png")
rez1 = py1.resize((250,250))
n_py1 = ImageTk.PhotoImage(rez1)
img2 = Label(m, image=n_py1)
img2.place(x=1000,y=320)

m.mainloop()