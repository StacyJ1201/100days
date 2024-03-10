weight = input("Enter your weight in pounds: ")
height = input("Enter your height in inches: ")

weight_in_kgs = float(weight) * 0.45359237

height_in_m = float(height) * 0.0254

BMI = weight_in_kgs / (height_in_m ** 2)

print("Your BMI is ", BMI)