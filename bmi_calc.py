
height = float(input("Enter your  Height in cm : "))
weight = float(input("Enter your weight in kg : "))


#bmi fomula
bmi =  weight / (height/100)**2

print (f"Your BMI is {bmi}")

#BMI classification using if conditions  
if bmi <= 18.4:
    print("Your are underweight")
elif bmi <= 24.9:
    print("Your are healthy")
elif bmi <= 29.9:
    print("Your overweight")
elif bmi <= 34.9:
    print("You are serverly overweight")
elif bmi <= 39.9:
    print("You are obese")
else :
    print("You are serverly obese.")

