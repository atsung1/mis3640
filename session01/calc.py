#Session 1 exercise 1
#question 1:2562s
# print(42*60+42)
#question 2:6.21miles
# print(10/1.61)
#question 3:
# a=42*60+4
# b=10/1.61
# time per mile in seconds:406.364
# print(a/b)
#time per mile in minutes:6.772
# c=a/b
# print(c/60)
#average speed in miles per hour: 8.859
# d=a/60/60
# print(b/d)

#Session 2 Exercise 1
#question 1: What is the volume of a sphere with radius 5?
import math
r = float(input('What is the radius?'))
V = 4/3*math.pi*r**3
print('The volume is {}'.format(V))

#question 2: Total wholesale cost
b = int(input('How many books?'))
c = b*24.95*0.60-3-0.75*b
print('The total wholesale cost for 60 copies is ${:.2f}'.format(c))

#question 3:time
start = 6*60+52
start_s = start*60
e = 8*60+15
t = 7*60+12
dur = 2*e + 3*t
end = start_s+dur
end_h = end/(60**2)
end_m = (end_h-int(end_h))*60
print('Breakfast is {:d}:{:d}am'.format(int(end_h), int(end_m)))

#question 4: grade
g = ((89-82)/82)*100
print('The percentage increase of my grade is {:.1f}%'.format(g))