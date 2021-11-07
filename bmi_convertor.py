def index():
    height = float(input("Input your height in meters: "))
    weight = float(input("Input your weight in kilograms: "))
    bmi= round(weight/(height*height),2)

    if bmi<18.5:
        print("You're underweight :( ")
    elif 18.5<=bmi<25:
        print("You're normal :)")
    elif 25<=bmi <30:
        print("You're overweight ")
    elif 30<=bmi >30:
        print("You are obese")
    

index()  # calling the function

print("Thanks for using Python Programming Language :)")
