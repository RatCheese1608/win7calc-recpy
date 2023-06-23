import math
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# root
main = tk.Tk()
main.title('Funny Title')
main.geometry('390x520')
main.resizable(0,0)

# var
global disp, memor, ln, op
calcu = tk.StringVar()
memor = 0
ln, op='', 0

# functions
def inpt(n):
    dsn = disp.get()
    scn = float(dsn)
    if len(dsn) > 12:
        return
    disp.configure(state=tk.NORMAL)
    if float(dsn)==0:
        disp.delete(0,tk.END)
    disp.insert(tk.END, n)
    disp.configure(state=tk.DISABLED)

oprt={}
def mc():
    global memor
    memor=0
oprt['MC']=mc

def mr():
    global memor
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    disp.insert(0,memor)
    disp.configure(state=tk.DISABLED)
oprt['MR']=mr

def ms():
    global memor
    dsn = disp.get()
    memor=float(dsn)
    memor=memor if int(memor)!=memor else int(memor)
oprt['MS']=ms

def mp():
    global memor
    dsn = disp.get()
    memor+=float(dsn)
    memor=memor if int(memor)!=memor else int(memor)
oprt['M+']=mp

def mm():
    global memor
    dsn = disp.get()
    memor-=float(dsn)
    memor=memor if int(memor)!=memor else int(memor)
oprt['M-']=mm

def dl():
    disp.configure(state=tk.NORMAL)
    disp.delete(len(disp.get())-1,tk.END)
    if not disp.get():
        disp.insert(0,0)
    disp.configure(state=tk.DISABLED)
oprt['DEL']=dl

def ce():
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    disp.insert(0,0)
    disp.configure(state=tk.DISABLED)
oprt['CE']=ce

def cr():
    global ln, op
    ln=''
    op=0
    ce()
oprt['C']=cr

def pm():
    dsn = disp.get()
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    scn = -float(dsn)
    scn = scn if int(scn)!=scn else int(scn)
    disp.insert(0,scn)
    disp.configure(state=tk.DISABLED)
oprt['+/-']=pm

def sq():
    dsn = disp.get()
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    scn = math.sqrt(float(dsn))
    disp.insert(0,scn if int(scn)!=scn else int(scn))
    disp.configure(state=tk.DISABLED)
oprt['SQRT']=sq

def per():
    global ln
    dsn = disp.get()
    scn = float(dsn)
    if ln=='':
        return
    scn=ln*scn/100
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    disp.insert(0,scn if int(scn)!=scn else int(scn))
    disp.configure(state=tk.DISABLED)
oprt['%']=per

def ove():
    dsn = disp.get()
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    scn = 1/float(dsn)
    disp.insert(0,scn if int(scn)!=scn else int(scn))
    disp.configure(state=tk.DISABLED)
oprt['1/x']=ove

def equ():
    global ln, op
    dsn = disp.get()
    scn = float(dsn)
    if ln=='':
        return
    if op==1:
        scn=ln/scn
    elif op==2:
        scn=ln*scn
    elif op==3:
        scn=ln-scn
    elif op==4:
        scn=ln+scn
    else:
        return
    ln=scn
    op=0
    disp.configure(state=tk.NORMAL)
    disp.delete(0,tk.END)
    disp.insert(0,scn if int(scn)!=scn else int(scn))
    disp.configure(state=tk.DISABLED)
oprt['=']=equ

def div():
    global op, ln
    op=1
    dsn = disp.get()
    scn = float(dsn)
    ln = scn if int(scn)!=scn else int(scn)
    ce()
oprt['/']=div

def mul():
    global op, ln
    dsn = disp.get()
    scn = float(dsn)
    ln = scn if int(scn)!=scn else int(scn)
    ce()      
    op=2
oprt['*']=mul

def mnu():
    global op, ln
    op=3
    dsn = disp.get()
    scn = float(dsn)
    ln = scn if int(scn)!=scn else int(scn)
    ce()
oprt['-']=mnu

def add():
    global op, ln
    op=4
    dsn = disp.get()
    scn = float(dsn)
    ln = scn if int(scn)!=scn else int(scn)
    ce()
oprt['+']=add

def dot():
    dsn = disp.get()
    scn = float(dsn)
    if (int(scn)!=scn):
        return
    disp.configure(state=tk.NORMAL)
    disp.insert(tk.END,'.')
    disp.configure(state=tk.DISABLED)
oprt['.']=dot

# interface
intf = ttk.LabelFrame(main, text="Ray and Friends' Funny Calculator",
                      padding=10)
intf.grid(padx=10, pady=10, sticky='news')
main.rowconfigure(0, weight=1)
main.columnconfigure(0, weight=1)

## expression disp
disp = ttk.Entry(intf, textvariable=calcu, state=tk.DISABLED,
                 justify='right', font=('monospace', 24))
disp.grid(columnspan=5, sticky='news', pady=10)

## number input
ttk.Style().configure('inpt.TButton', font=('sans-serif',16))
numb = {}
r = 3
c = 2
for i in range(9,-1,-1):
    nb = ttk.Button(intf, text=str(i), style='inpt.TButton',
                    command=lambda n=i: inpt(n) )
    numb[i] = nb
    numb[i].grid(row=r, column=c, sticky='news', padx=2, pady=2)
    c -= 1
    if c<0:
        r+=1
        c=2
numb[0].grid_configure(column=0, columnspan=2)

## operator input
ttk.Style().configure('oper.TButton', font=('sans-serif',14))
oper = {}
cc=0
r=1
c=0
for i in ('MC', 'MR', 'MS', 'M+', 'M-', 'DEL', 'CE', 'C', 
          '+/-', 'SQRT', '/', '%', '*', '1/x', '-', '=', '+', '.'):
    ob = ttk.Button(intf, text=i, style='oper.TButton',
                    command=lambda n=i: oprt[n]())
    oper[i]=ob
    if cc<10:
        oper[i].grid(row=r, column=c%5, sticky='news', padx=2, pady=2)
        c+=1
        if not c%5:
            r+=1
    elif cc<17:
        oper[i].grid(row=r, column=c%2 +3, sticky='news', padx=2, pady=2)
        c+=1
        if not c%2:
            r+=1
    cc+=1
oper['.'].grid(row=6, column=2, sticky='news', padx=2, pady=2)
oper['='].grid_configure(rowspan=2)

# grid width and height
for i in range(7):
    intf.rowconfigure(i, weight=3)
intf.rowconfigure(0, weight=4)
for i in range(5):
    intf.columnconfigure(i, weight=2)
for i in range(3):
    intf.columnconfigure(i, weight=3)

# run it
disp.configure(state=tk.NORMAL)
disp.insert(0, 0)
disp.configure(state=tk.DISABLED)
main.mainloop()
