# WAP to check whether a number is positive, negative or zero
# If positive, check whether it is even or odd using nested if

no = int(input("Enter any number: "))

if no > 0:
    print("Number is Positive")

    if no % 2 == 0:
        print("It is an Even number")
    else:
        print("It is an Odd number")

elif no < 0:
    print("Number is Negative")

else:
    print("Number is Zero")
