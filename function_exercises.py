# This function is used to check that all my answers get inputs with correct types.

def num_check(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    return True

##    Define a function named is_two.
##    It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two():
    while True:
        user_input = input("How many things come in a pair?\n")
        if user_input.strip() != "2" and user_input.strip().lower() != "two":
            print("Oops! Try again.\n")
            continue
        else:
            print("That's correct!\n")
        break
is_two()

##    Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel():
    while True:
        user_input = input("Type a vowel into this prompt.\n")
        if user_input.strip().lower() != "a" and user_input.strip().lower() != "e" and user_input.strip().lower() != "i" and\
           user_input.strip().lower() != "o" and user_input.strip().lower() != "u" and user_input.isdigit() == False:
            print("Oops! Try again.\n")
            continue
        else:
            print("That's correct!\n")
        break
is_vowel()

##    Define a function named is_consonant.
##    It should return True if the passed string is a consonant, False otherwise.
##    Use your is_vowel function to accomplish this.

def is_consonant():
    while True:
        user_input = input("Type a consonant into this prompt.\n")
        if user_input.strip().lower() in "aeiou" or user_input.isdigit() == True:
            print("Oops! Try again.\n")
            continue
        else:
            print("That's correct!\n")
        break
is_consonant()

##    Define a function that accepts a string that is a word.
##    The function should capitalize the first letter of the word if the word starts with a consonant.

def lexi_cap():
    while True:
        user_input = input("Welcome to LexiCap!\nSo you want to capitalize a word, huh?\nEnter the word"\
                                           "you would like to capitalize!\n")
        first_letter = user_input[0]
        if user_input.isdigit() == True:
            print("Oops! Letters only, please!\n")
            continue
        if first_letter.lower() in "aeiou":
            print("Your word starts with a vowel, and will not be capitalized. We are biased at LexiCorp.\n")
            continue
        else:
            print(user_input.capitalize())
lexi_cap()
    
##    Define a function named calculate_tip.
##    It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip():
    print("Welcome to Tip by Calc U Later!\n")
    while True:
        
        tip_prcnt = input("What percentage of your bill would you like to tip?\nEnter as a number only, please.\n")
        
        if num_check(tip_prcnt):
            tip_prcnt = float(tip_prcnt)
        else:
            print("Silly user! Please, only enter a number for the percentage of your tip.\n")
            continue
        if tip_prcnt < 0:
            print("A negative tip?! That's rude! Please, use zero or a positive number for the percentage.\n")
            continue
        if tip_prcnt > 100:
            print("That's nice of you to tip that much, but let's keep your spending under control. Try a smaller "\
                      "percentage.\n")
            continue
        if tip_prcnt == 0:
            print("Please, don't be a cheapskate. Service workers don't always make a living wage.\n")
        
        tip_ratio = tip_prcnt / 100
        
        total_bill = input("What was your total bill (rounded to the nearest cent)?\n")
        if num_check(total_bill):
            total_bill = float(total_bill)
        else:
            print("The question asked for a number. Please, respect that. Try again\n")
            continue
        if total_bill < 0:
            print("They paid YOU for the meal?! Lucky... Calculate for a positive bill next time.\n")
            continue
     
        bill_w_tip = (tip_ratio + 1) * total_bill
        print("Your total bill with tip will be $", "{0:.2f}".format(bill_w_tip), ".\n", sep="")
        break
    
calculate_tip()
 
##    Define a function named apply_discount.
##    It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def calc_discount():
    print("Welcome to DisCounter by Calc U Later!\n")
    while True:
        
        dc_prcnt = input("How much of a discount would you like to give?\nEnter as a number only, please.\n")
        
        if num_check(dc_prcnt):
            dc_prcnt = float(dc_prcnt)
        else:
            print("Silly user! Please, only enter a number for the percentage of your discount.\n")
            continue
        if dc_prcnt < 0:
            print("A negative discount?! That's a ripoff! Please, use zero or a positive number for the percentage.\n")
            continue
        if dc_prcnt > 100:
            print("That's nice of you to discount that much. Your bank would like to know you are filing for bankruptcy soon. "\
                  "Try a smaller percentage next time.\n")
            continue
        if dc_prcnt == 0:
            print("No discount? Then why post all the signs saying you are having a sale?!.\n")
        break

    dc_ratio = dc_prcnt / 100

    while True:
        
        total_bill = input("What was the subtotal of the bill (rounded to the nearest cent)?\n")
        if num_check(total_bill):
            total_bill = float(total_bill)
        else:
            print("The question asked for a number. Please, respect that. Try again\n")
            continue
        if total_bill < 0:
            print("You paid the customer to take it off your hands?! Let's calculate for a positive bill next time.\n")
            continue
     
        bill_w_dc = (1 - dc_ratio) * total_bill
        print("The total bill after discount will be $", "{0:.2f}".format(bill_w_dc), ".\n", sep="")
        break
    
calc_discount()

##    Define a function named handle_commas.
##    It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas():
    while True:
        num = input("Enter an integer over 999 with commas included after every three place values.\n")
        if num.isalpha() == True:
            print("Please do not include letters. Try again.\n")
            continue
        num_form = int(num.replace(",", "_"))
        if int(num_form) < 1000:
            print("Please use a large enough integer. Try again.\n")
            continue
        print(num_form)
        break
handle_commas()

##    Define a function named get_letter_grade.
##    It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade():
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

##    Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels():
    print("Welcome to the Acme Vowel Remover!\n")
    user_input = input("Please type in a word or phrase to have all its vowels removed.\n")
    for i in user_input:
        if i.lower() in "aeiou":
            user_input = user_input.replace(i,"")
    print(user_input)
remove_vowels()

##    Define a function named normalize_name.
##    It should accept a string and return a valid python identifier, that is:
##        anything that is not a valid python identifier should be removed
##        leading and trailing whitespace should be removed
##        everything should be lowercase
##        spaces should be replaced with underscores
##        for example:
##            Name will become name
##            First Name will become first_name
##            % Completed will become completed

def normalize_name():
    while True:
        iden = input("Enter a name or selection of characters to turn it into a valid Python identifier.\n")
        if iden.isidentifier() == True:
            print(iden, " is already a valid Python identifier.\n")
            break
        if iden.isidentifier() != True:
            iden = iden.strip().lower().replace(" ", "_")
            print("Here is your new Python identfier:  ", iden, "\n")
        break        
normalize_name()

## Write a function named cumulative_sum that accepts a list of numbers and returns a list that is
## the cumulative sum of the numbers in the list.
##       ex. -  cumulative_sum([1, 1, 1]) returns [1, 2, 3]
##        cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum():
    user_input = input("Enter a list of numbers seperated by commas ' , ' to produce a cumulative sum.\n")
        
    user_list = user_input.replace(",", " ").split()
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    cs_list = []
    cs_len = len(user_list)
    cs_list = [sum(user_list[0: x: 1]) for x in range(1, cs_len+1)]
    print("Here is your original list:  ", user_list, "\n")
    print("Here is the cumulative sum:  ", cs_list, "\n")
        
cumulative_sum()

##Additional Exercise
##
##    Once you've completed the above exercises, follow the directions from
##    https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to
##    thouroughly comment your code to explain your code.
##
##Bonus:
##
##    Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm
##    and return a string that is the representation of the time in a 24-hour format.
##    Bonus: write a function that does the opposite.
##    
##    Create a function named col_index.
##    It should accept a spreadsheet column name, and return the index number of the column.
##        col_index('A') returns 1
##        col_index('B') returns 2
##        col_index('AA') returns 27
