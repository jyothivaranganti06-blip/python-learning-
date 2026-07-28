from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("employee salary calculator")
window.geometry("300x500")

def calculate():
    employee=employee_entry.get()
    salary=float(salary_entry.get())
    bonus=float(bonus_entry.get())
    total=salary+bonus 
    messagebox.showinfo("employee details ",f"Employee:{employee}\nSalary:{salary}\nBonus:{bonus}\nTotal:{total}")


Label(window,text="employee name").grid(row=0,column=0,padx=10,pady=10)
Label(window,text="Salary").grid(row=1,column=0,padx=10,pady=10)
Label(window,text="Bonus").grid(row=2,column=0,padx=10,pady=10)
Label(window,text="Total").grid(row=3,column=0,padx=10,pady=10)

employee_entry=Entry(window,width=25)
employee_entry.grid(row=0,column=1)

salary_entry=Entry(window,width=25)
salary_entry.grid(row=1,column=1)

bonus_entry=Entry(window,width=25)
bonus_entry.grid(row=2,column=1)

Button(window,text="calculate",command=calculate).grid(row=4,column=0,columnspan=3,pady=20)

window.mainloop()