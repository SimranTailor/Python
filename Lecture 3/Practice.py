# 1. Write a Program to ask the user to enter names of their 3 favorite movies & store them in a list
# First Way
Movies = []
Mov1 = input("Enter your First favorite movie:")
Mov2 = input("Enter your Second favorite movie:")
Mov3 = input("Enter your Third favorite movie:")
Movies.append(Mov1)
Movies.append(Mov2)
Movies.append(Mov3)
print(Movies)

# Second Way
Movies = []
Mov = input("Enter your First favorite movie:")
Movies.append(Mov)
Mov = input("Enter your Second favorite movie:")
Movies.append(Mov)
Mov = input("Enter your Third favorite movie:")
Movies.append(Mov)
print(Movies)

# Third Way
Movies = []
Movies.append(input("Enter your First favorite movie:"))
Movies.append(input("Enter your Second favorite movie:"))
Movies.append(input("Enter your Third favorite movie:"))
print(Movies)

# 2. Write a Program to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1 = [1, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()
if (list1 == copy_list1):
    print("List is palindrome")
else:
    print("List is not palindrome")

# 3. Write a Program to count the number of students with the "A" grade in the following tuple ["C", "D", "A", "A", "B", "B", "A"]
Grade = ("C", "D", "A", "A", "B", "B", "A")
print(Grade.count("A"))

# 4. Write a Program to store the above values in a list & sort them from "A" to "D"
Grades = ["C", "D", "A", "A", "B", "B", "A"]
Grades.sort()
print(Grades)
