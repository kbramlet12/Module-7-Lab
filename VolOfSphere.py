#===============================================================================
#Program Name: VolOfSphere
# Name: Keegan Bramlet
# Date: 11/28
# Purpose of a Program: Print the volume of a sphere, given a radius
#===============================================================================
import math
pi = math.pi
 
def volume(r):
    vol = (4 / 3) * pi * r * r * r
    return vol

radius = float(input("What is the radius?"))
print( "Volume Of Sphere : ", volume(radius))
