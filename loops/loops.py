# i = 1;

# while i <= 100:
#     print("x", i);  
#     i += 1; 


# print multiplication number n 

# num = int(input("Enter number 1:")); 
# seq = 1;

# while seq <= 10:
#     print(num, "x", seq, "=", (num * seq));
#     seq += 1; 


# print list using loop

# nums = (1,4,7,15,44,55,312,1); 
# idx = 0;

# while idx <= len(nums) - 1: code
#     print("nums", nums[idx]);  
#     idx += 1; 


# search for  number n 

num = int(input("Enter Number:"));  
nums = (1,4,7,15,44,55,312,1); 
idx = 0;

while idx <= len(nums) - 1:  
    val = nums[idx];
    idx += 1; 
    if(val == num) :
        print("yes number exists", val); 
    elif(val != num): 
        print('No not exists');
    
    
