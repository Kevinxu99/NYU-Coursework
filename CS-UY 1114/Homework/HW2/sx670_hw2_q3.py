aside=int(input())
bside=int(input())
angle=int(input())
import turtle
import math
turtle.forward(aside)
turtle.left(180-angle)
turtle.forward(bside)
a1=180-angle
cside=math.sqrt(aside*aside+bside*bside-2*aside*bside*math.cos(math.radians(angle)))
ca=-(aside*aside-bside*bside-cside*cside)/(2*bside*cside)
sa=math.sqrt(1-(ca*ca))
turtle.left(180-math.degrees(math.asin(sa)))
turtle.forward(cside)
