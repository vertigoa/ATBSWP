def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = (3 * number + 1)
print(number)
return number