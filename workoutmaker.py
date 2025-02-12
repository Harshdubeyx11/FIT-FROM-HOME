#the workout
MODE=input("Enter the intensity of workout you want?begginer,regular or pro")
def User_workout():
    cal_workout=0
    AMR=int(input("Enter your amr in calories"))
    weight_init=int(input("Enter your current weight in kg"))
    weight_fin=int(input("Enter your desired weight in kg"))
    if weight_init>weight_fin:
        cal_count=(weight_init-weight_fin)*7700 
    elif weight_init<weight_fin:
        cal_count=(weight_fin-weight_init)*7700
    elif weight_init==weight_fin:
        cal_count=0
    if MODE == "begginer"and weight_init>weight_fin:
        cal_workout:AMR+500
    elif MODE == "regular"and weight_init>weight_fin:
        cal_workout:AMR+800
    elif MODE == "pro"and weight_init>weight_fin:
        cal_workout:AMR+1100 
    elif MODE == "begginer"and weight_init<weight_fin:
        cal_workout:AMR-500      
    elif MODE == "regular"and weight_init<weight_fin:
        cal_workout:AMR-800    
    elif MODE == "pro"and weight_init<weight_fin:
        cal_workout:AMR-1100    
    workout_days=cal_count//cal_workout
    print("your workout is for",workout_days,"days")
    cal_muscle=cal_workout//12
    import csv
    import random
    l=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    l11=[]
    l12=[]
    l_workout={}
    f=open("User_exercise.csv","r")
    r=csv.reader(f)
    for i in r:
       l.append(i)
    for i in l:
        if i[0] =="delts":
            l1.append(i[1])
        elif i[0] =="back":
            l2.append(i[1])
        elif i[0] =="glutes":
            l3.append(i[1]) 
        elif i[0] =="calves":
            l4.append(i[1])    
        elif i[0] =="quads":
            l5.append(i[1])    
        elif i[0] =="lats":
            l6.append(i[1])
        elif i[0] =="abs":
            l7.append(i[1])
        elif i[0] =="obliques":
            l8.append(i[1])  
        elif i[0] =="biceps":
            l9.append(i[1]) 
        elif i[0] =="triceps":
            l10.append(i[1])    
        elif i[0] =="forearms":
            l11.append(i[1])
        elif i[0] =="chest":
            l12.append(i[1]) 
    exercise1=str(random.choices(l1))        
    exercise2=str(random.choices(l2))        
    exercise3=str(random.choices(l3))        
    exercise4=str(random.choices(l4))        
    exercise5=str(random.choices(l5))        
    exercise6=str(random.choices(l6))        
    exercise7=str(random.choices(l7))        
    exercise8=str(random.choices(l8))        
    exercise9=str(random.choices(l9))        
    exercise10=str(random.choices(l10))        
    exercise11=str(random.choices(l11))        
    exercise12=str(random.choices(l12))        
    for i in l:
        if i[1]== exercise1:
            ex_dur1=cal_muscle//i[3],"minutes"
        elif i[1]== exercise2:
            ex_dur2=cal_muscle//i[3],"minutes"
        elif i[1]== exercise3:
            ex_dur3=cal_muscle//i[3],"minutes"
        elif i[1]== exercise4:
            ex_dur4=cal_muscle//i[3],"minutes"
        elif i[1]== exercise5:
            ex_dur5=cal_muscle//i[3],"minutes"
        elif i[1]== exercise6:
            ex_dur6=cal_muscle//i[3],"minutes"
        elif i[1]== exercise7:
            ex_dur7=cal_muscle//i[3],"minutes"
        elif i[1]== exercise8:
            ex_dur8=cal_muscle//i[3],"minutes"
        elif i[1]== exercise9:
            ex_dur9=cal_muscle//i[3],"minutes"
        elif i[1]== exercise10:
            ex_dur10=cal_muscle//i[3],"minutes"
        elif i[1]== exercise11:
            ex_dur11=cal_muscle//i[3],"minutes"
        elif i[1]== exercise12:
            ex_dur12=cal_muscle//i[3],"minutes"    
    l_workout={ex_dur1:exercise1,ex_dur2:exercise2,ex_dur3:exercise3,ex_dur4:exercise4,ex_dur5:exercise5,ex_dur6:exercise6,ex_dur7:exercise7,ex_dur8:exercise8,ex_dur9:exercise9,ex_dur10:exercise10,ex_dur11:exercise11,ex_dur12:exercise12}   
    print("your personal workout:",l_workout)  
