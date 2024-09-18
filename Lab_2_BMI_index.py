#userprompts
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Formula
bmi = weight / (height ** 2)


print(f"Your BMI is: {bmi:.2f}")

# display msg
if 18.5 <= bmi <= 24.9:
    print("You are within the healthy BMI range.")
elif bmi < 18.5:
    print("You are NOT within the healthy BMI range.")
else:
    print("You are NOT within the healthy BMI range.")
