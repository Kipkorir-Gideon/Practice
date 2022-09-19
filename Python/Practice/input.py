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



