firstInteger = int(input("Enter the first integer: "))
secondInteger = int(input("Enter the second integer: "))
thirdInteger = int(input("Enter the third integer: "))

if firstInteger>secondInteger:

    if firstInteger>thirdInteger:
        print(firstInteger)
    else:
        print(thirdInteger)
else:
    if secondInteger>thirdInteger:
        print(secondInteger)
    else:
        print(thirdInteger)