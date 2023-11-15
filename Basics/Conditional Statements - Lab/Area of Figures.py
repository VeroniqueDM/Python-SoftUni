figure=input()
if figure=="square":
    side=float(input())
    area=float(side*side)
    print(round((area), 3))
if figure=="rectangle":
    length=float(input())
    width=float(input())
    area=float(length*width)
    print(round((area), 3))
if figure=="circle":
    from math import pi
    radius=float(input())
    area=float(radius*radius*pi)
    print(round((area), 3))
if figure=="triangle":
    base=float(input())
    height=float(input())
    area= float((base*height)/2)
    print(round((area), 3))