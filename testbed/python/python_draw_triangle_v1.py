
"""
Date : 30.5.2020
By: Ali
Wesite: ahradwani.com

Project: To Draw a Right angle Triangle.  
Version : V1  (3.June.2020)


Details:
        The system will ask the user to Enter the cordenates
        of two points To draw a Right Angle Triangle. In our Trianles,
        we will call the (x1,y1) as Point A, and (x2,y2) as Point C.

        From our starting poins we can calculate the thired point as following:
        tri_opposite = abs( y2 - y1 )
        tri_adjacent = abs( x2 - x1 )

        The system then will detearmin the following:

        The Adjacent
        The Opposite
        The Hypotenuse

        From a mathimatics triangle formula we know that:

        Opposite^2 + Adjacent^2 = Hypotenuse^2
        where: x^2 = square(x)

        So:
            tri_hypo = tri_opposite**2 + tri_adjacent**2
            tri_hypo = math.sqrt(tri_hypo)

            tri_hypo is the distance between point A and point C.

        Also we now that in a Right Triangle we will have a 90 degree angle (ABC) and first thing
        we are looking to calculate the Opposite angle (BAC).

        tri_opposite = abs( y2 - y1)
        tri_adjacent = abs(x2 -x1)
        the_deg = tri_opposite /  tri_adjacent

        we need the inverse of Tan(the_deg)
        the_ang BAC = math.degrees(math.atan(the_deg)) 
        

        Triangle has three heads (angles), the summation of the angles are 180deg
        in the right triangle we always have one 90deg angle, so we will calculate the other angels.


"""

import turtle, math


#turtle_setting
t = turtle.Turtle()
t.shape("non")
t.speed(9)
t.speed('fastes')
t.visible = False
t.penup()
t.hideturtle()


def the_cross() :
    # The cross to draw the cross represent the cordenate
    t.penup()
    t.pencolor('gray')
    t.goto(-200,0)
    t.setheading(0)
    t.pendown()
    t.forward(400)
    t.penup()
    t.goto(0,200)
    t.setheading(90)
    t.pendown()
    t.forward(-400)
    t.penup()
    t.goto(2,0)
    t.pendown()
    t.circle(2)
    t.penup()
    t.goto(0,0)
    t.setheading(0)


the_cross()  # To draw the croos



def draw_triangle(x1, y1, x2, y2) :
    
    # draw the triang
    style = ('Courier', 20) # font style
    t.penup()
    t.goto(x1,y1)
    t.setheading(0)
    t.pendown()
    t.circle(1)   # To draw small circle on point A.
    
    t.write('A',font = style)   # To write A next to the point.
    t.forward((x2-x1))
    x3 = t.xcor()
    y3 = t.ycor()

    t.right(-90)
    t.forward((y2-y1))
    t.write('C',font = style)   # To write C next to the point.
    t.goto(x2,y2)
    t.setheading(0)
    t.pendown()
    t.circle(1)   # To draw small circle on point C.
    t.penup()
    t.goto(x3,y3)
    t.pendown()
    t.circle(1)    # To draw small circle on point B.
    t.penup()
    t.setpos(x3-15,y3-15)
    t.write('B',font = style)   # To write B next to the point.


    # To calculate the angle of BAC using Triangle Math Equations.
    tri_opposite = abs( y2 - y1)
    tri_adjacent = abs(x2 -x1)
    the_deg = tri_opposite /  tri_adjacent

    
    # get the inverse ot Tan using Triangle Math Equations.     
    the_ang = math.degrees(math.atan(the_deg))

    t.goto(x1,y1)
    
    # To correct the rotation angle based on it's coordinates.
    if (x1 > x3) and (y2 > y1) :
      rotation = the_ang - 180 
      
    elif (x1 < x3) and  (y2 > y1):
      rotation =  360 - the_ang

    elif (x1 > x3) and  (y2 < y1) :
      rotation =  180 - the_ang

    elif (x1 < x3) and  (y2 < y1) :    
      rotation =   the_ang - 360



    t.right(rotation)
    t.pendown()

    # From using Triangle Math Equations, we know that Hypotenuse^2 = Opposite^2 + adjacent^2. 
    tri_hypo = tri_opposite**2 + tri_adjacent**2
    tri_hypo = math.sqrt(tri_hypo)
    
    t.forward(tri_hypo)
    t.penup()

    print('\n  The Triangle Information:')
    print('  Point A= ({},{})'.format(x1,y1))
    print('  Point B= ({},{})'.format(x3,y3))
    print('  Point C= ({},{})'.format(x2,y2))
    print('  Adjacent',tri_adjacent)
    print('  Opposite',tri_opposite)
    print('  Hypotenuse',tri_hypo)
    print('  Angle: ABC = 90')
    print('  Angle: BAC = ',the_ang)
    print('  Angle: ACB = ',180 - the_ang - 90)

  

print('\n   To draw the Triangle you need to Enter Two Points as X,Y for each one.')
x1 = int(input('   Enter x for first point'))
y1 = int(input('   Enter y for first point'))
x2 = int(input('   Enter x for second point'))
y2 = int(input('   Enter y for second point'))



t.pencolor('green')
if (x2==x1) or (y2==y1) :
   print('  Your Points are not valid, (x1,x2) or (y1,y2) can''t be equal ')
else :
   draw_triangle(x1, y1, x2, y2)













