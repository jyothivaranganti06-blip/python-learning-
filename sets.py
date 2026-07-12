# A set is a collection of unordered elements and stores unique elements,is mutable .
fruits={"apple","orange","grapes"}
print(fruits)

students={"rahul","rohith","rahul","raghav"}#set can't contain duplicate values
print(students)#duplicates disappear automatically
#subjects passed
passed={"python","java","SQL"}
print("python"in passed)  #true
#creating a set
a={1,2,3,4}
b=set()
c=set([1,2,3,4])
print(c)
print(a)

#important functions
#add()
s={1,2}
s.add(3)
print(s)
#update()
s={1,2}
s.update([3,4])
print(s)
#remove()
s={1,2,3}
s.remove(2)
print(s)
#discard
s={2,3,4}
s.discard(3)
print(s)
#pop()
s={2,3,4,5}
print(s.pop())
print(s)
#clear()
s={2,3,4}
print(s.clear())
#copy()
s={2,3,4}
print(s.copy())
print(s)

#set operations
#UNION combines two sets and ignore duplicates
a={1,2,3,4}
b={2,3,4,5}
print(a|b)

#INTERSECTION only gives the same in both sets
a={1,2,3,4}
b={2,3,4,5}
print(a&b)

#DIFFERENCE 
a={1,2,3,4}
b={2,3,4,5}
print(a-b)

#SYMMETRIC DIFFERENCE
a={1,2,3,4}
b={4,5,6,7}
print(a^b)

# FROZEN SET  connat be modified
#a=frozenset([1,2,3])
#a.add(4)
#print(a)

# practice questions
# BASIC
# create a set of five colors
colors={"red","green","yellow","orange"}
print(colors) #printing all elements

#add one color to colors
colors.add("purple")
print(colors)
#remove one color
colors.remove("orange")
print(colors)
#length of set
print(len(colors))
#check if number exist
print(2 in colors)
#clear the set
print(colors.clear())
#copy a set
colors={"red","green","yellow","orange"}
print(colors.copy())
print(colors)
#convert a list to set
a=[1,2,4]
c=set([1,2,4])
print(c)
#convert set to list 
a={1,2,5}
c=list({1,2,5})
print(c)

#INTERMEDIATE PROBLEMS
#find union
a={1,4,3}
d={3,2,6}
print(a|d)
#find intersection
a={2,3,4}
d={2,4,5}
print(a&d)
#find difference
a={3,9,0}
b={3,4,5,6}
print(a-b)
print(b-a)
#find symmetric difference
a={2,3,4,5}
b={2,4,5,7}
print(a^b)
#remove duplicates from list
l=[2,3,2,4,5,3]
s=set(l) #coverting list to set
a=list(s)#converting the set to list without deplicates
print(s)
print(a)

#count unique numbers
l=[4,5,6,4,5,6]
s=set(l)
print(s) #set only contain unique values
print(len(s)) #count the elements

#find common elements in two lists
l1=[2,3,4,5,1]
l2=[3,4,7,8,2]
s1=set(l1)
s2=set(l2)
print(s1&s2) #intersection combines the common elements

#check whether two sets are equal
s1={2,3,4,9}
s2={8,5,6,1}
s3={8,5,1,6}
print(s2==s3) #true
print(s1==s2) #false

#find the elements only in the first set
s1={3,4,5}
s2={4,3,6}
print(s1-s2) #using the symbol
print(s1.difference(s2)) #using the method

#merge the sets
s1={4,3,2}
s2={6,7,8}
s3={9,8,0}
print(s1|s2)#using the symbol
print(s1.union(s2))#using the method
print(s1.union(s2,s3)) #merging the three sets

#advanced problems
#finding missing numbers using sets
expected=set(range(1,11))
s={3,4,6,9}
print(expected.difference(s))
#check if the one set is a subset of another
s1={2,3,4,5}
s2={2,4,5,3}
print(s1.issubset(s2)) # .issubset checks if the set contain all elements of another set
print(s1<=s2)
#check if one set is superset of another
s={2,3,4,6}
s1={2,3,4,6}
print(s.issuperset(s1)) #superset is check if a set contains all elements of another set
print(s>=s1)
#check if two sets are disjoint 
s={3,2,4,5}
s1={8,9,7,6}
print(s.isdisjoint(s1)) #return true if two sets has no common elements

#remove the duplicates while preserving the order
