def multiplo(n):
    for c in range(1, n+1):
        if c % 3 == 0 and c % 5 == 0:
            print('FizzBuzz.')
        elif c % 3 == 0 and c % 5 != 0:
            print('Fizz.')
        elif c % 5 == 0 and c % 3 != 0:
            print('Buzz.')
        else:
            print(c)

multiplo(15)