def prime(prime_no):
    for i in range(2,prime_no):
        if prime_no % i == 0 and i != prime_no:
            print("Not Prime")
            break
        else:
            print("Prime")
            break


prime(8)