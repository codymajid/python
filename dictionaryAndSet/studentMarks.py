mark1 = input("Enter marks for 1:")
mark2 = input("Enter marks for 2:")
mark3 = input("Enter marks for 3:")

dicti = {};

# first method 
dicti.update({"English" : mark1})
dicti.update({"Maths" : mark2})
dicti.update({"Sindhi" : mark3})

# second method

newDic = dict(english = mark1, maths=mark2, sindhi= mark3);

print("dicti", dicti) 
print("new dict", newDic) 