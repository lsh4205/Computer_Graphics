# Seonghyun Lee
# GT ID: 903452500

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
		ray_eq = PVector.add(ray_eq, self.origin)
		# ray_eq = ray_eq.add(self.origin)
		return ray_eq

## Surface Class
## self.dr : Diffuse color Red
## self.dg : Diffuse color Green
## self.db : Diffuse color Blue
## TODO: need to add other color variables for 3B
class Surface(object):
	def __init__(self, dr, dg, db):
		self.dr = dr
		self.dg = dg
		self.db = db
	
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
	
	def canonical_sphere_interesect(self, ray):
		# A = D ^ 2
		# B = 2D (O - C)
		# C = |O - C| ^ 2 - R ^ 2 
		
		# D = Ray direction
		# O = Origin
		# C = Location of the Center of the Sphere
		# R = Radius of Sphere
		diff = PVector.sub(ray.origin, self.center)

		A = ray.direc.dot(ray.direc)
		B = 2 * (ray.direc.dot(diff))
		C = diff.dot(diff) - self.radius ** 2
		
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
				return t1
			elif t1 < 0:
				return t0
			else:
				t = min(t0,t1)
		# One Solution
		elif d == 0: 
			t = (-B)/ 2*A
		# There is No Solution (intersection)
		else:
			return None
		return t

## Hit Class
## self.sphere : Sphere Class
## self.t : Scalar - t-value
## self.ray : Ray Class
## self.intersect : Vector - intersection point
## self.norm : Vector - normalize(intersect - sphere.center location)
class Hit(object):
	def __init__(self, sphere, t, ray, intersect):
		self.sphere = sphere
		self.t = t
		self.ray = ray
		self.intersect = intersect

		norm = PVector.sub(self.intersect, self.sphere.center)
		# norm = self.intersect.sub(self.sphere.center)
		self.norm = norm.normalize()
	def __repr__(self):
		return '{}, t: {}, {}, intersection_pt: {}, normal: {}'.format(self.sphere, self.t, self.ray, self.intersect, self.norm)
	