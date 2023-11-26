import matplotlib.pyplot as plt
import math

def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return {}
    # One circle within other
    if d < abs(r0-r1):
        return {}
    # coincident circles
    if d == 0 and r0 == r1:
        return {}
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 
        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        return x3, y3, x4, y4

# intersection circles
x0, y0 = 0, 0
r0 = 5
x1, y1 = 2, 2
r1 = 5

# intersecting with (x1, y1) but not with (x0, y0)
x2, y2 = -1,0
r2 = 2.5

circle1 = plt.Circle((x0, y0), r0, color='b', fill=False)
circle2 = plt.Circle((x1, y1), r1, color='b', fill=False)
circle3 = plt.Circle((x2, y2), r2, color='b', fill=False)

fig = plt.figure(figsize = (10, 10)) 
plt.grid(True)
ax = fig.add_subplot(111)

ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

intersections1 = get_intersections(x0, y0, r0, x1, y1, r1)
print(intersections1)
if len(intersections1) > 0:
    print(intersections3)
    i_x3, i_y3, i_x4, i_y4 = intersections1 
    #plt.plot([i_x3, i_x4], [i_y3, i_y4], 'o', color='r')
    ax.scatter([i_x3, i_x4],[i_y3, i_y4] ,marker ='X',s=300,alpha=1)

intersections2 = get_intersections(x0, y0, r0, x2, y2, r2)
print(intersections2)
if len(intersections2) > 0:
    i_x3, i_y3, i_x4, i_y4 = intersections2 
    plt.plot([i_x3, i_x4], [i_y3, i_y4], 'o', color='r')
    ax.scatter([i_x3, i_x4],[i_y3, i_y4] ,marker ='X',s=300,alpha=1)

intersections3 = get_intersections(x1, y1, r1, x2, y2, r2)

if len(intersections3) > 0:
    print(intersections3)
    i_x3, i_y3, i_x4, i_y4 = intersections3 
    #plt.plot([i_x3, i_x4], [i_y3, i_y4], 'o', color='r')
    ax.scatter([i_x3, i_x4],[i_y3, i_y4] ,marker ='X',s=300,alpha=1)
plt.gca().set_aspect('equal', adjustable='box')
