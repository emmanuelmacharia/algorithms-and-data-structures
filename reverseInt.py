'''reverse an integer'''


def reverser(x):
    my_Str = str(x)
    reversedInt = 0
    if x < 0:
        iterator = len(my_Str) - 1
        modulus = -10
    else:
        iterator = len(my_Str)
        modulus = 10

    while iterator != 0:
        print(f"my iterator == {iterator}")
        reversedInt = reversedInt * 10
        print(f"reversedInt after multiplying by 10 == {reversedInt}")
        print(f"heres the modulo --> {x % modulus}")
        if x < 0:
            reversedInt = reversedInt - x % modulus
            print(f"reversedInt after addition by modulo == {reversedInt}")
            x *= -1
            x //= modulus
            print(f"here's x: {x}")
        else:
            reversedInt = reversedInt + x % modulus
            print(f"reversedInt after addition by modulo == {reversedInt}")
            x //= modulus
            print(f"here's x: {x}")
        iterator -= 1
    return reversedInt


print(reverser(-321))
