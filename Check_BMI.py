#CALCULATE BMI INDEX

weight = input("enter you weight in kg")
height = input("enter your height in meter")
weight = float(weight)
height = float(height)
bmi = weight/(height*height)

print("your BMI is " +str(bmi))
if bmi < 18.5:
    print("you are underweight\n")
    print("you need to eat more protein")
elif (bmi > 18.5) and (bmi < 24.9):
    print("Congratulation! you are normal")
elif (bmi > 24.9) and (bmi < 29.9):
    print("you are over wieght \n you need to do excercise and eat healthy")
else:
    print("alert you are obesity!!!! \n you need to exercise harder and need to make a habit of eating healthy ")