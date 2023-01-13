

ned=1
øvre=5
n=10


def f(x):
    return x**2-2*x+2

summen=0
delta_x=(øvre-ned)/n


for i in range(n):
    summen=summen+f(ned+i*delta_x)*delta_x

print(round(summen,2))
