name =input("enter the name:")
grade =int(input("enter the grade :"))
rollnumber =int(input("enter the roll number :"))
English = int(input("enter the English Marks :"))             
Math = int(input("enter the Math Marks :")) 
Urdu = int(input("enter the Urdu Marks :"))
Science= int(input("enter the  Science Marks :")) 
Islamiat = int(input("enter the Islamait Marks :")) 
Socialstudy = int(input("enter the Socialstudy Marks :")) 
Obtained_marks=  English + Math + Urdu + Science + Islamiat + Socialstudy
print(Obtained_marks)
percentage= Obtained_marks / 600 * 100
print(percentage)

print("----------STUDENT MARKSHEETS----------")
print("Your Name is :" + name)
print("Your Class is :" + str(grade))
print("Your Rollnumber is :" + str(rollnumber))
print("Total Marks are :600")
print("Obtained Marks are :" + str(Obtained_marks))
print("Your Percentage is : "  + str(percentage))
if percentage >= 90 :
     print("you got A+ GRADE:")
elif percentage>+ 80 :
     print("you got A GRADE :")
elif percentage>= 70:
     print("you got B GRADE :")
elif percentage>= 60:
     print("you got C GRADE :")
elif percentage>= 50:
     print("you got d GRADE :")
else:
 print("you are Fail:")