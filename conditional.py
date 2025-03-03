marks = int(input("Enter Student marks : "))


if(marks >= 90):
    grade = "Grade A"; 

elif(marks >= 80 and marks < 90):
            grade = "Grade b"; 

elif(marks >= 70):
            grade = "Grade C"; 


else: 
      grade = "Grade D"; 


print("Grade of the student--->>>>", grade);