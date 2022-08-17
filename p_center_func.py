from turtle import Vec2D
import math

def isclose(a, b, rel_tol=1e-06, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    
class Vec2D:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y);
    def __eq__(self, v):
        return isclose(self.x, v.x) and isclose(self.y, v.y)
    def __add__(self, v):
        return Vec2D(self.x + v.x, self.y + v.y)
    def __sub__(self, v):
        return Vec2D(self.x - v.x, self.y - v.y)
    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar):
        return Vec2D(self.x / scalar, self.y / scalar)
    def coordinate(self):
        return self.x, self.y

    
# length^2
def len2(v):
    return v.x*v.x + v.y*v.y;

def distance(v1, v2):
    return math.sqrt(len2(v1 - v2))

# true if point is outside of the circle
def outside(v1, v2, r):
    return math.sqrt(len2(v1 - v2)) > r;    

#cross product of two vectors. Used to test the collinearity
def cross(v1, v2):
    return v1.x*v2.y - v1.y*v2.x;

def circle(*args):
    if len(args) == 2:
        return (args[0]+args[1])/2, math.sqrt(len2(args[0]-args[1]))/2.0
    elif len(args) == 3:
        p1, p2, p3 = args[0], args[1], args[2]
        slope1 = (p1.y - p2.y)/(p1.x - p2.x)
        slope2 = (p1.y - p3.y)/(p1.x - p3.y)
        c, r = 0,0
        #collinear
        if (slope1 == slope2):
            c, r = circle(p1, p2)
            tmp_c, tmp_r = circle(p1, p3)
            if (tmp_r > r):
                c = tmp_c;
                r = tmp_r;
            tmp_c, tmp_r = circle(p2, p3)
            if (tmp_r > r):
                c = tmp_c;
                r = tmp_r;
            return c, r;
        
        pa = (p1 + p2) / 2;
        pb = (p1 + p3) / 2;
        va = Vec2D(p1.y-p2.y, p2.x-p1.x);
        vb = Vec2D(p1.y-p3.y, p3.x-p1.x);
        delta = cross(va, vb)
        t = ((pb.x-pa.x)*vb.y - (pb.y-pa.y)*vb.x) / delta;
        c = pa + va*t;
        r = math.sqrt(len2(c-p1));
        return c, r;
    else:
        print("arg number error")
    

# reutrn (center, radiuis)
def smallest_enclosing_circle(pts):
    c, r = Vec2D(1e6,1e6), 0.0;
    for i in range(len(pts)):
        if outside(pts[i], c, r):
            c = pts[i]
            r = 0.0;
            for j in range(i):
                if outside(pts[j], c, r):
                    # pi and pj must be on boundary
                    c, r = circle(pts[i], pts[j])
                    for k in range(j):
                        if outside(pts[k], c, r):
                            c, r = circle(pts[i], pts[j], pts[k])

    return c, r;