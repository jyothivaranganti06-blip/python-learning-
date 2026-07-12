number=int(input("enter a number: ")) 
if number%2==0 and number >0:
     print(" you have entered positive even number")
elif number%2==0 and number < 0:
    print("you entered neg even number")
elif number%2!=0 and number < 0:  
    print("you have entered negative odd number")
elif number%2!=0 and number > 0:  
    print("you entered positive odd number")
else:
    print("you have entered whole number")