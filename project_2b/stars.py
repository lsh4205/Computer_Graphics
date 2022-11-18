# Seonghyun Lee
# GT ID: 903452500

from star import *

class Stars:
	brightYellow = [255,255,153]
	brightOj = [229, 255, 204]
	brightR = [255, 255, 204]

	star_colors = [brightR, brightYellow, brightOj]

	def __init__(self, loc, time):
		j = 0
		for i in range(len(loc)):
			if j == 3:
				j = 0
			star = Star(0.07, time, 
				loc[i][0],loc[i][1],loc[i][2],
				self.star_colors[j], loc[i][3])
			j += 1
