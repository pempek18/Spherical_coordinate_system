import numpy as np
import matplotlib.pyplot as plt 
# import sqrt from math module
from math import sqrt
from Spherical import Spherical

# Function check whether a number
# is prime or not
def isPrime(n):
    # Corner case
    if (n <= 1):
        return False
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

s = Spherical(False)

for i in range(1,10000):
    if isPrime(i) :
        x = s.x(i, np.pi /2, i)
        y = s.y(i, np.pi /2, i)
        plt.scatter(x=x, y=y)
plt.show()