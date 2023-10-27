num = int(input())
if num < 0:
    print("Please enter positive number")

sum = num * (num + 1)/2
print("The sum of the first", num, "positive integers is", int(sum))