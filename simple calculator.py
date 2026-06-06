
a=int(input("enter a number: "))
b=int(input("enter another number: "))
operator=input("choose an operator(+,-,*,/,%)")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
else:
    print(" choose valid operator")