height = input("Input your height in meters(0.0): ")
weight = input("Input your weight in kg: ")

bmi = int(weight) / (float(height) **2)

print("Body Mass Index is calculated as Weight/height2")
print("Your Body Mass Index is: " + str(int(bmi)))
