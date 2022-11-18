# Seonghyun Lee
# GT ID: 903452500

from shapes import *

class ShipBody:
	log_factor = 10
	def __init__(self,x,y,z, time):
		pushMatrix()
		fill(200,200,200)
		s_angle = radians(45)
		top, bottom = 0, 0.5
		translate(0,0,-5)
		rotateX(radians(90))
		scale(3.5,5,2)
		cone(sides=6)

		rotateX(radians(-90))
		translate(0,0,1)
		# Front light
		fill(0,255,255)
		o_cylinder(1.08, 0.1, 0, sides=6)
		
		# Fire
		fill(0,255,255)
		f_z2, f_z1 = 2.2, 1.2
		o_cylinder(0.6, f_z2, f_z1, sides=6)
		f_z3 = f_z2 + 0.3
		f_z4 = f_z3 + 0.3
		fill(0,255,255)
		o_cylinder(0.5, f_z4, f_z3, sides=6)
		
		f_z5 = f_z4 + 0.5
		f_z6 = f_z5 + 0.1
		fill(0,255,255)

		o_cylinder(0.35, f_z6, f_z5, sides=6)
		# fill(200,200,200)
		# o_cylinder(0.8, 2.7, 2.6, sides=6)

		fill(200,200,200)
		o_cylinder(1, 1.2, 0.1, sides=6)
		fill(0,255,255)
		o_cylinder(1.08, 0.94, 0.84, sides=6)

		popMatrix()

