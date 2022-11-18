from shapes import *

# Draw Engine Cylinder
def eng_cylinder1(radius, time, sides=50):
	top, bottom = 1, -1.5
	o_cylinder(radius, top, bottom)
	o_cylinder(radius * 0.9, top + 0.15, top)
	o_cylinder(radius * 0.75, top + 0.5, top + 0.15)

	translate(0,0, 0.1 + sin(time * 2.4)*0.5)
	o_cylinder(radius * 0.6, top + 2.5, 0.25)

	#translate(0,0, -0.5 + sin(time * 2)*0.4)
	o_cylinder(radius * 0.75, top + 2.85, top + 2.5)
	#o_cylinder(radius * 0.9, top + 3, top + 2.85)
	# o_cylinder(radius * 0.35, top + 4, top + 2.5)
	o_cylinder(radius * 0.9, top + 4.5, top + 2.85)
	o_cylinder(radius * 0.8, top + 4.6, top + 4.5)
	
	last_z = top + 4.6
	#bearing(radius, 0, 0, last_z, 0.2)
	return 0, 0, last_z

# Draw Two Bearing
# Need to translate the last object location
# return Left-edge, Right-edge 
def bearing(radius):
	pushMatrix()
	# New bearing z-value
	c_z = 0.3
	rotateY(radians(90))
	rotateZ(radians(90))
	
	nut_h = 0.45
	# (-0.1) (-c_z) (+0.05) --- 0 --- (-0.05) (+c_z) (+0.1)
	#fill(110, 110, 110)
	#nut(radius * 0.4, (c_z*1.7) + nut_h, (c_z*1.7) + 0.15)
	o_cylinder(radius * 0.6, (c_z*1.7) + 0.15, (c_z*1.7) + 0.1)
	o_cylinder(radius * 0.7, (c_z*1.7) + 0.1, c_z + 0.05)
	o_cylinder(radius * 0.6, c_z + 0.05, c_z)

	# Center 
	o_cylinder(radius * 0.5, c_z*2.9, -c_z*2.9)

	o_cylinder(radius * 0.6, -c_z, -c_z - 0.05)
	o_cylinder(radius * 0.7, -c_z - 0.05, -(c_z*1.7) - 0.1)
	o_cylinder(radius * 0.6, -(c_z*1.7) - 0.1, -(c_z*1.7) - 0.15)
	
	fill(110, 110, 110)
	nut(radius * 0.4, (c_z*1.7) + nut_h, (c_z*1.7) + 0.15)
	nut(radius * 0.4, -(c_z*1.7) - 0.15,  -(c_z*1.7) - nut_h)
	
	popMatrix()
	return  -(c_z*1.7) - nut_h,(c_z*1.7) + nut_h

# Draw armStructure
# return x, y, z_top, z_bottom
def armStructure(radius, x, y, z, zPlus, time):
	pushMatrix()
	fill (200, 200, 200)
	dis = 0.4
	#translate(x, y, z + dis + zPlus)
	#rotateX(radians(-60))
	# rotateX(abs(sin(radians(30)*time)))
	c_z = 0.6
	m_size = 7
	o_cylinder(radius * 0.3, c_z*1.15, 0)
	o_cylinder(radius * 0.5, c_z*1.3, c_z*1.15)
	o_cylinder(radius * 0.55, c_z*m_size, c_z*1.3)
	o_cylinder(radius * 0.5, c_z*(m_size+0.15), c_z*m_size)
	o_cylinder(radius * 0.3, c_z*(m_size+1.15), c_z*(m_size+0.15))

	translate(0, radius * 1, c_z * 5)
	#o_cylinder(radius * 0.8, c_z*5, c_z*2)
	popMatrix()

	return x, y, c_z*1.15, c_z*(m_size+1.15)

# Plane's Turbine
def turbine(radius, l):
	# Support line (Cyan)
	def support_line(x,y,z, l_w, l_len, r_angle):
		r_angle = radians(r_angle)
		x, y, z, l_w = float(x), float(y), float(z), float(l_w)
		
		fill(0,255,255)
		rotateY(-r_angle)
		translate(x, y, z)
		box(l_len, l_w, l_w)
		translate(-x, -y, -z)
		rotateY(r_angle)

	pushMatrix()
	translate(0,0,0.1)
	#fill(127,255,212)
	fill(0,255,255)
	torus(radius=1.3, tube_radius=0.1, detail_x=20, detail_y=20)
	# c_start, c_end = 0.1, 1.5
	# hollow_cylinder(1.3, c_end, c_start)
	
	# First shallow cylinder
	translate(0,0,0.3)
	fill(200,200,200)
	torus(radius=1.5, tube_radius=0.3, detail_x=20, detail_y=20)
	
	c_start, c_end = 0.1, 1.2
	hollow_cylinder(1.76, c_end, c_start)
	# #Support line (Cyan)
	# rotateZ(radians(30))
	# support_line(0, 0, -.9, 0.15, 1.7, 50)
	# rotateZ(radians(-30))

	# rotateZ(radians(-30))
	# support_line(0, 0, -.9, 0.15, 1.7, 50)
	# rotateZ(radians(30))

	# rotateZ(radians(-(30+180)))
	# support_line(0, 0, -.9, 0.15, 1.7, 50)
	# rotateZ(radians((30+180)))

	# rotateZ(radians((30+180)))
	# support_line(0, 0, -.9, 0.15, 1.7, 50)
	# rotateZ(radians(-(30+180)))

	rotateZ(radians(0))
	support_line(0, 0, -.9, 0.15, 1.7, 50)
	rotateZ(radians(0))

	rotateZ(radians(180))
	support_line(0, 0, -.9, 0.15, 1.7, 50)
	rotateZ(radians(-180))
	popMatrix()

	# Middle 
	pushMatrix()
	translate(0,0,c_end)
	c_start, c_end = 0, 7
	# CYAN
	fill(0,255,255)
	torus(radius=1.85, tube_radius=0.1, detail_x=20, detail_y=20)
	
	# Middle shallow cylinder
	fill(200, 200, 200)
	hollow_cylinder(1.9, c_end, c_start)

	# Inside of Engine 
	fill(200, 200, 200)
	shear_angle = radians(55)
	rotateX(radians(90))
	rotateZ(radians(62))
	shearX(shear_angle)
	sphere(1.1)
	popMatrix()

	pushMatrix()
	translate(0,0, c_end)
	fill(200, 200, 200)
	shear_angle = radians(55)
	rotateX(radians(90))
	rotateZ(radians(62))
	shearX(shear_angle)
	sphere(1.7)
	popMatrix()

	pushMatrix()
	translate(0,0, c_end)
	translate(0,0, 0.2)
	#fill(127,255,212)
	fill(0,255,255)
	torus(radius=2.03, tube_radius=0.1, detail_x=20, detail_y=20)

	translate(0,0, 0.2)
	translate(0,0, 0.74)
	fill(0,255,255)
	torus(radius=1.85, tube_radius=0.12, detail_x=20, detail_y=20)
	popMatrix()

	max_r = 1.9 * 2
	return max_r, 0, 0

# TODO: Need to animate 
# 		by increasing y-scale of wing proportional to 'time'
# Wing will have light and connecting piece 
def wings(x,y,z, s, time):
	last_x = 0.00

	# Wing piece will have Wing-piece, light, and connecting frame
	def wing_piece(w, h, zH, zPos, dis, time):
		w, h, zH = float(w), float(h), float(zH)
		fill(200,200,200)
		translate(w/2.0, 0, zPos)
		box(w, h, zH)

		# Light line
		fill(0,255,255)
		box(w+0.15, 0.15, zH+0.2)
		
		# Support frame
		fill(180,180,180)
		support_h = zH/1.5
		translate(w/2.0 + dis, 0, -(zH-support_h)/2.0)
		box(dis * 2.0, h/3.0, zH/1.5)
		# Move back to original z-position
		translate(0, 0, (zH-support_h)/2.0)

	pushMatrix()
	x1 = 4.00
	x1_dis = 0.8
	translate(x/2.0 +0.2, 0, 0)
	wing_piece(x1, 1.3, 5.5, 4, x1_dis, time)
	x2 = 5.0
	x2_dis = 0.8
	wing_piece(x2, 1, 4.5, -0.5, x2_dis, time)
	x3 = 8.0
	x3_dis = 1.0
	wing_piece(x3, 0.7, 3, -0.75, x3_dis, time)

	# translate(0.8,0,0)
	# rotateX(radians(90))
	# rotateZ(radians(25))
	# shearY(radians(60))
	# #rotateY(radians(30))
	# sphere(1)
	# shearY(radians(-60))
	# rotateZ(radians(-25))
	# rotateX(radians(-90))
	popMatrix()
	last_x = x/2.0 + 0.2 + x1 + x2 + x3 + x1_dis + x2_dis + x3_dis * 2
	return last_x, 0, 0

# Create Wing-edge at the end of Wings
def wing_edge(x,y,z):
	pushMatrix()
	translate(x,y,z)
	fill(200,200,200)

	# Add light on each cylinder
	def antenna_light(radius, thickness, z):
		translate(0,0,z)
		fill(0,255,255)
		torus(radius=radius, tube_radius=thickness, detail_x=20, detail_y=20)
		translate(0,0,-z)

	# Basic shape of Antenna 
	def antenna(radius):
		top, bottom = 14.5, -3.5
		o_cylinder(radius, top, bottom)
		top1, bottom1 = 5, -0.5
		o_cylinder(radius * 1.6, top1, bottom1)
		top2, bottom2 = 15, 14.5
		o_cylinder(radius * 1.3, top2, bottom2)

		# Anteena Light
		middle_thick, last_thick = 0.08, 0.06
		antenna_light(radius * 0.9, 0.08, bottom)
		translate(0,0, bottom+0.3)
		torus(radius=radius * 0.9, tube_radius=0.08, detail_x=20, detail_y=20)
		translate(0,0,-(bottom+0.3))
		antenna_light(radius * 1.6, middle_thick, bottom1)
		antenna_light(radius * 1.6, middle_thick, top1)
		antenna_light(radius * 1.3, last_thick, bottom2)
		antenna_light(radius * 1.3, last_thick, top2)

	antenna(0.2)

	popMatrix()

def ship_body(x,y,z, time):
	fill(200,200,200)
	def angled_triangle(x,y,z):
		fill(200,200,200)
		beginShape()
		vertex(x,y,z)
		vertex(-x,y,z)
		vertex(0,-y,z)
		endShape(CLOSE)

		beginShape()
		vertex(x,y,-z)
		vertex(-x,y,-z)
		vertex(0,-y,-z)
		endShape(CLOSE)
		
		fill(0,255,255)
		beginShape()
		vertex(x,y,z)
		vertex(x,y,-z)
		vertex(-x,y,-z)
		vertex(-x,y,z)
		endShape(CLOSE)

		beginShape()
		vertex(-x,y,z)
		vertex(-x,y,-z)
		vertex(0,-y,-z)
		vertex(0,-y,z)
		endShape(CLOSE)

		beginShape()
		vertex(0,-y,z)
		vertex(0,-y,-z)
		vertex(x,y,-z)
		vertex(x,y,z)
		endShape(CLOSE)

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















