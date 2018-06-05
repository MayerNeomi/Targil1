#Neomi Mayer 328772801

#  Example program for Targil 1
#
import math
from myboolfuncs import *
#
# Area calculation program

def squareArea(a):
     return a*a

def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
 
def sphereArea(r):
    return 4 * math.pi * r**2        

def coneArea(r,h):
    return math.pi * r * (r+ math.sqrt(h**2 + r**2))

def squarepyramidArea(h,a):
    return a**2 + 2 * a * math.sqrt(a**2/4 + h**2)
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle","Square","Sphere","Cone","Square Pyramid")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
         length = getNumber("Please enter the length: ")
         area = squareArea(length)
         print ("The area is", area)
    elif shape == "4":
         radius = getNumber("Please enter the radius: ")
         area = sphereArea(radius)
         print ("The area is", area)
    elif shape == "5":
        radius = getNumber("Please enter the radius: ")
        height = getNumber("Please enter the height: ")
        area = coneArea(radius,height)
        print ("The area is", area)
    elif shape == "6":
        height = getNumber("Please enter the height: ")
        length = getNumber("Please enter the length: ")
        area = squarepyramidArea(height,length)
        print ("The area is", area)
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
