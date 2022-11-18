# Seonghyun Lee
# GT ID: 903452500

from shapes import *

class Wing:
	max_r = 1.9 * 2
	def __init__(self, y,z, s, time, s_angle, x=max_r):
		pushMatrix()
		shearX(s_angle)
		x1 = 4.00
		x1_dis = 0.8
		translate(x/2.0 +0.2, 0, 0)

		self.wing_piece(x1, 1.5, 5.5, 4, x1_dis, time)
		x2 = 5.0
		x2_dis = 0.8

		self.wing_piece(x2, 1.2, 4.5, -0.5, x2_dis, time)
		x3 = 8.0
		x3_dis = 1.0

		self.wing_piece(x3, 0.9, 3, -0.75, x3_dis, time)
		shearX(-s_angle)
		# translate(0.8,0,0)
		# rotateX(radians(90))
		# rotateZ(radians(25))
		# shearY(radians(60))
		# #rotateY(radians(30))
		# sphere(1)
		# shearY(radians(-60))
		# rotateZ(radians(-25))
		# rotateX(radians(-90))
		self.wing_edge(x3_dis,0,-2.5)
		popMatrix()

	# Wing piece will have Wing-piece, light, and connecting frame
	def wing_piece(self,w, h, zH, zPos, dis, time):
		w, h, zH = float(w), float(h), float(zH)
		fill(200,200,200)
		slow = 1.4
		translate(slow*time + 1 if slow*time + 1 <= w/2.0 else w/2.0, 0, zPos)
		box(w, h, zH)
		# Light line
		fill(0,255,255)
		box(w+0.15, 0.15, zH+0.2)
		
		# Support frame
		fill(160,160,160)
		support_h = zH/1.5
		translate(w/2.0 + dis, 0, -(zH-support_h)/2.0)
		box(dis * 2.0, h/3.0, zH/1.5)
		# Move back to original z-position
		translate(0, 0, (zH-support_h)/2.0)

	# Create Wing-edge at the end of Wings
	def wing_edge(self, x,y,z):
		pushMatrix()
		translate(x,y,z)
		fill(200,200,200)

		# Add light on each cylinder
		def antenna_light(radius, thickness, z):
			translate(0,0,z)
			fill(0,255,255)
			torus(radius=radius, tube_radius=thickness, detail_x=7, detail_y=7)
			translate(0,0,-z)

		# Basic shape of Antenna 
		def antenna(radius):
			fill(200,200,200)
			radius = radius * 2
			top, bottom = 14.5, -3.5
			o_cylinder(radius, top, bottom, sides=8)
			top1, bottom1 = 5, -0.5
			o_cylinder(radius * 1.6, top1, bottom1, sides=8)
			top2, bottom2 = 15, 14.5
			o_cylinder(radius * 1.3, top2, bottom2, sides=8)

			# Anteena Light
			middle_thick, last_thick = 0.08, 0.06
			antenna_light(radius * 0.9, 0.08, bottom)
			translate(0,0, bottom+0.3)
			torus(radius=radius * 0.9, tube_radius=0.08, detail_x=7, detail_y=7)
			translate(0,0,-(bottom+0.3))
			antenna_light(radius * 1.6, middle_thick, bottom1)
			antenna_light(radius * 1.6, middle_thick, top1)
			antenna_light(radius * 1.3, last_thick, bottom2)
			antenna_light(radius * 1.3, last_thick, top2)

		antenna(0.2)
		popMatrix()







