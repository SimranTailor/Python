# 1. Write a Program to input user's first name & print its length
First_Name = input("Enter First Name:")
print("Length of First Name is:", len(First_Name))

# 2. Write a Program to find the occurence of '$' in a String
Str = input("Enter a String:")
print(Str.count("$"))

# 3. Write a Program to check if a number entered by the user is odd or even
Num = int(input("Enter a Number:"))
if (Num % 2 == 0):
    print(Num, "is Even Number")
else:
    print(Num, "is Odd Number")

# 4. Write a Program to find the greatest of 3 numbers entered by the user
Num1 = int(input("Enter First Number:"))
Num2 = int(input("Enter Second Number:"))
Num3 = int(input("Enter Third Number:"))
if (Num1 >= Num2 and Num1 >= Num3):
    print(Num1, "is the Greatest Number")
elif (Num2 >= Num3):
    print(Num2, "is the Greatest Number")
else:
    print(Num3, "is the Greatest Number")

# 5. Write a Program to check if a number is a Multiple of 7 or not
num = int(input("Enter a Number:"))
if (num % 7 == 0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")
