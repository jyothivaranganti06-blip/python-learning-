# #class: a class is a blueprint for creating objects 
# class student:
#     pass
# s1=student()
# print(s1)




# class student:
#     pass
# s1=student()
# s1.name="jyothi"
# s1.age=20
# print(s1.name)
# print(s1.age)

# class student:
#     pass
# s1=student()
# s1.name="jyothi"
# s1.age=20

# s2=student()
# s2.name="james"
# s2.age=20
# print(s1.name,s1.age)
# print(s2.name,s2.age)

# class employee:
#     pass
# e1=employee()
# e1.name="jyothi"
# e1.salary=30000
# e2=employee()
# e2.name="sampath"
# e2.salary=40000

# print("Name:",e1.name,"\nSalary:",e1.salary)
# print("Name:",e2.name,"\nSalary:",e2.salary)

# #__init__() and self()
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# e1=Employee("jyothi",40000)
# e2=Employee("sampath",50000)
# print(e1.name,e1.salary)
# print(e2.name,e2.salary)

# class student:
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.marks=marks
#         self.age=age
# s1=student("jyothi",89,20)
# s2=student("juhoon",78,19)
# s3=student("james",89,20)
# print(s1.name,s1.marks,s1.age)
# print(s2.name,s2.marks,s2.age)
# print(s3.name,s3.marks,s3.age)

# #instance method: is a function written inside a class that works with an object's data
# class Animals:
#     def __init__(self,pet,sound):
#         self.pet=pet
#         self.sound=sound

#     def display(self):
#             print("pet:",self.pet)
#             print("sound:",self.sound)
# a1=Animals("cat","meow")
# a2=Animals("dog","bow")
# a1.display()
# a2.display()

# #adding a method that returns a value
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calculate_area(self):
#           Area=self.length*self.width
#           return Area
# r1=Rectangle(23,6)
# r2=Rectangle(2,9)
# print(r1.calculate_area())
# print(r2.calculate_area())

#class variables vs instance variables
#instance variables: belong to individual objects. Each object can have different values
class Employees :
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employees("jyothi",75000)
e2=Employees("Adithya",65000)
print(e1.name)
print(e1.salary)
print(e1.company)

print(e2.name)
print(e2.salary)
print(e2.company)

#inheritance:means one class can reuse the properties and methods of another class

class Animal:
    def eat(self):
        print("this animal is eating")
class Dog (Animal):
    def bark (self):
        print("dog is barking")
d1=Dog()
d1.eat()
d1.bark()

#inheritance with __init__() :a child class can also inherit attributes from its parent
class Animal:
    def __init__(self,name):
        self.name=name
class Dog (Animal):
    def bark (self):
        print(self.name, "is barking")
d1=Dog("YEONTAN")
d1.bark()