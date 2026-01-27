point = (3, 5)
point2 = (7, 2)

print("Point 1:", point)
print("Point 2:", point2)

x1, y1 = point
x2, y2 = point2

print("X1:", x1, "Y1:", y1)
print("X2:", x2, "Y2:", y2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance between points:", distance)

string = "PYTHON"
str_tuple = tuple(string)
for char in str_tuple:
    print(char)
