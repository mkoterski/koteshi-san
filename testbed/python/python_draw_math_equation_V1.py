
"""

Project: Draw Math Equation
By: Ali
Date: 9.6.2020
Version: V1-9.6.2020


Detail:
	To draw lines using the draw_line function and Mathimatical Equations.



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



def draw_line(x1, y1, x2, y2):

  t.goto(x1,y1)
  t.pendown()
  t.goto(x2,y2)
  t.penup()



def get_points() :
  p = int(input('  Enter number of Points:  ') )# number of points

  arc_angle = 360 / p
  circle_r = int(input('  Enter the Cricle Radius: ') )
  fix_r = int(input('  Enter a number to reduce the Radius:'))

  #To return the x,y list of the points that we want to connec
  p_list = []
  t.goto(0,0)
  t.setheading(-90)

  for p in range (0,p+1) :

    t.goto(0,0)
    t.forward(circle_r)
    nx = t.xcor()
    ny = t.ycor()

    # If the user want to reduce the radius
    circle_r = circle_r - fix_r
    p_list.append([nx,ny])
    t.right(-arc_angle)

  return p_list



p_list = get_points()


for d in range(len(p_list)-1) :

  # you can change the equations e1, e2  
  e1 = int(d/2)
  e2 = 1  # abs( len(p_list)) -int(d/2)

  try:
    draw_line(p_list[d][0], p_list[d][1],p_list[e1][0], p_list[e1][1])
    print(d, int(d/2) )
  except:
    if e1 > len(p_list) :  # you can change this condition if you want 
      draw_line(p_list[d][0], p_list[d][1],p_list[e2][0], p_list[e2][1])




# Sample of e1, e2 and output shapes are in the post on my website
# www.ahradwani.com

