# Seonghyun Lee
# GT ID: 903452500

from stars import *
from spaceShip import * 
        
def position(x,y,z, time, s_angle):
    spaceShip = SpaceShip(x,y,z,time,s_angle)
    rotate_t = spaceShip.rotate_t + spaceShip.tur_t + 1.5

    star_z = -17

    star_location = [[3,0, star_z, 2.8],
        [0,9, star_z, 2.2],
        [-3,-4, star_z, 2],
        [-3,-4.5, star_z, 2.3],
        [-3,0, star_z, 1.9],
        [-7.5,-0.2, star_z, 2.4],
        [-8,-2, star_z, 2.9],
        [-11,-1, star_z, 2.7],
        [8,0, star_z, 1.8 ],
        [8.5,-1, star_z, 2.5],

        [0,-9, star_z, 2.3 ],
        [-0.8,-9, star_z, 1.7],
        [9,-9, star_z, 2.1 ],
        [-9.4,-6, star_z, 2.5 ],
        [-9,-9, star_z, 1.9 ],
        [5,-5, star_z, 1.9 ],
        [5,1, star_z, 2.3 ],
        [4,4, star_z, 2.8 ],
        [5.5,6, star_z, 2.6 ],
        [-5,2, star_z, 2.7 ],
        [-2,4, star_z, 2.15 ],
        [-2.5,6, star_z, 2.2 ],
        [-7,3, star_z, 1.7 ],
        [-8,4, star_z, 2.7 ],
        [-2.5,6, star_z, 2.5 ],
    ]

    stars = Stars(star_location, time-rotate_t)

# def rotateZ_motion_arctan(r_angle, time):
#     time = time * 4
#     log_m = 10.0
#     # Want to start from (0, 0)
#     # Y = arctan(X - b) + c
#     # c = 0 - arctan(0 - b)
#     b = 2
#     c = -atan(-b)
#     f_atan = atan(time - b) + c
#     if r_angle < 0:
#         rotateZ(radians(-(f_atan*log_m) 
#             if -(f_atan*log_m) >= (r_angle) else (r_angle)))
#     else:
#         rotateZ(radians((f_atan*log_m) 
#             if (f_atan*log_m) <= (r_angle) else (r_angle)))




