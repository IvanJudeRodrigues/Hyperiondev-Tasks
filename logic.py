#  this is an example of a logical error
import math
# initialise area of triangle
area_of_triangle=0
# inform user you will calculate area of your right-angled triangle
print("To find the area of your right-angled triangle")
# ask for length of hypotenuse
hypotenuse=int(input("what is the length of the hypotenus in centimetres."))
# ask for length of one of the other sides
other_side = int(input("what is the length of one of the other side."))
# work out length of the left over side using the formula
leftover_side = (hypotenuse**2-other_side**2)**0.5
# calculate area of triangle using formula 1/2base times height
# this is the logical error.Hypotenuse is used instead of other side
area_of_triangle=float(1/2*hypotenuse*leftover_side)
# print area of triangle
print(f"the area of your right-angled triangle is{area_of_triangle} cm squared.")
