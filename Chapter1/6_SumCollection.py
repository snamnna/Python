sum = 0

while True: 
    number = input()
    if number.isnumeric():
        numberToFloat = float(number)
        if numberToFloat == 0:
            print("The grand total is", sum)
            break

        sum += numberToFloat
        print("The total is now", sum)
    else:
        print("That wasn’t a number.")