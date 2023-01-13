
import math
ned=0
øvre=2
n=10


def f(x):
    return math.sqrt(4-x**2)


summen=0
delta_x=(øvre-ned)/n


for i in range(n):
    summen=summen+f((ned+delta_x)+i*delta_x)*delta_x

print(summen,2)
