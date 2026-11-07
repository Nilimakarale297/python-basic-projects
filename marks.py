# Student Marks Project - by Nilima Karale
print("Student Marks Calculator")

name = input("Tuz nav tak: ")
m1 = int(input("Maths marks: "))
m2 = int(input("Science marks: "))
m3 = int(input("English marks: "))

total = m1 + m2 + m3
average = total / 3

print("----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 75:
    print("Grade: Distinction - Khup Chhan!")
elif average >= 60:
    print("Grade: First Class")
elif average >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail - parat try kar")
