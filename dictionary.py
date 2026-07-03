#dictionary  is a collection of data stored as key-value pair

#creating and accessing dictionary elements
student={"name":"james","age":20,"course":"cse"}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])
print(student.get("name"))  #using get()

#adding items
student={"name":"jay"}
student["age"]=24
print(student)

#updating an item
student={"name":"sana","age":28}
student["age"]=29
print(student)

#removing  items
#pop()
std={"name":"shinchan","age":5}
std.pop("age")
print(std)

#del()
std={"name":"kazhama","age":5}
del std["age"]
print(std)

#dict length
std={"name":"david","age":25,"region":"USA"}
print(len(std))

#loops through dictionary
student={
"name":"juhoon",
"age":18
}
for key in student:
    print(key)

for value in student.values():
   print(value)
for key, value in student.items():
    print(key,value)

#Built-in methods in dictionary 

student={"name":"james","age":20}
print(student.keys()) #return all keyks
print(student.values()) #returns all values
print(student.items()) #return all among with keys and values
print(student.get("name")) #return values safely
print(student.pop("age")) #removes item
print("after removing age:",student)
student.update({"age":20}) #updates dictionary
print("afer updating age:",student)
print(student.copy()) #copy the dictionary
print(student.clear()) #removes all items
keys=["a","b","c","d"]
d=dict.fromkeys(keys,0) #create a new dictionary from the iterable with the values equal to value
print(d)
g={"a":1} 
print("a"in g)
d={"name":"david"}
d.setdefault("age",20) #it is used to set the key to the default value if the key 
#is not declaredd in the dictionary
print(d)

#nested dictionary 
students={"s1":{"name":"james","age":20},
          "s2":{"name":"juhoon","age":18}}
print(students["s1"]["name"])
print(students["s2"]["age"])

#dictionary comprehension 
square={x:x*x for x in range(2,6)}
print(square)

#practice problems

#creating a dict with name,age,course
#basic problems
student={"name":"jay","age":24,"course":"computer science"}
print(student)
#print all keys
print(student.keys())
#print all values
print(student.values())
#add a new key called "city"
student["city"]="australia"
print(student)
#update age
student.update({"age":25})
print(student)
#remove one key using pop()
print(student.pop("city"))
print("after removing city:",student)
#find the length of dictionary
print(len(student))
#check if a key exists
print("age" in student)
#print all key-value pair
print(student.items())
#clear dictionary
print(student.clear())
#intermediate problems
#count frequency of character in a string 
#using if-else method
s="apple"
freq={}
for i in s:
    if i  in freq:
      freq[i]=freq[i]+1 #if "a" in freq it count plus
    else:
       freq[i]=1 #if "a" appears once it counts once
print(freq)

#using get() method
s="apple"
freq={}
for i in s:
   freq[i]=freq.get(i,0)+1
print(freq)

#count frequency of words in a sentence
sen="python is a programming language it is a easy programming language"
s=sen.split(" ")
print(s)
freq={}
for i in s:
   if i in freq:
      freq[i]+=1
   else:
      freq[i]=1
print(freq)

#find the student with highest marks
marks={"A":34, "B":99,"C":98}
highest_student=""
highest_marks=0
for student in marks:
   if marks[student]>highest_marks:
      highest_marks=marks[student]
      highest_student=student
print("highest marks:",highest_marks)
print("student:",highest_student)
#sum all values in a dictionary
val={"a":5,"b":8,"c":3}
v=val.values()
print(v)
total=0
for i in v:
   total+=i
print(total)
#create a dic of numbers and their squares from 1 to 10 
sqr={}
for i in range(1,11):
   sqr[i]=i*i
print(sqr)
#merge two dictionaries
d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5,"f":5}
d3=d1|d2 #union operator
print(d3)
#find keys whose values are greater than 20
d={"a":2,"b":56,"c":45,"d":12,"e":59}
for key in d:
   if d[key]>20:
      print(key)
#reverse a dictionary
d={"a":1,"b":2,"c":3}
reverse={}
for key  in d:
   reverse[d[key]]=key
print(reverse)
#nested dictionary for 3 students
student={"s1":{"a":1,"b":2},
         "s2":{"c":3,"d":4},
         "s3":{"e":6,"f":7}}
print(student)

#count vowels in a string using a dictionary
s="union"
freq={}
for i in s:
    if i in  "aeiou":
       if   i in freq:
        freq[i]=freq[i]+1
       else :
         freq[i]=1
print(freq)

s="bEautIful"
txt=s.lower()
vowels={}
for i in txt:
    if i in "aeiou":
       vowels[i]=vowels.get(i,0)+1
print(vowels)

 