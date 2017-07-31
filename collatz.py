def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        number = number // 2
        return number
    else:
        print(str(3 * number + 1))
        number = (3 * number + 1)
        return number
n = int(input('Please give me a number: '))
if n == 1:
    while n == 1:
        n = int(input('Please give me a number besides 1: '))
while n != 1:
    n = collatz(int(n))