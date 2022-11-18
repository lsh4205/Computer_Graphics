# Seonghyun Lee
# GT ID: 903452500
class PVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "PVector(%f, %f, %f)" % (self.x, self.y, self.z)

    def __add__(self, other):
        return PVector.add(self, other)

    def __mul__(self, n):
        return PVector.mult(self, n)

    def __rmul__(self, n):
        return PVector.mult(self, n)

    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def copy(self):
        return PVector(self.x, self.y, self.z)

    def div(self, n):
        return PVector(
            a.x / n,
            a.y / n,
            a.z / n,
        )

    @staticmethod
    def dist(a, b):
        return PVector.sub(a, b).mag()

    @staticmethod
    def add(a, b):
        return PVector(
            a.x + b.x,
            a.y + b.y,
            a.z + b.z,
        )

    @staticmethod
    def sub(a, b):
        return PVector(
            a.x - b.x,
            a.y - b.y,
            a.z - b.z,
        )

    @staticmethod
    def mult(a, n):
        return PVector(
            n * a.x,
            n * a.y,
            n * a.z,
        )

    @staticmethod
    def pairwise_mult(a, b):
        return PVector(
            a.x * b.x,
            a.y * b.y,
            a.z * b.z,
        )

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def cross(a, b):
        return PVector(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x,
        )

    def normalize(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self
## Light Class
## self.pos : light position
## self.r : light color Red
## self.g : light color Green
## self.b : light color Blue
class Light(object):
    def __init__(self, pos, r, g, b):
        self.pos = pos
        self.r = r 
        self.g = g
        self.b = b

## Ray Class
## self.origin : Vector - Eye origin
## self.direc : Vector - Ray direciton 
class Ray(object):
    def __init__(self, origin, direc):
        self.origin = origin
        self.direc = direc

    def __repr__(self):
        return 'Ray=[Ray_origin: {}, Ray_direction: {}]'.format(self.origin, self.direc)

    def parametric_eq(self, t):
        ray_eq = PVector.mult(self.direc, t)
        P = PVector.add(self.origin, ray_eq)
        # ray_eq = ray_eq.add(self.origin)
        return P

## Surface Class
## self.dr : Diffuse color Red
## self.dg : Diffuse color Green
## self.db : Diffuse color Blue
class Surface(object):
    def __init__(self, dr,dg,db, ar,ag,ab, sr,sg,sb, spec_power, k_refl):
        self.dr = dr
        self.dg = dg
        self.db = db

        self.ar = ar
        self.ag = ag
        self.ab = ab

        self.sr = sr
        self.sg = sg
        self.sb = sb

        self.spec_power = spec_power
        self.k_refl = k_refl

    def __repr__(self):
        return 'Surface=[dr: {}, dg: {}, db: {}]'.format(self.dr, self.dg, self.db)

## Sphere Class
## self.radius : Scalar - radius value
## self.center : Vector - center coordinate
## self.surface : Surface class
class Sphere(object):
    def __init__(self, radius, center, surface):
        self.radius = radius
        self.center = center 
        self.surface = surface

    def __repr__(self):
        return 'Sphere=[radius: {}, center_loc: {}, surface: {}]'.format(self.radius, self.center, self.surface)

    def intersect(self, ray):
        # A = D ^ 2
        # B = 2D (O - C)
        # C = |O - C| ^ 2 - R ^ 2 
        
        # D = Ray direction
        # O = Origin
        # C = Location of the Center of the Sphere
        # R = Radius of Sphere
        diff = PVector.sub(ray.origin, self.center)
        A = PVector.dot(ray.direc, ray.direc)
        B = 2 * PVector.dot(ray.direc, diff)
        # B = 2 * (ray.direc.dot(diff))
        C = PVector.dot(diff, diff) - self.radius ** 2
        # C = diff.dot(diff) - self.radius ** 2
        
        d = B*B - 4*A*C
        self.A = A
        self.B = B
        self.C = C
        t = 0
        # Two Solution
        if d > 0:
            t0 = (-B + sqrt(d)) / (2 * A)
            t1 = (-B - sqrt(d)) / (2 * A) 
            if t0 < 0 and t1 < 0:
                return None
            elif t0 < 0:
                t = t1
            elif t1 < 0:
                t = t0
            else:
                t = min(t0,t1)
        # One Solution
        elif d == 0: 
            t = (-B)/ 2*A
        # There is No Solution (intersection)
        else:
            return None
        P = ray.parametric_eq(t)
        N = PVector.sub(P, self.center)
        N.normalize()
        self.normal_v = N

        return Hit(self, t, ray, P, N)
    
class Triangle(object):
    def __init__(self, a, b, c, surface):
        self.a = a
        self.b = b
        self.c = c

        self.ab = PVector.sub(b, a) # precompute the sides of the triangle
        self.bc = PVector.sub(c, b)
        self.ca = PVector.sub(a, c)
        self.normal_v= (PVector.cross(self.ab, self.bc)).normalize()
        self.surface = surface

    def intersect(self, ray):
        t = 0
        denom = PVector.dot(self.normal_v, ray.direc)
        # Demonimator first
        # 1. There is a Hit/Intersection 
        if denom == 0:
            return None 
        # 2. There is a Hit/Intersection
        temp = PVector.dot(self.normal_v, PVector.sub(self.a, ray.origin))
        t = temp / denom
        if t < 0:
            return None
        P = ray.parametric_eq(t)
        

        ap = PVector.sub(P, self.a)
        bp = PVector.sub(P, self.b)
        cp = PVector.sub(P, self.c)

        triple1 = PVector.dot(PVector.cross(ap, self.ab), self.normal_v)
        triple2 = PVector.dot(PVector.cross(bp, self.bc), self.normal_v)
        triple3 = PVector.dot(PVector.cross(cp, self.ca), self.normal_v)
        
        if ((triple1 > 0) == (triple2 > 0) == (triple3 > 0)):
            v = self.normal_v
            if denom > 0:
                # normal_v= -1 * normal_v5
                v = PVector.mult(self.normal_v, -1)
            return Hit(self, t, ray, P, v)
        else: return None

## Hit Class
## self.sphere : Sphere Class
## self.t : Scalar - t-value
## self.ray : Ray Class
## self.intersect : Vector - intersection point
## self.norm : Vector - normalize(intersect - sphere.center location)
class Hit(object):
    def __init__(self, shape, t, ray, intersect, normal_v):
        self.shape = shape
        self.t = t
        self.ray = ray
        self.intersect = intersect
        self.normal_v= normal_v
        self.surface = shape.surface

    def __repr__(self):
        return '{}, t: {}, {}, intersection_pt: {}, normal: {}'.format(self.shape, self.t, self.ray, self.intersect, self.normal_v)
