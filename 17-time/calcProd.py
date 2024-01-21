#! python3
# calcProd.py - Calculate time it takes to loop through all integers from 1 to 99,999 and return their product.

import time, sys

# To prevent ValueError: Exceeds the limit (4300) for integer string conversion
sys.set_int_max_str_digits(0)

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100_000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

