"""
Challenge:
Write a program that says:
    This is
    a computer program
    that prints on several lines
"""
print ("""This is
a computer program
that print on several lines""")


"""
Challenge task:
Complete the following program so it uses the variables to print out ‘the cat sat on the mat’. It should print out on
one line, with spaces.
"""

word1 = "that"
word2 = "cat"
word3 = "sat"
word4 = "on"
word5 = "the"
word6 = "mat"
space = " "

sentense = word1 + space + word2 + space + word3 + space + word4 + space + word5 + space + word6
print(sentense)


"""
Challenge task:
Write a program that asks the user their name and then asks what their favourite food is, using their
name in the question, and responds to their answer.
"""

name = str(input("What is your name: "))
food = str(input("What is your fav food: "))
responses = ("Hello"+" "+name+" "+"your fav food is"+" "+food+" "+"Thank you!")
print(responses)


"""
Challenge task:
Write a program that has 3 variables (a, b and c). a = 12 and b = 6.
c should be equal to a plus b. The program should print c.
"""

a = 12
b = 6
c = a+b 
print(c)


"""
Challenge 5
Write a program that asks the user their first name and then asks them their surname and then prints
their whole name 3 times.
"""

fname = str(input("what is your first name: "))
surname = str(input("Enter your surname: "))

name3 = (fname+" "+surname+" "+fname+" "+surname+" "+fname+" "+surname)
print(name3)


"""
Challenge 6
Write a program that uses the following variables to calculate the number of minutes in a week:
Variables:
DaysPerWeek
HoursPerDay
MinutesPerHour
"""

DaysPerWeek = 7
HoursPerDay = 24
MinutesPerHour = 60

Week = 24 * 7
Weekmin = Week * 60
print("Number of minutes in a week is"+" "+str(Weekmin)+"min")

Logic = DaysPerWeek * HoursPerDay * MinutesPerHour
print(str(Logic)+" "+"Min")


"""
Challenge:
Write a program that asks the user their name, says ‘Hello’ to them, using their name and then asks how
old they are. The program should then calculate their age at their next birthday and respond “So your
next birthday you are (age)?’
"""

yname = str(input("Enter your name: "))
print("Hello"+" "+yname)
age = int(input("Enter your age: "))
calAge = (age + 1)
print("Next year you are"+" "+str(calAge)+" "+"Years old. Thank you!")


"""
Challenge 8
Find the area of a rectangle
Write a program that finds the area of a rectangle:
"""

width = int(input("ENter width: "))
height = int(input("ENter height: "))
area = width * height
print("Your rectangle are is"+" "+str(area))


"""
Challenge 10
Write a program that asks the user how long, on average, they spend on a computer per day.
"""

PCtime = int(input("how long you spend on a computer per day in hour: "))

if PCtime <= 2:
    print("That seems reasonable")
else:
    print("Get a life")

