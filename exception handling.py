#exception handling allows us to handle the error and continue the program

#try and except
try:
    number=int(input("enter thr number: "))
    print(number)
except:
    print("please enter a valid number")

#specific exceptions
#valueError

try:
    age=int(input("enter the age :"))
    print(age)
except ValueError:
    print("Age must be number")

#ZeroDivisonError

try:
    a=10
    b=0
    result=a/b
except ZeroDivisionError:
    print("cannot divide by Zero")

#IndexError

numbers=[10,20,30]
try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")

#KeyError
student={"name": "jyothi","age":20}
try:
    print(student["marks"])
except KeyError:
    print("marks key does not exist")

#type error
a=10
try:
    print(a+"hello")
except TypeError:
    print("cannot add integer and string")

#else : else runs only when there is no error

try:
    number=int(input("enter the number:"))
except ValueError:
    print("invalid number")
else:
    print("number: ",number)

#finally : finally runs whether there is an error or not 
try:
    number=int(input("enter number: "))
except ValueError:
    print("invalid number")
finally:
    print("program finished")


#calculator
def calculator():
    try:
        num1=int(input("enter the number: "))
        num2=int(input("enter the number: "))
        operator=input("choose the operator(+,-,*,/): ")
        if operator=='+':
            return num1+num2
        elif operator=='-':
            return num1-num2
        elif operator=="*":
            return num1*num2
        else:
            return num1/num2
    except ValueError:
        print("invalid number")
    except ZeroDivisionError:
        print("cannot divided by zero")
    finally:
        print("Done")
result=calculator()
print("Result:",result)

#ouside a function
try:
    age=int(input("enter your age: "))
except ValueError:
    print("please enter a number")

#inside function
def get_age():
    try:
        age=int(input("enter age: "))
        return age
    except ValueError:
        print(" please enter a valid age! ")
get_age()

#inside loops
while True:
    try:
      number=int(input("enter the number: "))
      break
    except ValueError:
        print("invalid input")

#inside conditions or other code
numbers=[12,23,45,67]
try:
    print(numbers[6])
except IndexError:
    print("that position is doesn't exist")

#the raise
age=int(input("enter the age: "))
if age<0:
    raise ValueError("Age cannot be Negative")
print("your age is: ",age)

#using raise with try-except
try:
    age=int(input("enter the age: "))
    if age<0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("error: ",e)
print("program continues")

#ATM withdrawel
balance=5000
try:
    amount=int(input("enter the amount:  "))
    if amount<=0:
        raise ValueError("Amount must be greater than zero")
    if amount>balance:
        raise ValueError("insufficient balance")
    balance-=amount
    print("withdrawel sucessfull")
    print("remaining balance:",balance)
except ValueError as e:
    print("error: ",e)



try:
    a=int(input("enter the first  number: "))
    b=int(input("enter the second number: "))
    print("result: ",a/b)
except ValueError:
    print("please enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")

#student marks calculator
try:
  marks=[]
  name=input("enter name: ")
  for i in range(3):
      mark= int(input(f"enter marks for subject{i+1}: "))
      if mark<0 or mark>100:
       raise ValueError("marks must be between 0 and 100")
      marks.append(mark)
     
  print("marks: ",marks)
  print("total:",sum(marks))
  print("average: ",sum(marks)/len(marks))
except ValueError as e:
    print("invalid input!",e)

#custom exception : to create own ERRORS(problems)
#---------------------------#
#class creates new class
#InvalidNameError is the name of the custom exception
#(Exception) makes it an exception type
#pass means there is no additional code inside the class yet



class InvalidNameError(Exception):
    pass
try:
  name=input("enterr your name: ")
  if not name.replace("","").isalpha():
    raise InvalidNameError("Name must be contain alphabets only")
except InvalidNameError as e:
    print("ERROR:",e)

class InvalidMarksError(Exception):
   pass

marks=int(input("enter the marks: "))
if marks< 0 or marks> 100:
    raise InvalidMarksError("marks must be between 0 and 100")
print("marks:",marks)

#try-except
class InvalidMarksError(Exception):
    pass
try:
    marks=int(input("enter the marks:"))
    if marks <0 or marks>100:
        raise InvalidMarksError("marks must be between 0 and 100")
    print("marks: ",marks)
except ValueError:
    print("please enter a whole number.")
except InvalidMarksError as e:
     print("ERROR: ",e)



class InvalidMarksError(Exception):
   pass
class InvalidNameError(Exception):
    pass
try:
    name=input("enter your name: ")
    if not name.replace("","").isalpha():
        raise InvalidNameError("name must be alphabetical")
    marks=int(input("enter your marks: "))
    if marks<0 or marks>100:
        raise InvalidMarksError("marks must be between 0 and 100")
    print("student name:",name)
    print("marks: ",marks)
except ValueError:
    print("please enter a whole number")
except InvalidNameError as e:
    print("ERROR:",e)
except InvalidMarksError as e:
    print("Error: ",e)

#exception handling in functions
def divide(a,b):
    try:
        result=a/b
        print("result:",result)
    except ZeroDivisionError:
        print("cannot divided by zero ")
divide(10,2)
divide(10,0)

#handle invalid user iput inside a function
def get_age():
    try:
        age=int(input("enter your age: "))
        print("age:",age)
    except ValueError:
        print("age must be in numbers")
get_age()

class InvalidMarksError(Exception):
    pass
try:
    marks=int(input("enter your marks:"))
    if marks<0 or marks>100:
        raise InvalidMarksError("marks must be in between 1 to 100 ")
    print("marks: ",marks)
except ValueError:
    print("marks must be in numbers")
except InvalidMarksError as e:
    print("Errror: ",e)


