height=float(input("Enter your height in meters"))
weight=float(input("Enter your weight in kilograms"))
def BMI(height,weight):
    Bmi=(weight/height**2)
    print(Bmi)
    if Bmi <=18.5:
        print("UNDERWEIGHT!")
    elif Bmi >18.5 and  Bmi<25:
        print("NORMAL.")
    elif Bmi>25 and Bmi<30:
        print("OVERWEIGHT!")
    elif Bmi>30:
        print("OBESE!")
    else:
        print("error")
BMI(height,weight)        
