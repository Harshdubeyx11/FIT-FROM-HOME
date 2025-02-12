FOOD=input("Enter your food item")
QUANTITY=int(input("Enter the quantity of food item in grams"))
CARBOHYDRATES=float(input("Enter carbohydrates in food item per 100 g"))
PROTIENS=float(input("Enter protiens in food item per 100 g"))
FATS=float(input("Enter fats in food item per 100 g"))
FIBER=float(input("Enter fiber in food item per 100 g"))
def CALORIE_CALC(CARBOHYDRATES,PROTIENS,FATS,FIBER):
    cal=(4*CARBOHYDRATES)+(4*PROTIENS)+(9*FATS)+(2*FIBER)
    print("TOTAL CALORIES IN",QUANTITY,"g",FOOD,"=",(QUANTITY/100)*cal)
CALORIE_CALC(CARBOHYDRATES,PROTIENS,FATS,FIBER)   
    
    
