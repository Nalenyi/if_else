# Write a program to check whether a person is eligible for voting or not. (accept age from user)
age=int(input("Enter age:"))
if age >=18:
    print("eligible for voting")
else:
    print("not eligible for voting")

# # Write a program to check whether a number entered by user is even or odd. 
Num=int(input("Enter number:")) 
if Num%2==0:
    print("even")  
else:
    print("odd")
# Write a program to check whether a number is divisible by 7 or not.    
num=int(input("enter number:"))
if num%7==0:
    print("divisible by 7")
else:
    print("not divisible by 7")
# # Write a program to display "Hello" if a number entered by user is a multiple of five , 
# # otherwise print "Bye".    
num=int(input("enter number:"))
if  num%5==0:
    print("Hello")

else:
    print("bye")
# Write a program to calculate the electricity bill (accept number of unit from user)
#  according to the following criteria :  
#            Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
unit=int(input("enter unit:")) 

# Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)
num=int(input("Enter number:"))
if num%10==0:
 print("The last digit is",num%10)
# Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.
num=int(input("Enter number:"))
if num%3==0:
    print("divisible by 3")
else:
    print("not divisible")
# Write a program to accept percentage from the user and display the grade according to the 
# following criteria:

        #  Marks                                    Grade
        #  > 90                                         A
        #  > 80 and <= 90                       B
        #  >= 60 and <= 80                       C
        #  below 60                                  D
 
scores=int(input("Enter number:"))
if scores >90:
    print("A")
elif scores> 80 and scores<= 90:
    print("B")
elif scores>=60 and scores<=80:
    print("C") 
else:
    print("D")       
# Write a program to check whether an years is leap year or not.
year=int(input("Enter year:"))
if year%4==0:
    print("Leap year")
else:
    print("not a leap year")


def mult():
 for num in range(1,50):
    if num%7==0:
        print(num)

mult()
def product():
    y=1
    num = [7,2,6,8]
    for x in num:
        y*=x
        print(y)
product()



# Counting the total number of digits in a number.
def numbers():
 numbers=6587292
 i=0
 while i in numbers:
  print(i.count())
            
# Write a program to accept a number from 1 to 7 and display the name of the day 
# like 1 for Sunday , 2 for Monday and so on.
num=int(input("Enter any number from 1 to 7:"))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
   print("Thursday")
elif num==6:
    print("Friday")
elif num==7:
        print("Saturday")
# Write a program to accept a number from 1 to 12 and display name of the month and days in that
#  month like 1 for January and number of days 31 and so on.
days=int(input("Enter any number from 1 to 12:"))
if days==1:
    print("January  and it has 31 days")
if days==2:
    print("February and it has 29 days")
if days==3:
    print("March and it has 31 days")
if days==4:
    print("April and it has 31 days")
if days==5:
    print("May and it has 30 days")
if days==6:
    print("June and it has 30 days")
if days==7:
    print("July and it has 30 days")
if days==8:
    print("August and it has 31 days")
if days==9:
    print("September and it has 30 days")
if days==10:
    print("October and it has 31 days")
if days==11:
    print("November and it has 30 days")
if days==12:
    print("March and it has 31 days")
#  Write the logical expression for the following:
# A is greater than B and C is greater than D
    

def numbers(y):
    for i in y:
        if y [0]==y[-1]:
            return True
        else:
            return False
print(numbers([12,5,66,15,13])) 




  











    

