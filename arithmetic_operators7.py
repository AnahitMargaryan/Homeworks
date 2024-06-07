# Exercise 7. You are given four real numbers - the coordinates of two points on a
# plane. The first two numbers are the x and y coordinates of the first point,
# and the last two numbers are the x and y coordinates of the second point.
# Output the length of the line segment bounded by the two points.


x1 = 1
y1 = 2.2
x2 = 2.5
y2 = -1.5
    
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Length of the line segment between the two points:", distance)

