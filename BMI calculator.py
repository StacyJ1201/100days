weight = input(float("Enter your weight in pounds: "))
height = input(float("Enter your weight in inches: "))

weight_in_kgs = weight * 0.45359237

height_in_m = height * 0.0254

BMI = weight_in_kgs / (height_in_m ** 2)

print("Your BMI is " + str(BMI))