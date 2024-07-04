# check = input("Hey you have a banana do you want to test its ripness: ")
# if check == yes :
#     colour = input("Tell me color of Banana : ")
#     if colour == green:
#          print("It looks banana is unripe")

#     elif colour == Yellow:
#         print("It looks banana is ready to eat its completely ripe")

#     elif colour == brown:
#         print("It looks banana is not good to eat its  overripe")

#     else :
#         print("choose colour between yellow, green ,brown other colour are not present in banana ")
# else :
#     print("if you select yes then only i will test otherwise i will not test ")

check = input("Hey, do you have a banana? Would you like to test its ripeness? (yes/no): ")

if check.lower() == "yes":
    colour = input("Tell me the color of the banana (green/yellow/brown): ").lower()

    if colour == "green":
        print("It looks like the banana is unripe.")

    elif colour == "yellow":
        print("It looks like the banana is ready to eat; it's completely ripe.")

    elif colour == "brown":
        print("It looks like the banana is overripe and not good to eat.")

    else:
        print("Please choose a color between green, yellow, or brown. Other colors are not present in bananas.")

else:
    print("If you select 'yes,' I will test the banana. Otherwise, I won't test it.")
