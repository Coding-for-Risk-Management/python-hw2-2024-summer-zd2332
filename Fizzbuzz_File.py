import numpy as np
#getFizzbuzz
def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = "fizzbuzz"
    objvec[(numvec % 3 == 0) & (numvec % 5 != 0)] = "fizz"
    objvec[(numvec % 5 == 0) & (numvec % 3 != 0)] = "buzz"
    
    return objvec

# Test values
start = 16
finish = 30

# Calculate FizzBuzz
result = FizzBuzz(start, finish)
print(result)
