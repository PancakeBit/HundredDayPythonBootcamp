# don't change this code
height = float(input("enter your height in m: " ))
weight = float(input("enter your weight in kg: "))
# don't change this code

bmi = weight / (height **2)

if bmi < 18.5:
    classification = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    classification = "Healthy"
elif bmi >= 25 and bmi < 30:
    classification = "Overweight"
else:
    classification = "Obese"

print(f"Your bmi is {bmi:.2f} and You are classified as {classification}")
