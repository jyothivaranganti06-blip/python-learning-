from tkinter import *

window=Tk()
window.title("profile card")
window.geometry("500x700")
Label(window,text="profile",font=("Arial",17),bg="red",fg="black").grid(row=0,column=3,padx=10,pady=70)
Photo=PhotoImage(file="paint.png")
Label(window,text="Name: V.Jyothi",bg="pink",font=("Arial",15)).grid(row=1,column=3,padx=10,pady=10)
Label(window,text="Role: Student",bg="pink",font=("Arial",15)).grid(row=2,column=3,padx=10,pady=10)
window.mainloop()