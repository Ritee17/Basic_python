# area of triangle using heron's formula where sides are entered by the user 
side1=int(input("Enter the first side of the triangle:"))
side2=int(input("Enter the second side of the triangle:"))
side3=int(input("Enter the third side of the triangle:"))
s=(side1+side2+side3)/2
area=((s*(s-side1)*(s-side2)*(s-side3))**0.5)
print("The area of the triangle is",area)
