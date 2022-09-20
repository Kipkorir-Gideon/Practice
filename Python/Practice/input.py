# input("What's your name?")
# print("Your name has" + " " + len(input) + "characters.")


# a = 100
# b = 400

# c = a
# a = b
# b = c

# print(a)
# print(b)


# print("Welcome to the Band Name Generator.")
# your_city = input("What is the name of the city you grew in?\n")
# favorite_pet = input("What is your favorite pet?\n")

# print("Your band name could be " + your_city + " " + favorite_pet)


# num = 45
# to_str = str(num)  
# print(int(to_str[0]) + int(to_str[1]))

# weight = float(input("What is your weight in kilograms?\n"))
# height = float(input("What is your height in meters?\n"))


# bmi = round(weight / (height ** 2), 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi} and you are underweight!")
# elif bmi <= 25:
#     print(f"Your BMI is {bmi} and you are under the normal weight.")
# elif bmi <= 30:
#     print("Your BMI is {bmi} and you are overweight!")
# elif bmi <= 35:
#     print("Your BMI is {bmi} and you are obese!")
# else:
#     print("Your BMI is {bmi} and you are clinically obese!")


# age = input("What is your age?\n")
# remaining_years = 90 - int(age)
# days = remaining_years * 365 
# weeks = remaining_years * 52 
# months = remaining_years * 12   
# print(f"You have {days} days, {weeks} weeks, {months} months remaining.")


# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in centimeters?\n"))

# if height >= 120:
#     print("You can ride the rollercoaster. Enjoy.")
# else:
#     print("You cannot ride the rollercoaster. Try after some time.")



# print("Welcome to the number check!")
# number = int(input("Please enter a number:\n"))

# if number % 2 == 0:
#     print("You entered an even number.") 
# else: 
#     print("You entered an odd number.")

# height = int(input("Enter your height in centimeters:\n"))

# if height >= 120:
#     adult = input("Are you an adult or not? (yes/no):\n ")
#     if  adult == "yes":
#         print("You can ride the rollercoaster at a cost of $10.") 
#     elif adult == "no":
#         print("You can ride the rollercoaster at a cost of $7.")
#     else:
#         print("Invalid input. Please enter either 'yes' or 'no'.")
# else:
#     print("You cannot ride the rollercoaster.")


# year = int(input("Enter a year to check if it is a leap year or not: \n"))

# if year % 4 == 0 and year % 400 == 0:
#     print("A leap year.")
# elif year % 4 == 0 and year % 100 == 0:
#     print("Not a leap year.")
        
# else:
#     print("Not a leap year.")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.") 




# print("Welcome to Python Pizza Deliveries!")

# size = input("What size of pizza you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? (Y/N)\n")
# extra_cheese = input("Do you want extra cheese? (Y/N)\n")

# bill = 0

# if size == "S":
#     bill += 15  
    # if add_pepperoni == "Y":
    #     bill += 2
    # if extra_cheese == "Y": 
    #     bill += 1
# elif size == "M":
#     bill += 20 
    # if add_pepperoni == "Y":
    #     bill += 3
    # if extra_cheese == "Y": 
    #     bill += 1
# elif size == "L":
#     bill += 25
    # if add_pepperoni == "Y":
    #     bill += 3
    # if extra_cheese == "Y": 
    #     bill += 1

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2 
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your bill is ${bill}")



# print("Welcome to Love Calculator!\n")
# name1 = input("What is your name\n").upper()
# name2 = input("What is their name?\n").upper()



# count1 = 0
# count2 = 0

# for i in name1:
#     if i == "T" or i == "R" or i == "U" or i == "E":
#         count1 += 1

# for i in name2:
#     if i == "T" or i == "R" or i == "U" or i == "E":
#         count2 += 1
# result1 = count1 + count2

# count3 = 0
# count4 = 0

# for i in name1:
#     if i == "L" or i == "O" or i == "V" or i == "E":
#         count3 += 1

# for i in name2:
#     if i == "L" or i == "O" or i == "V" or i == "E":
#         count4 += 1
# result2 = count3 + count4


# result = str(result1) + str(result2)

# if int(result) < 10 or int(result) > 90:
#     print(f"Your score is {result}, you go together like coke and mentos.") 
# elif int(result) >= 40 and int(result) <= 50:
#     print(f"Your score is {result}, you are alright together.")
# else:
#     print(f"Your score is {result}.")




# print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# direction = input("Which direction are you taking? 'Left' or 'Right\n").lower()

# if direction == "left":
#     swim_or_wait = input("Do you want to swim or wait? 'Swim' or 'Wait'\n").lower()
#     if swim_or_wait == "wait":
#         color = input("What color of the door do you want to open? 'Red' or 'Yellow' or 'Blue'\n").lower()
#         if color == "yellow":
#             print("You Win!")
#         else:
#             print("Game Over!")
#     elif swim_or_wait == "swim":
#         print("Game Over!")
# elif direction == "right":
#     print("Game Over!")



# import random

# random_integer = random.randint(0, 100)

# print(random_integer)

# random_float = random.random()
# print(random_float)


# import random

# test_seed = int(input("Create a seed number:\n"))
# random.seed(test_seed)


# toss = random.randint(0,1)

# if toss==0:
#     print("Heads")
# else:
#     print("Tails")



# import random

# namesAsCSV = input("Give me everybody's names, separated by a comma\n")
# names = namesAsCSV.split(",")

# print(names)

# random_index = random.randint(0, len(names) - 1)
# print(random_index)

# random_name = names[random_index]

# print(f"{random_name} is the one paying the bill.")



# row1 = ["","",""]
# row2 = ["","",""]
# row3 = ["","",""]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position  = input("Where do you want to put the treasure?\n")

# vertical = int(position[1])
# horizontal = int(position[0])

# selected_row = map[vertical -1]
# selected_row[horizontal -1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!") 




# fruits = ["Apple", "Peach", "Banana", "Pear"]
# for fruit in fruits:
#     print(fruit)


# student_heights = input("Input the heights of the students in centimeters.\n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# student_height_sum = 0

# for student_height in student_heights:
#     student_height_sum += student_height

# average_height = round(student_height_sum / len(student_heights))
# print(f"The average height of the students is {average_height} centimeters.")



# student_scores = input("Input a list of students scores.\n").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = student_scores[n]
# for score in student_scores:
#     if highest_score < score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")



# total = 0
# for number in range(2, 101, 2):
#     total += number
#     print(number)

# print(total)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number) 
    



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")