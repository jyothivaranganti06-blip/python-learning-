from tkinter import *
window=Tk()
window.title("calcutor")
window.geometry("300x500")
entry = Entry(window,width=20,font=("Arial",20), borderwidth=5)#entry creates a single-line text box
entry.grid(row=0,column=0,columnspan=4)

def click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,current+str(number))

def clear():
    entry.delete(0,END)
def calculate():
    expression=entry.get()
    try:
        result=eval(expression)
        entry.delete(0,END)
        entry.insert(0,result)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")

Button(window,text="7",width=5,height=2,command=lambda:
click(7)).grid(row=1,column=0)
Button(window,text="8",width="5",height=2,command=lambda:
click(8)).grid(row=1,column=1)
Button(window,text="9",width=5,height=2,command=lambda:
click(9)).grid(row=1,column=2)
Button(window,text="/",width=5,height=2,command=lambda:
click("/")).grid(row=1,column=3)

Button(window,text="4",width=5,height=2,command=lambda:
click(4)).grid(row=2,column=0)
Button(window,text="5",width=5,height=2,command=lambda:
click(5)).grid(row=2,column=1)
Button(window,text="6",width=5,height=2,command=lambda:
click(6)).grid(row=2,column=2)
Button(window,text="*",width=5,height=2,command=lambda:
click("*")).grid(row=2,column=3)

Button(window,text="1",width=5,height=2,command=lambda:
click(1)).grid(row=3,column=0)
Button(window,text="2",width=5,height=2,command=lambda:
click(2)).grid(row=3,column=1)
Button(window,text="3",width=5,height=2,command=lambda:
click(3)).grid(row=3,column=2)
Button(window,text="-",width=5,height=2,command=lambda:
click("-")).grid(row=3,column=3)

Button(window,text="0",width=5,height=2,command=lambda:
click(0)).grid(row=4,column=0)
Button(window,text=".",width=5,height=2,command=lambda:
click(".")).grid(row=4,column=1)
Button(window,text="=",width=5,height=2,command=calculate).grid(row=4,column=2)
Button(window,text="+",width=5,height=2,command=lambda:
click("+")).grid(row=4,column=3)

Button(window,text="Clear",width=24,height=2,command=clear).grid(row=5,column=0,columnspan=4)
window.mainloop()   