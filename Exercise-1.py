# Create a program that asks the user
# to enter their name and their age.
# Print out a message addressed to them that tells
# them the year that they will turn 100 years old.
name = input("Tell me your name : ")
age = int(input("Tell me your age : "))
one_hundred_year = 100 - age
# print(one_hundred_year)
print("Name :", name)
print("Age : ", age)
if age == 100:
    print(name, "live so long now you're 100 years old")
elif one_hundred_year < 0:
    print(name, "have pass 100 years old by", abs(one_hundred_year), "years")
elif age < 1:
    print("did your mom given birth to you?")
else:
    print(name, "age will be 100 in", one_hundred_year, "years")
