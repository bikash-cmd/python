name = input("Enter your name ")
age = input("Enter you Age ")
age = float(age)

weight = input("enter you weight in kg ")
height = input("enter your height in meter ")
weight = float(weight)
height = float(height)
bmi = weight/(height*height)
print("your BMI is " +str(bmi))
if  age > 20 :
    if bmi < 18.5:
        print("hello " + name +" you are underweight\n")
    elif (bmi > 18.5) and (bmi < 24.9):
        print("Congratulation! " +name +" you are normal")
    elif (bmi > 24.9) and (bmi < 29.9):
        print("hello " + name +" \nyou are over wight \n you need to do excercise and eat healthy")
    else:
        print("hello " + name +" \nalert you are obesity!!!! \n you need to exercise harder and need to make a habit of eating healthy ")
else:
    if bmi < 15.5:
        print("hello " + name +" \nyou need to eat more protein")
    elif (bmi > 15.5) and (bmi < 23.9):
        print("Congratulation! "  + name +" \nyou are normal")
    elif (bmi > 23.9) and (bmi < 28.9):
        print("you are over wight \n you need to do excercise and eat healthy")
    else:
        print("alert "+ name+ " are obesity!!!! \n you need to exercise harder and need to make a habit of eating healthy ")
    
