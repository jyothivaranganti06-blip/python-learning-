from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("login page")
window.geometry("400x300")

window.configure(bg="lightblue")

def login():
    user=user_entry.get()
    password=password_entry.get()
    messagebox.showinfo("user details",f"Name:{user}\nPassword:{password}")

Label(window,text="username",fg="black",font=("Arial",12)).grid(row=0,column=0)
Label(window,text="password",font=("Arial",12)).grid(row=1,column=0)

user_entry=Entry(window,width=25)
user_entry.grid(row=0,column=1,padx=10,pady=10)

password_entry=Entry(window,width=25)
password_entry.grid(row=1,column=1,padx=10,pady=10)

Button(window,text="Login",command=login,bg="lightblue",fg="black",font=("Arial",12),activebackground="darkblue",activeforeground="black").grid(row=2,column=1)

window.mainloop()