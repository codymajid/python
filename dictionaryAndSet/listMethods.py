list = [2,3,1,4];

list.append(5); #add new element in the end 

list.sort();

list.sort(reverse=True) #descending order me sort krnay kay leye 

list.reverse(); 

list2 = list.insert(0,"Mango")

print(list)

remove =  list.pop(0);
print("remove", remove)
print("remove", list)

p = list[0] = 4

print("list in p", list)

print("p", p)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("thislist", thislist)

