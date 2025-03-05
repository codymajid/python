#yeh like objects he hotay json me bs likhengay 

dictionary = {
    "name" : "Majid Aziz",
    "caste" : "Shaikh",
    "age" : "25",
    "students" : {
        "chem" : 12,
    }
}

print("dictionary", dictionary["name"])

keys = tuple(dictionary.keys());

print("keys", keys)


dictionary["students"].update({"city" : "Karachi"});
print("dictionary updated", dictionary)