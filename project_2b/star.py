# Seonghyun Lee
# GT ID: 903452500

from shapes import * 

class Star:
	
	log_factor = 10
	
	def __init__(self, w, time, x,y,z, colors, time_value):
		# 1. Increase z-size of box
		# 2. After certain time decrease the z-size of box
		pushMatrix()
		fill(colors[0], colors[1], colors[2])
		# start from -Y-axis to +X-axis, counter clock-wise
		translate(x, y, z)
		rotateZ(radians(self.calcuate_rotateZ_angle(x,y,z)))
		rotateX(radians(self.calcuate_rotateX_angle(x,y,z)))
		scale(0.6, 0.6,1)

		rel_time = time - time_value
		# second param = diminishing
		# third param = appearing
		o_cylinder(w,
			self.arctan_rate_scale(time-abs(time_value-2.0)) if time-(abs(time_value-2.00)) >= 0 else w,
			w if time <= time_value else w + self.arctan_rate_scale(rel_time),
			sides=4)

		# o_cylinder(w,
		#  w if time <= time_value else w + self.arctan_rate_scale(rel_time),
		# 	self.arctan_rate_scale(time-abs(time_value-2.0)) if time-(abs(time_value-2.00)) >= 0 else w,
		# 	sides=4)
		# self.arctan_rate_scale(time - float(abs(time_value - 2.00)) if time >= 0else w
		# w + self.arctan_rate_scale(time - float(abs(time_value - 2.00))) if time >= 0 else w,
		popMatrix()

	def arctan_rate_scale(self,time):
		time = time * 5
		# Want to start from (0, 0)
		# Y = arctan(X - b) + c
		# c = 0 - arctan(0 - b)
		b = 2
		c = -atan(-b)
		f_atan = atan(time - b) + c

		return f_atan * self.log_factor

	def spread_tail_in_cirlce(self, x, y, z):
		theta = 0
		# start from -Y-axis to +X-axis, counter clock-wise
		if x == 0 or y == 0:
			if x == 0:
				if y > 0: theta = 180
				else: theta = 0
			else:
				if x > 0: theta = 90
				else: theta = -90
		else:
			tan = float(abs(x))/float(abs(y))
			# returns in radians 
			theta = atan(tan)
			# Convert to degrees 
			theta = theta * 180 / PI
			if y > 0:
				theta = 180 - theta
			if x < 0:
				theta = -theta 

		return theta

	def calcuate_rotateZ_angle(self, x, y, z):
		theta = 0
		# start from -Y-axis to +X-axis, counter clock-wise
		if x == 0 or y == 0:
			if x == 0:
				if y > 0: theta = 180
				else: theta = 0
			else:
				if x > 0: theta = 90
				else: theta = -90
		else:
			tan = float(abs(x))/float(abs(y))
			# returns in radians 
			theta = atan(tan)
			# Convert to degrees 
			theta = theta * 180 / PI
			if y > 0:
				theta = 180 - theta
			if x < 0:
				theta = -theta 

		return theta

	def calcuate_rotateX_angle(self, x, y, z):
		theta = 0 
		# Opposite value
		# tan = opposite / adjacent

		opposite = sqrt(x ** 2 + y ** 2)
		tan = opposite / abs(float(z))
		theta = atan(tan) * 180 / PI

		return theta 



