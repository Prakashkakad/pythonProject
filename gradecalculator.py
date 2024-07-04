score = int(input("Tell What is your Score I will tell you your Grade :-"))

if score >= 101:
    print("please Enter Vaild Score")
    exit()
    
print("Nice You have Good Score", score)

if score >=90 or score <=100:
    print("You have Grade  A ")

elif score >=80 or score <=89:
    print("You have Grade  B ")

elif score >=70 or score <=79:
    print("You have Grade  C ")

elif score >=60 or score <=69:
    print("You have Grade  D ")

else:
    print("You have Grade F ")


