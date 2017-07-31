def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


while True:
    n = input('> ')
    try:
        while n != 1:
            n = collatz(int(n))
            print
            n
    except ValueError:
        print
        'Input must be an integer'