#TASK1
import math
# calculating the other side of right-angled triangle
side1 = input('Please enter side 1 of triangle: ')
side2 = input('Please enter side 2 of triangle: ')
side3 = float(side1)**2 + float(side2)**2 #or (side1+side2)**2
print("side 3 of triangle:" + str(math.sqrt(side3))) #instead of math.sqrt just do **2

#calculating area and displaying in binary form
area = float(side1) * float(side2) / 2
print("Area of triangle is: " + str(area))
print("Binary digit of area is: " + str(bin(int(area))))


#TASK2
mynumbers = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
mynumbers.sort()
print("The first number on the list is: " + str(mynumbers[0]))
print("The last number of the list is: " + str(mynumbers[-1]))


