num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    i = 2
    is_prime = True

    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
