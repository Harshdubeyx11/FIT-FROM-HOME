GENDER=input("Enter your gender(M or F)")
BMI=float(input("Enter yor BMI"))
AGE=int(input("Enter your AGE"))
def FAT_percentage(BMI,AGE):
    if GENDER=="M":
        fat=(1.20*BMI)+(0.23*AGE)-16.2
    elif GENDER=="F":
        fat=(1.20*BMI)+(0.23*AGE)-5.4
    else:
        print("Error")
    if GENDER=="F":
        if AGE>=20 and AGE<=40:
            if fat<=21:
                print("UNDERFAT")
            elif fat>21 and fat<=33:
                print("HEALTHY")
            elif fat>33 and fat<=39:
                print("OVERWEIGHT")
            elif fat>39:
                print("OBESE")
        elif AGE>40 and AGE<=60:
            if fat<=23:
                print("UNDERFAT")
            elif fat>23 and fat<=35:
                print("HEALTHY")
            elif fat>35 and fat<=40:
                print("OVERWEIGHT")
            elif fat>40:
                print("OBESE")
        elif AGE>61 and AGE<=79:
            if fat<=24:
                print("UNDERFAT")
            elif fat>24 and fat<=36:
                print("HEALTHY")
            elif fat>36 and fat<=42:
                print("OVERWEIGHT")
            elif fat>42:
                print("OBESE")
    elif GENDER=="M":
        if AGE>=20 and AGE<=40:
            if fat<=8:
                print("UNDERFAT")
            elif fat>8 and fat<=19:
                print("HEALTHY")
            elif fat>19 and fat<=25:
                print("OVERWEIGHT")
            elif fat>25:
                print("OBESE")
        elif AGE>40 and AGE<=60:
            if fat<=11:
                print("UNDERFAT")
            elif fat>11 and fat<=22:
                print("HEALTHY")
            elif fat>22 and fat<=27:
                print("OVERWEIGHT")
            elif fat>27:
                print("OBESE")
        elif AGE>61 and AGE<=79:
            if fat<=13:
                print("UNDERFAT")
            elif fat>13 and fat<=25:
                print("HEALTHY")
            elif fat>25 and fat<=30:
                print("OVERWEIGHT")
            elif fat>30:
                print("OBESE")
    else:print("ERROR")
    print(fat)
FAT_percentage(BMI,AGE)                       
                
