def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    # print("Name ", name ,"Power: ",power)



print_kwargs(name="Pakash",power ="lazer")
print_kwargs(name="Pakash",power ="lazer",Enmy = "Fighter")