import math

n = 4
l = 25

p = n * l
ap = l * 0.5 / math.tan(180/n)
s = 0.5 * p * ap
print(s)