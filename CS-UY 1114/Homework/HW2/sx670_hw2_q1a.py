w=float(input("Please enter weight in kilograms: "))
h=float(input("Please enter height in meters: "))
BMI=w/(h*h)
print("BMI is",BMI)
if (BMI<18.5):
    print("Underweight")
elif (BMI<24.9):
    print("Normal")
elif(BMI<29.9):
    print("Overweight")
else:
    print("Obese")

