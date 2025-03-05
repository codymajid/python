a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))


if(a >= b and a >= c and a >= d):
    print("First greatest is", a);

elif(b >= c and b >= d and b >= a):
    print("Second greatest number is", b)
    
elif(c >= d):
    print("Second greatest number is", c)
    
else : 
    print("Second greatest number is", d) 