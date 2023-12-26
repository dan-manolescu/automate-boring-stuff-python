# The Collatz sequence (or "the simplest impossible math problem").

def collatz(number):
    if number % 2 == 0: # The number is even.
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return result

stop = False
while not stop:
    print('Enter a strictly positive number:')
    try:
        number = int(input())
        if number > 0:
            stop = True
        else:
            print('Number is not strictly positive!')
    except ValueError:
        print('Not a number!')

iterations = 0
while number != 1:
    number = collatz(number)
    iterations += 1

print('Finished after %s iterations' % iterations)
