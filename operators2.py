
#python has different types of the operators like arithmetic, relational,logical,bitwise,assignment operators

#arithmetic operator
#addition
n=34
m=40
print(n+m)

#subtraction
a=50
b=20
print(a-b)

#multiplication
s=3
c=9
print(s*c)

#division
e=40
f=5
print(e/f)

#modules
x=15
y=4
print(x%y) # it gives the reminder value after division

#floor division
s=40
t=5
print(s//t)# returns the integer value without having any decimal points

#exponentiation
p=3
o=4
print(p**o)# multiplies the number for the no.of times


#relational operators 
a=5
b=2
print(a>b) # '5' is greater then '2' so, it gives "TRUE"

d=3
f=3
print(d>=f) #gives "TRUE"


e=9
f=8
print(e<f)# gives"FALSE"


r=80
t=80
print(r==t) # This operator compare the two values ; it gives "true"


t=90
r=40
print(t==r)# gives "FALSE"

#assignment operators
d=45
d+=4
print(d) #add and assign

d=50
d-=2 #subtract and assign
print(d)

c=34
c*=2 #multiply and assign
print(c)

e=56
e/=2 #division and assign
print(e)

u=88
u%=3 #module and assign
print(u)

w=89
w//=2 #floor division and assign 
print(w)

h=78
h**=2 #power and assign
print(h)

k=90
k&=3 #logical and assign 
print(k)

y=89
y|=3 #logical or and assign
print(y)

r=6
r^=2 #square root and assign
print(r)


x=5
x>>=3 #rignt shift and assign
print(x)

z=34
z<<=3 #left shift and assign
print(z)


#comparing operators
e=23
f=23
print(e==f)

#not equal to
p=34
y=23
print(p!=y)

#greaterthan or equal to
d=34
f=43
print(f>=d)

#lessthan or equal to 
f=90
g=89
print(g<=f)

# chaining comparision operators 
x=5
print(1<x<10)
print(1<x and x<10 )


#logical operators
#and operator
a=5
b=10
print(a>3 and b>1)

#another example of and operator
s=5
print(s>0 and s<10)

#or operator
x=67
b=56
print(x>23 or b>100)
 
#another example of or operator
f=45
print(f>100 or f<89)

#not operator
f=90
print(not f>200)
print(not f<100)

#not operator with and operator
x=6
print(not(x>3 and x<30))


#identity operators 
#is operator
x=["apple","mango","banana"]
y=["apple","mango","banana"]
z=x
print(x is z) #return true if both variables are the same objects 
print(y is x)
print(x==y)

#is not
x=["apple","mango","banana"]
y=["apple","mango","banana"]
print(x is not y) #is not returns true if both variables are not the same

#membership operators
#in operator
x=["dream","imagination"]
print("dream" in x) #return true cause the sequence with the value 'dream' is in the list

#not in operator
x=["dream","imagination"]
print("reality" not in x) #returns true if the element is not in the list


#bitwise operators
#AND & operator
print(6&3) #the & operator compares each bit and set it to 1 both are 1 ,otherwise it set to 0

#OR | operator
print(6|3) #the | operator compares each bit and set it to 1 if one of them (or) both ,otherwise it set to 0

# x-or ^ operator compares each bit it set to 1 if one of them is 1,otherwise it set to 0 if both are 1and if both are 0


#type conversion or type casting
#int--->float
a=5
print("type of a: ",type(a))
b=float(a)
print(b)
#float--->int
g=34.5
h=int(g)
print(h)

#str--->int
a="9000"
c=int(a)
print(c)
print(type(c))
#int-->str
a=342
r=str(a)
print(r)
print(type(r))

#float-->str
y=23.344
z=str(y)
print(z)
print(type(z))
#str-->float
e="455.888"
f=float(e)
print(f)
print(type(f))





