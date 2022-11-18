# Seonghyun Lee
# GT ID: 903452500

from turbine import *
from wing import *
from shipbody import *

class SpaceShip:
	
	rotate_t = 1.5
	tur_t = 1.8

	def __init__(self, x, y, z, time, s_angle):
		# 1. Strech wing
		# 2. Camera switch to back
		# 2.1. Turbine support line rotate
		# 3. Wing rotate 
		tur_time = time - self.tur_t
		rel_time = tur_time - self.rotate_t
		# Ship body
		shipbody = ShipBody(0,0,0, time)

		# Left-Below 
		translate(x,y,0)
		turbine1 = Turbine(1,tur_time)
		if time >= rel_time:
		    self.rotateZ_motion_arctan(30, rel_time)
		wing1 = Wing(0, 0, 5, time, s_angle)
		if time >= rel_time:
		    self.rotateZ_motion_arctan(-30, rel_time)
		translate(-x,-y,0)

		# Right-Below 
		translate(-x,y,0)
		turbine2 = Turbine(1,tur_time)
		rotateZ(radians(-180))
		if time >= rel_time:
		    self.rotateZ_motion_arctan(-30, rel_time)
		#wings(tur_x, 0, 0, 5, time, -s_angle)
		wing2 = Wing(0, 0, 5, time, -s_angle)
		#wing.wings(0, 0, 5, time, -s_angle)
		if time >= rel_time:
		    self.rotateZ_motion_arctan(30, rel_time)
		rotateZ(radians(180))
		translate(x,-y,0)

		# Upper-Left
		translate(x,-y,0)
		turbine3 = Turbine(1,tur_time)
		if time >= rel_time:
		    self.rotateZ_motion_arctan(-30, rel_time)
		    # rotateZ(radians(-(rel_time * 3) if -(rel_time*3) >= (-30) else (-30)))
		wing3 = Wing(0, 0, 5, time, -(s_angle+radians(180)))
		#wing.wings(0, 0, 5, time, -(s_angle+radians(180)))
		if time >= rel_time:
		    self.rotateZ_motion_arctan(30, rel_time)
		    # rotateZ(radians((rel_time*3) if (rel_time*3) <= (30) else (30)))
		translate(-x,y,0)

		# Upper-Right
		translate(-x,-y,0)
		turbine4 = Turbine(1,tur_time)
		rotateZ(radians(180))
		if time >= rel_time:
		    self.rotateZ_motion_arctan(30, rel_time)
		    #rotateZ(radians((rel_time * 3) if (rel_time*3) <= (30) else (30)))
		wing4 = Wing(0, 0, 5, time, (s_angle+radians(180)))
		#wing.wings(0, 0, 5, time, (s_angle+radians(180)))
		if time >= rel_time:
		    self.rotateZ_motion_arctan(-30, rel_time)
		    #rotateZ(radians(-(rel_time * 3) if -(rel_time*3) >= -(30) else -(30)))
		rotateZ(radians(-180))
		translate(x,y,0)

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




