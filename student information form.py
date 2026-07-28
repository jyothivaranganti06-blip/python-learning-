from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("student information from")
window.geometry("300x500")
#function to run whrn submit button is clicked
def submit ():
    name=name_entry.get()
    age= age_entry.get()
    course=course_entry.get()
    messagebox.showinfo( "student details",f"Name:{name}\nAge:{age}\nCourse:{course}") 
#creates labels
Label(window,text="Name").grid(row=0,column=0,padx=10,pady=10)
Label(window,text="Age").grid(row=1,column=0,padx=10,pady=10)
Label(window,text="Course").grid(row=2,column=0,padx=10,pady=10)
#entry box text box 
name_entry=Entry(window,width=25)
name_entry.grid(row=0,column=1)

age_entry=Entry(window,width=25)
age_entry.grid(row=1,column=1)

course_entry=Entry(window,width=25)
course_entry.grid(row=2,column=1)

Button(window,text="submit",command=submit).grid(row=3,column=0,columnspan=2,pady=20)

window.mainloop()