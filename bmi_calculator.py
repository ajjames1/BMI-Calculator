def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print(f"Your BMI is {bmi}, which falls under '{category}' category.")