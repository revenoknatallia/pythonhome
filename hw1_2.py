import mathlib
import math4python
import math

print("---------------------------задание 2 вариант 11 --------------------------------")
a=-1.4
m=16
j=[0.5,9.1,5]
l=len(j)

print("math.exp(a/m)=" + str(math.exp(a / m)))
w= math.tan(a/3) + math.exp(a/m)
print("в радианах w=" + str(w))
w= math.tan(math.radians(a/3)) + math.exp(a/m)
print("в градусах w=math.tan(math.radians(a/3)) + math.exp(a/m)  w=" + str(w))

print("---------------------------for--------------------------------")
for i in range(l):
     print("j=" + str(j[i]))
     r = 0.9*math.sqrt(w+j[i]) + (math.pow(a,2)-1)
     print("r= 0.9*math.sqrt(w+j[i]) + (math.pow(a,2)-1)=" + str(r))
print("---------------------------while--------------------------------")
j=1.8
while j <= 3:
    print("j=" + str(j))
    r = 0.9 * math.sqrt(w + j) + (math.pow(a, 2) - 1)
    print("r= 0.9*math.sqrt(w+j) + (math.pow(a,2)-1)=" + str(r))
    j+=0.2

print("---------------------------double for--------------------------------")
a=[0.2,-4,0.6]
l1=len(a)
j=[0.1,0.1,0.4]
l2=len(j)
for i in range(l1):
    print("a=" + str(a[i]))
    w = math.tan(math.radians(a[i] / 3)) + math.exp(a[i] / m)
    print("в градусах w=math.tan(math.radians(a/3)) + math.exp(a/m)  w=" + str(w))

    for x in range (l2):
        print("j=" + str(j[x]))
        r = 0.9 * math.sqrt(w + j[x]) + (math.pow(a[i], 2) - 1)
        print("r= 0.9*math.sqrt(w+j[i]) + (math.pow(a,2)-1)=" + str(r))
