firstInteger = input("Enter the first integer: ")
secondInteger = input("Enter the second integer: ")
thirdInteger = input("Enter the third integer: ")

if firstInteger>secondInteger:

    if firstInteger>thirdInteger:
        print(firstInteger)
    else:
        print(thirdInteger)

else:
    if secondInteger>thirdInteger:
        print(secondInteger)

print(thirdInteger)