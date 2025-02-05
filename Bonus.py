print("*****calculate your BMI*****")
weight = float(input("your weight please:"))
height = float(input("your height please:"))

bmi:float = weight / ((height*0.01)**2)

print("Your BMI is",round(bmi,2))
print("-"*15)
if bmi <= 29.9 and bmi >= 25:
    print("You are in the overweight range you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi <= 25.9:
    print("you are in the healthy weight range.")
elif bmi <= 18.5:
    print("you are in the underweight range.")
else:
    print("you are in the obesity range.")