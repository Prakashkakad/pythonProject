number = int(input("Please Enter your number i will check its Prime number : "))
is_prime = True

if number > 1:
    for i in range(2,number):
        if ( number % i ) == 0:
            is_prime = False
            break

print("Number is  Prime",is_prime)