age = int(input("Please Enter your age : "))
print("The Given Age is", age)

if age < 13:
    print("This age is of child ")

elif age >= 13 and age <=19:
    print("The Given age is of Teenager")

elif age >= 20 and age <=59:
    print("The Given age is of Adult")

else:
    print("The Given age is of Teenager")



print ("What is your Age ",age)
day=(input("What the day today ???"))

price = 12 if age >=18 else 8
if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket Price for you is $", price)
