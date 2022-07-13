##Conditional Basics

##    prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input("Please input a day of the week.\n")
if day_of_the_week.lower() in ["monday"]:
    print("That is indeed Monday.")
else:
    print("That is not Monday.")

##    prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input("Please input a day of the week.\n")
if day_of_the_week.lower() in ["monday", "tuesday", "wednesday"," thursday", "friday"]:
    print("That is a weekday.")
elif day_of_the_week.lower() in ["saturday", "sunday"]:
    print("That day is on a weekend.")
else:
    print("That is not a day of the week.")

##        the number of hours worked in one week
##        the hourly rate
##        how much the week's paycheck will be
##    write the python code that calculates the weekly paycheck.
##You get paid time and a half if you work more than 40 hours
    
hours  = eval(input("How many hours did you work this week?\n"))
wage = eval(input("How much is your hourly rate in US dollars?\n"))
if hours > 40:
    paycheck = (40 * wage) + ((hours - 40) * (wage * 1.5))
else:
    paycheck = hours * wage
print("A total estimate for this week's pay is $", "{0:.2f}".format(paycheck), ".\n", sep="")

##Loop Basics

##    While
##        Create an integer variable i with a value of 5.
##        Create a while loop that runs so long as i is less than or equal to 15
##        Each loop iteration, output the current value of i, then increment i by one.

##    Your output should look like this:

##6
##7
##8
##9
##10
##11
##12
##13
##14
##15

i = 5
while i <= 15:
    print(i)
    i += 1
    

##    Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

x = 0
while x <= 100:
    print(x)
    x += 2
    
##    
##    Alter your loop to count backwards by 5's from 100 to -10.

x = 100
while x > -11:
    print(x)
    x -= 10
    
##    Create a while loop that starts at 2, and displays the number squared on each line while
##the number is less than 1,000,000. Output should equal:

## 2
## 4
## 16
## 256
## 65536

x = 2
while x < 1000000:
    print(x)
    x *= x

##Write a loop that uses print to create the output shown below.

##    100
##    95
##    90
##    85
##    80
##    75
##    70
##    65
##    60
##    55
##    45
##    40
##    35
##    30
##    25
##    20
##    15
##    10
##    5

x = 100
while x > 4:
    print(x)
    x -= 5

##For Loops

## Write some code that prompts the user for a number, then shows a multiplication table
## up through 10 for that number.

##    For example, if the user enters 7, your program should output:

##7 x 1 = 7
##7 x 2 = 14
##7 x 3 = 21
##7 x 4 = 28
##7 x 5 = 35
##7 x 6 = 42
##7 x 7 = 49
##7 x 8 = 56
##7 x 9 = 63
##7 x 10 = 70

times_table_10 = eval(input("Enter a number to find its multiples up to 10."))
for multiple in range(1,11):
    print(times_table_10, " x ", multiple, " = ", (times_table_10 * multiple))

##Create a for loop that uses print to create the output shown below.

##    1
##    22
##    333
##    4444
##    55555
##    666666
##    7777777
##    88888888
##    999999999

for x in range(1,10):
    print(str(x) * x)

##break and continue
##
## Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue
## prompting the user if they enter invalid input.
## (Hint: use the isdigit method on strings to determine this).
## Use a loop and the continue statement to output all the odd numbers between 1 and 50,
## except for the number the user entered.
##    Your output should look like this:
##
##        Number to skip is: 27
##
##        Here is an odd number: 1
##        Here is an odd number: 3
##        Here is an odd number: 5
##        Here is an odd number: 7
##        Here is an odd number: 9
##        Here is an odd number: 11
##        Here is an odd number: 13
##        Here is an odd number: 15
##        Here is an odd number: 17
##        Here is an odd number: 19
##        Here is an odd number: 21
##        Here is an odd number: 23
##        Here is an odd number: 25
##        Yikes! Skipping number: 27
##        Here is an odd number: 29
##        Here is an odd number: 31
##        Here is an odd number: 33
##        Here is an odd number: 35
##        Here is an odd number: 37
##        Here is an odd number: 39
##        Here is an odd number: 41
##        Here is an odd number: 43
##        Here is an odd number: 45
##        Here is an odd number: 47
##        Here is an odd number: 49

while True:
    num = eval(input("Enter an odd number from 1-50.\nThe number selected will be skipped when displaying"\
                                 " all the odd numbers from 1-50.\n"))
    if num % 2 == 1:
        for x in range(1, 50, 2):
            if x == num:
                print("Yikes! Skipping number: ", x)
                continue
            print("Here is an odd number: ", x)
    else:
        print("The number you entered is not odd. Try again.")
        continue
    break
        
##    The input function can be used to prompt for input and then used inside your python code.

##Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
##(Hints: first make sure that the value the user entered is a valid number, also note that the input function
##returns a string, so you'll need to convert this to a numeric type.)

while True:
    num = eval(input("Enter a positive integer.\nThe number selected will be counted up to from zero.\n"))
    if num  > 0:
        for x in range(0, (num+1)):
            print(x)
    else:
        print("The number you entered is not positive. Try again.")
        continue
    break

##    Write a program that prompts the user for a positive integer. Next write a loop that prints
##out the numbers from the number the user entered down to 1.

while True:
    num = eval(input("Enter a positive integer.\nThe number selected will be counted up to from zero.\n"))
    if num  > 0:
        for x in range(0, (num+1)):
            print(x)
    else:
        print("The number you entered is not positive. Try again.")
        continue
    break

##The Fizzbuzz Test
##
##One of the most common interview questions for entry-level programmers is the FizzBuzz test.
##Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
##
##    Write a program that prints the numbers from 1 to 100.
##    For multiples of three print "Fizz" instead of the number
##    For the multiples of five print "Buzz".
##    For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print( "FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        
##Display a table of powers.
##
##    Prompt the user to enter an integer.
##    Display a table of squares and cubes from 1 to the value entered.
##    Ask if the user wants to continue.
##    Assume that the user will enter valid data.
##    Only continue if the user agrees to.
##
##Example Output
##
##What number would you like to go up to? 5
##
##Here is your table!
##
##number | squared | cubed
##------ | ------- | -----
##1      | 1       | 1
##2      | 4       | 8
##3      | 9       | 27
##4      | 16      | 64
##5      | 25      | 125

nteger = eval(input("Please enter an integer.\n"\
                                    "The resulting table will display the squares and cubes up to that number.\n"\
                                    "You may want not want to pick an integer that is too large.\n"))
print("------|------|------")
for x in range(1, (nteger+1)):
    print("{:<6}".format(x), "{:<6}".format("|"), "{:<6}".format(pow(x, 2)),  "{:<6}".format("|"), "{:<6}".format(pow(x, 3)))

##Bonus: Research python's format string specifiers to align the table
##
##Convert given number grades into letter grades.
##
##    Prompt the user for a numerical grade from 0 to 100.
##    Display the corresponding letter grade.
##    Prompt the user to continue.
##    Assume that the user will enter valid integers for the grades.
##    The application should only continue if the user agrees to.
##
##    Grade Ranges:
##        A : 100 - 88
##        B : 87 - 80
##        C : 79 - 67
##        D : 66 - 60
##        F : 59 - 0
##
##Bonus
##
##    Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:
    while True:
        grade_input = input("Please enter the numerical grade you wish to convert.\n")
        try:
            float(grade_input)
        except ValueError:
            print("That is not a valid numerical grade.\n")
            continue
        grade = float(grade_input)
        if 100 >= grade >= 95:
            print(grade, " = A+")
        elif 94 >= grade >= 90:
            print(grade, " = A-")
        elif 89 >= grade >= 85:
            print(grade, " = B+")
        elif 84 >= grade >= 80:
            print(grade, " = B-")
        elif 79 >= grade >= 75:
            print(grade, " = C+")
        elif 74 >= grade >= 70:
            print(grade, " = C-")
        elif 69 >= grade >= 60:
            print(grade, " = D")
        elif 59 >= grade >= 0:
            print(grade, " = F")
        else:
            print("That is not a valid numerical grade.\n")
            continue
        break
    cont = input("Would you like to continue?\n")
    if cont.lower() in ["yes", "y"]:
        continue
    break

## Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should
## have the keys title, author, and genre. Loop through the list and print out information about each book.
## Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

library = [{"title" : "Everyone Poops", "author" : "Taro Gomi", "genre" : "Children's Books" }, \
 {"title" : "The Giver", "author" : "Lois Lowry", "genre" : "Science Fiction" }, \
 {"title" : "Foundation", "author" : "Isaac Asimov", "genre" : "Science Fiction" }, \
 {"title" : "Lord of the Rings", "author" : "J. R. R. Tolkein", "genre" : "Fantasy" }, \
 {"title" : "Neverending Story", "author" : "Michael Ende", "genre" : "Fantasy" }, \
 {"title" : "It", "author" : "Stephen King", "genre" : "Horror" }]

get_items = ['title','author','genre']
lengths = ( max(len(item[itemname]) for item in library) for itemname in get_items )
fmtstring = ' '.join(['{{:{:d}}}' for i in range(len(get_items))]).format(*lengths)

for book in library:
    print(fmtstring.format(book["title"], book["author"], book["genre"]))

while True:
    genre_check = input("Please enter the genre you wish to search for.\n")
    try:
        str(genre_check)
    except ValueError:
        print("Use only letters. That is not a valid input for genre.\n")
        continue
    for book in library:
        if book["genre"] == genre_check:
            print(book["title"])
        else:
            continue
    break


