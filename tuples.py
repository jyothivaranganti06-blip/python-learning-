
#tuples : tuples are finite ordered list of elements. A tuple is defined as a data structure that
#comprises an ordered,finite sequence of immutable ,heterogeneous elements that are of fixed sizes.

#creating a tuple
my_tuple=(2,3,4)
print(my_tuple)

# tuple with mixed data types
my_tuple=(2,3,6,"hello",4.65)
print(my_tuple)

#nested tuple
my_tuple=("python",[4,7,8],0,98,7)
print(my_tuple)

#accessing elements
my_tuple=('p','y','t','h','o','n')
print(my_tuple[3])
print(my_tuple[2])

my_tuple=("python",[4,7,8],0,98,7)
print(my_tuple[1][2])
print(my_tuple[0])
print(my_tuple[4])

#negative indexing
tuple1=('f','r','u','i','t')
print(tuple1[-1])
print(tuple1[-3])
print(tuple1[-5])

#tuple with single element
my_tuple=("apple",) #always use comma when using single element
print(my_tuple)

#type of a value
my_tuple=("apple","banana")
print(type(my_tuple))

#string
my_tuple=("apple")
print(type(my_tuple))

#integer
my_tuple=(1)
print(type(my_tuple))

#float
my_tuple=(5.45)
print(type(my_tuple))


#tuple constructor 
tuple1=tuple(("apple","banana","mango"))
print(tuple1)


#slicing
my_tuple=('p','r','o','g','r','a','m','m','e','r')
print(my_tuple[3:7])
print(my_tuple[:4])
print(my_tuple[3:])
print(my_tuple[:-3])
print(my_tuple[-8:-2])
print(my_tuple[:])

#tuple operations
t1=(1,2,3)
print(t1*2)#repetative
t1=("hello",)
t2=("world",)
print(t1+t2) #concatenation

t1=(4,5,6)
print(5 in t1) #membership
print(8 in t1)

t1=(1,2,3,4,5)
for i in t1: #iteration
    print(i)

#tuple built in functions 
t1=(1,2,3)
t2=(4,5,6,7)
print(len(t2)) #length of tuple
print(max(t2)) #maximum
print(min(t1)) #minimum


#update tuple 
# tuples are immutable, so in ordered to update an element convert the tuple to list
x=("rasberry","peach","plum")
y=list(x) #convert to list
y[1]="kiwi" #update kiwi
x=tuple(y) #again convert to tuple 
print(x)

#add item
t2=("apple","mango","grapes")
y=list(t2)
y.append("orange")
t2=tuple(y)
print(t2)

#add tuple to tuple
t2=("orange","peach","banana")
y=("rasberry",)
t2+=y
print(t2)

#removing an item

t2=(3,4,5,6)
y=list(t2)
y.remove(4) #removes 4
t2=tuple(y)
print(t2)



#unpacking a tuple
fruites=("mango","apple","banana")
(green,yellow,red)=fruites
print(green)
print(yellow)
print(red)

#using asterisk 
t2=("apple","banana","rasberry","strawberry","watermelon","melon")
(green,yellow, *red)=t2
print(green)
print(yellow)
print(red)


#add list of values the " tropic" variable:

fruits=("apple","mango","cherry","berries","papaya")
(green,*tropic,red)=fruits
print(green)
print(*tropic)
print(red)

#problems based on tuples

#creating a tuple of 5 numbers and print third elements
tuple2=(4,5,6,7,8)
print(tuple2[2])

#length of tuple 
t1=(4,78,97,76)
print(len(t1))

#count occurence of 8
t=(4,3,4,8,7,8,66,8,64,8,8)
print(t.count(8))

#finding python inex
t=("c","java","c++","python","oracle","javascript")
print(t.index("python"))

#unpacking tuple
t=(1,2,3)
(a,b,c)=t
print(a)
print(b)
print(c)

#slicing the from the last
t=(3,4,5,6,7,8,9)
print(t[5:])

#single element 
t=(3,)
print(t)


#if 50 in t
t=(10,20,30,40,50)
print(50 in t)


#convert tuple into list
t=(5,6,7)
y=list(t)
t=tuple(y)
print(y)

#list to tuple
t=[4,5,6,7,3]
x=tuple(t)
t=list(x)
print(x)
#########


#loop through tuple
t=(4,5,7,8)
for i in t:
    print(i)

#loop through index numbers
t=(34,56,77,67)
for i in range(len(t)):
    print(i)

#using while loop
t=(3,7,9,8,0)
i=0
while i<len(t):
    print(t[i])
    i=i+1

#join tuples
t1=(23,4,5)
t2=(5,6)
t3=t1+t2 
print(t3)

#multiply tuples
t1=(2,3)
t3=t1*2
print(t3)

#reversing the tuple
t=(3,4,5)
print(t[::-1]) #it follows[start:stop:step]

#printing every second element
t=(4,5,6,7,8,9,0)
print(t[0:7:2])

#from index 2 to 5
t=(3,4,5,6,7,8,9,0)
print(t[2:5])


#counting numbers
count=0
t3=(4,5,5,6,4,5,4,4,4)
for i in t3:
    count+=1
print(count)

#sum of elements
t=(4,3,2,4,5)
sum=0
for i in t:
    sum+=i
print(sum)

#largest num in tuple
t=(3,4,5,6,7,9)
largest=t[0]
for i in t:
    if i>largest:
        largest=i
print(largest)

#smallest num in tuple
t=(3,1,2,34)
smallest=t[0]
for i in t:
    if smallest>i:
       smallest=i
    print(smallest)

#tuple packing and unpacking 
 
#swap two numbers using tuple unpacking
t=(4,3,5)
(green,red,blue)=t
temp=blue
blue=red
red=temp
print(green)
print(red)
print(blue)

#unpacking person
person=("john",25,"USA")
(name,age,country)=person
print(name)
print(age)
print(country)

#tuple+list conversion
t=(3,4,5)
y=list(t)
y.append(9)
t=tuple(y)
print(t)

#removing element
t=(3,4,98,5)
y=list(t)
y.remove(98)
t=tuple(y)
print(t)

#sorting
t=(86,57,3,98,23)
print(sorted(t))

#second max number
t=(3,87,65,32)
sorted(t)
print(sorted(t))
print(t[-2:-1])

#using set removes duplicates
t=(3,4,5,3,4,6,7,1)
e=set(t)
t=tuple(e)
print(t)

#removing duplicates without set()
t=(2,3,2,3,5,6,7,8,1,8,7)
result=[]
for i in t:
    if i not in result:
        result.append(i)
print(result)


#count occurence 
t=(4,5,4,5,3,4,7,4)
count=0
target=4
for i in t:
    if i == target:
      count+=1
print(count)

#checking palindrome
t=(4,5,6,5,4)
target=(t[::-1])
print(target)
if t==target:
       print("palindrome")
else:
        print("not plaindrome")


#product of all elements
t=(9,8,3)
prod=1
for i in t:
    prod*=i
print(prod)

#count vowels

t=('s','a','m','s','u','n','g')
vowels=('a','e','i','o','u')
count=0
for i in t:
    if i  in vowels:
        count+=1
    print(i)
print("count of vowels :",count)


#accessing an inner element in nested tuple

t=((2,3),(6,9))
print(t[0][1])
print(t[1][1])


#checking if two tuples are identical
t=(9,8,6)
t2=(9,8,6)
if t==t2:
  print("same")
else:
  print("not same" )

#common elements between two tuples
t1=(3,4,5)
t2=(7,4,5)
for i in t1:
   if i in t2:
    print("common elements are:",i)

#covert string to uppercase
t=("apple","flowers")
for i in t:
   print(i.upper())

#create a tuple of squares from 1 to 10
result=[]
for i in range(1,11):
    square=i*i
    result.append(square)
t=tuple(result)
print("square of numbers:",t)


#split the tuple into two equal halves
t=(3,4,7,8,9)
middle=len(t)//2
print("middle index of tuple:",middle)
print(t[0:2])
print(t[3:5])


t=(-2,3,-3,4,5,-6,-7)
positive=0
negative=0
for i in t:
    if i>0:
      positive+=1
        
    else:
       negative+=1
print("negative:",negative)
print("positive:",positive)

       

