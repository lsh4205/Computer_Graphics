# Seonghyun Lee
# GT ID: 903452500

from shapes import *

class Turbine:
	# Plane's Turbine
	def __init__(self, r, time):
		radius = r
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

		def support_line_z_rotate_ani(x,y,z, l_w, l_len, r_angle, r_z_angle, time):
			self.rotateZ_motion_arctan(r_z_angle, time)
			support_line(x, y, z, l_w, l_len, r_angle)
			self.rotateZ_motion_arctan(-r_z_angle, time)

		def support_line_z_rotate(x,y,z, l_w, l_len, r_angle, r_z_angle):
			rotateZ(radians(r_z_angle))
			support_line(x, y, z, l_w, l_len, r_angle)
			rotateZ(radians(-r_z_angle))

		pushMatrix()
		translate(0,0,0.1)
		fill(0,255,255)
		torus(radius=1.3, tube_radius=0.1, detail_x=10, detail_y=10)

		# First shallow cylinder
		translate(0,0,0.3)
		fill(200,200,200)
		torus(radius=1.5, tube_radius=0.3, detail_x=10, detail_y=10)
		
		c_start, c_end = 0.1, 1.2
		hollow_cylinder(1.76, c_end, c_start)

		support_line_z_rotate(0,0,-.9, 0.15, 1.7, 50, 0)
		support_line_z_rotate(0,0,-.9, 0.15, 1.7, 50, 180)

		popMatrix()

		# Middle 
		pushMatrix()
		translate(0,0,c_end)
		c_start, c_end = 0, 7
		# CYAN
		fill(0,255,255)
		torus(radius=1.85, tube_radius=0.1, detail_x=10, detail_y=10)
		
		# Middle shallow cylinder
		fill(100, 100, 100)
		hollow_cylinder(1.9, c_end, c_start)

		# Inside of Engine 
		fill(200, 200, 200)
		shear_angle = radians(55)
		rotateX(radians(90))
		rotateZ(radians(62))

		shearX(shear_angle)
		sphereDetail(20);
		sphere(1.1)
		popMatrix()

		pushMatrix()
		translate(0,0, c_end)
		# Support line for the back of turbine
		# support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, 20, time)
		# support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, -20, time)
		# support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, 20 + 180, time)
		# support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, -(20 + 180), time)

		support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, 20, time)
		support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, -20, time)

		rotateZ(radians(-180))
		support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, 20, time)
		rotateZ(radians(180))

		rotateZ(radians(180))
		support_line_z_rotate_ani(1, 0, 2, 0.15, 2.5, 50, -20, time)
		rotateZ(radians(-180))

		fill(200, 200, 200)
		shear_angle = radians(55)
		rotateX(radians(90))
		rotateZ(radians(62))
		shearX(shear_angle)
		sphereDetail(20);
		sphere(1.7)
		popMatrix()

		pushMatrix()
		translate(0,0, c_end)
		translate(0,0, 0.2)
		#fill(127,255,212)
		fill(0,255,255)
		torus(radius=2.03, tube_radius=0.1, detail_x=10, detail_y=10)

		translate(0,0, 0.2)
		translate(0,0, 0.74)
		fill(0,255,255)
		torus(radius=1.85, tube_radius=0.12, detail_x=10, detail_y=10)
		popMatrix()

	def rotateZ_motion_arctan(self, r_angle, time):
	    time = time * 4
	    log_m = 10.0
	    # Want to start from (0, 0)
	    # Y = arctan(X - b) + c
	    # c = 0 - arctan(0 - b)
	    b = 2
	    c = -atan(-b)
	    f_atan = atan(time - b) + c
	    if r_angle < 0:
	        rotateZ(radians(-(f_atan*log_m) 
	            if -(f_atan*log_m) >= (r_angle) else (r_angle)))
	    else:
	        rotateZ(radians((f_atan*log_m) 
	            if (f_atan*log_m) <= (r_angle) else (r_angle)))













