#file=open("student.txt","x") #creates a  new file
#file.close()

file=open("student.txt","r") 
file.close()

file=open("student.txt","w") 
print(file.write("hello there i'm a computer science student")) #writes in the created file
file.close() #if we again wrote the "w" code it erases all the previous data 

with open("student.txt")as file:
    print(file.read(5)) #get the word by its length

#reads the file 
file=open("student.txt","r")
print(file.read())
file.close()

file=open("student.txt","a")
print(file.write("\npursuing graduation" )) #append mode adds a data without removing previous one
file.close()

#read+write
file=open("student.txt","r+")
print(file.read())
file.write("\nsubjects\npython\nc\ndatabase")
file.close()

#write+read
#file=open("student.txt","w+")
#file.write("java") #removes all the previous data before entering new data
#file.seek(0)
#print(file.read())
#file.close()

#append+read
file=open("student.txt","a+")
file.write("\njava")
file.seek(0)
print(file.read())
file.close()

#reading files
file=open("student.txt","r")
print(file.read())
file.close()

#readline
file=open("student.txt","r")
print(file.readline())
file.close()

#readdlines
file=open("student.txt","r")
print(file.readlines())
file.close()

#writing files

#writelines()
#file=open("student.txt","w")
#file.write("r language\n")
#lines=["python\n","java\n","SQL\n"]
#file.writelines(lines)
#file.close()

#append data
file=open("student.txt","a")
file.write("\nmachine learning")
file.close()
#closing files
file.close()


#using with
#file=open("me.txt","x")     #creates a new file called me.txt
#file.close()

#with open("me.txt","r") as file:
     #print(file.read())  #it doesn't has close python automatically closes it 
#with open("me.txt","w") as file:
     #print(file.write("hii"))
#with open("me.txt","w") as file:
     #lines=["i'm a student\n","iam focusing on pyhton\n","currently learning file handling\n"]
     #print(file.writelines(lines))
#with open("me.txt","a") as file:
     #print(file.write("afterr that i will focus on DSA\n"))

# file pointer

#tell() tell returns the current position of the file pointer
file=open("student.txt","r")
print(file.tell()) 
file.close()

file=open("student.txt","r")
print(file.read(12))
print(file.tell())
file.close()

#seek  seek moves the file pointer to a specific position in the file
file=open("student.txt","r")
file.seek(0)
print(file.read())
file.close()

file=open("student.txt","r")
file.seek(12)
print(file.read())
file.close()

#tell and seek
file=open("student.txt","r")
print(file.tell())
file.seek(16)
print(file.tell())
print(file.read())
file.close()
file=open("student.txt","r")
print(file.read())
file.seek(0)
print(file.read())
file.close()
#check if the file exists
import os
print(os.path.exists("student.txt")) #true

#rename file
#import os
#os.rename("student1.txt","student.txt")

#delete file
#import os
#os.remove("me.txt")


#csv files  csv=comma seperated values
import csv
with open("students.csv","w",newline="") as  file:
     writer=csv.writer (file)
     writer.writerow(["Name","Age","Course"])
     writer.writerow(["james","20","computer science"])
     writer.writerow(["juhoon","18","physics"])
     writer.writerow(["martin","18","chemistry"])

#read a csv file
with open("students.csv","r") as file:
     reader=csv.reader(file)
     for row in reader:
          print(row)

#write multiple rows
import csv
with open("students.csv","w",newline="")as file:
     writer=csv.writer(file)
     writer.writerows([["name","age","course"],
                       ["pinky",20,"computer science"],
                       ["james",20,"computer science"],
                       ["rahul",22,"chemistry"]])
#append a new row
import csv
with open("students.csv","a",newline="")as file:
     writer=csv.writer(file) 
     writer.writerow(["juhoon",20,"commputer science"])

#read as dictionary
import csv
with open("students.csv","r")as file:
     reader=csv.DictReader(file)
     for row in reader:
          print(row)
#write using dictionary
#import csv
#with open("students.csv","w",newline="")as file:
    # fields=["name","age","course"]
    # writer=csv.DictWriter(file,fieldnames=fields)
     #writer.writeheader()
     #writer.writerow({
       #   "name":"james",
      #    "age":20,
     #     "course":"computer science"
    # })

#problems on csv
#create a csv file 
import csv
with open("employees.csv","w",newline="")as file:
     writer= csv.writer(file)
     writer.writerows([["name","age","department"],
     ["jennie",30,"IT"],
     ["mina",26,"HR"],
      ["jihyo",25,"IT"]])
#read and print all records
with open("employees.csv","r")as file:
     reader=csv.reader(file)
     for row in reader:
      print(row)
#append one new student 
with open("employees.csv","a")as file:
     writer=csv.writer(file)
     writer.writerow(["kazhua",25,"HR"])
#count the number of rows
#including header
import csv
count=0
with open("employees.csv","r")as file:
     reader=csv.reader(file)
     for row in reader:
      count+=1
print(count)
#excluding header
count=0
with open("employees.csv","r")as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        count+=1
print(count)

#intermediate
#search for a employee by name
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    name="mina"
    for row in reader:
        if row["name"]==name:
            print(row)
#print only students older than 25:
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if int(row["age"])>25:
         print(row)
#find the average age
total_age=0
count=0
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
     age=int(row["age"])
     total_age+=age
     count+=1
     avg=total_age/count
print(avg) 
#update  employee's department 
rows=[]
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    name="mina"
    new_department="IT"
    for row in reader:
        if row["name"]==name:
          row["department"]=new_department
        rows.append(row)
with open("employees.csv","w",newline="")as file:
    writer=csv.DictWriter(file,fieldnames=["name","age","department"])
    writer.writeheader()
    writer.writerows(rows)
#delete a employees record
rows=[]
name="jihyo"
with open("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["name"]!=name:
            rows.append(row)
with open("employees.csv","w",newline="")as file:
    writer=csv.DictWriter(file,fieldnames=["name","age","department"])
    writer.writeheader()
    writer.writerows(rows)
#advanced problems 
#student management system 

#creating new student management system
import csv
with open("student management system.csv","w",newline="")as file:
  writer=csv.writer(file)
  writer.writerows([["Name","Age","Course"],
      ["hassini",20,"computer science"],
                   ["harini",22,"history"],
                   ["pinky",20,"computer science"],
                   ["james",20,"physical science"]])
#view all students
import csv
with open("student management system.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

#search a student
with open ("student management system.csv","r")as file:
    name="james"
    reader=csv.DictReader(file)
    for row in reader:
        if row["Name"]==name:
            print(row)



#update a student's age
#rows=[]
#with open("student management system.csv","r")as file:
      #reader=csv.DictReader(file)
      #name=input("enter your name: ")
      #age=int(input("enter your age: "))
      #for row in reader:
     #     if row["Name"]==name:
    #          row["Age"]=age
   #           rows.append(row)
#with open("student management system.csv","w",newline="")as file:
    #writer=csv.DictWriter(file,fieldnames=["Name","Age","Course"])
    #writer.writeheader()
   # writer.writerows(rows)


#deleting student records
rows=[]
choice=input("DELETE BY: "
"(1.Name),"
"(2.Age),"
"(3.Course): ")
if choice=="1":
    value="harini"
    column="Name"
elif choice=="2":
    value=int(input("enter your age: "))
    column="Age"
elif choice=="3":
    value=input("enter your course:")
    column="Course"
else:
    print("invalid choice")
    exit()
with open("student management system.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row[column]!=value:
            rows.append(row)
with open("student management system.csv","w",newline="")as file:
    writer=csv.DictWriter(file,fieldnames=["Name","Age","Course"])
    writer.writeheader()
    writer.writerows(rows)
print("Deletion successfully completed")
     
#attendence management system
import csv
with open("attendence management system.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows([["Name","Date","Status"],
                      ["pinky","2026-07-23","present"],
                      ["james","2026-07-23","present"],
                      ["martin","2026-07-23","absent"],
                      ["ruba","2026-07-23","absent"]])  
    
#find all absent students
with open("attendence management system.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["Status"]=="absent":
            print(row)

#count present and absent students
present=0
absent=0
with open("attendence management system.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["Status"]=="absent":
            absent+=1
        if row["Status"]=="present":
            present+=1
    print(present)
    print(absent) 

#employee payroll system
with open("employees payroll.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows([["Name","Salary"],
                      ["james",90000],
                      ["martin",80000],
                      ["juhoon",70000],
                      ["keonho",60000],
                      ["harini",50000]])
    
#highest salary
highest=0
with open("employees payroll.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        salary=int(row["Salary"])
        if salary>highest:
            highest=salary
            name=row["Name"]
    print("highest salary: ",highest)
    print("name: ",name)

#smallest salary
smallest=float("inf")
with open("employees payroll.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        salary=int(row["Salary"])
        if salary<smallest:
            smallest= salary
            name=row["Name"]
    print("smallest salary: ",smallest)
    print("name:",name)

#calaculate average salary
total_salary=0
count=0
with open("employees payroll.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        salary=int(row["Salary"])
        total_salary+=salary
        count+=1
        avg=total_salary/count
    print("average salary:",avg)
    #total salary
    print("total salary: ",total_salary)

#library management system






