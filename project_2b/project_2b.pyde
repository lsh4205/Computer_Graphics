# Object Modeling Example Code
# Seonghyun Lee
# GT ID: 903452500

from __future__ import division
import traceback
from shapes import *
from positions import *
from structure import *  

time = 0   # time is used to move objects from one frame to another
angle = 0


def setup():
    size (950, 950, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time, angle
        time += 0.01

        #camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        
        camera (-10, -20, -100, 0, 0, 0, 0,  1, 0)
        # position of the virtual camera
    
        if time >= 2:
            camera (-5, -10, 80, 0, 0, 0, 0,  1, 0)
        if time >= 1.8 + 1.5 + 3.5:
             camera (40, -40, -90, 0, 0, 0, 0,  1, 0)
        # clear screen and set background to light blue
        background(50,50,50)
        # Set up the lights
        ambientLight(70, 70, 70);
        lightSpecular(255, 255, 255)
        directionalLight (60, 50, 50, 2, 7, -10)
        #directionalLight (80,80, 80, 1, -2, 1)
        directionalLight (40,80, 80, 3, -1, 10)
        # back 
        directionalLight (30, 20, 20, 1, 1, -1)
        #directionalLight (70,45, 45, 1.2, 0.3, 2)
        # directionalLight (80,80, 80, 0, 0, -12)
        # Set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)

        # # a blue cylinder
        # fill (200, 200, 200)
        # pushMatrix()
        # translate (0, -35, 0)
        # if mousePressed:
        #     angle += 0.5
        #     rotateY(radians(angle))
        # rotateX(radians(5))
        # rotateY(radians(20))
        # scale (5, 5, 5)
        # #eng_cylinder_with_arm(time)
        # #turbine(1,1)
        # popMatrix()
        
        fill (200, 200, 200)
        pushMatrix()
        translate (0,0,0)


        s_val = 2
        #rotateX(radians(-15))

        # rotateX(radians(20))
        # rotateY(radians(18))
        scale (s_val, s_val, s_val)
        #directionalLight (80,80, 80, 0, 0, -12)
        s_angle = radians(30)
        position(5,2.5,0, time, s_angle)
        directionalLight (80,80, 80, 3, 1, -1)
        # translate(5,0,0)
        # tur_x, tur_y, tur_z = turbine(1,1)
        # rotateZ(radians(30))
        # shearX(s_angle)
        # wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        # shearX(-s_angle)
        # wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        # rotateZ(radians(-30))
        # translate(-5,0,0)
        
        # translate(-5,0,0)
        # tur_x, tur_y, tur_z = turbine(1,1)
        # rotateZ(radians(-210))
        # shearX(-s_angle)
        # wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        # shearX(s_angle)
        # wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        # rotateZ(radians(210))
        # translate(5,0,0)
        
        # translate(5,-5,0)
        # tur_x, tur_y, tur_z = turbine(1,1)
        # rotate(radians(-30))
        # shearX(-(s_angle+radians(180)))
        # wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        # shearX(s_angle+radians(180))
        # wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        # rotate(radians(30))
        # translate(-5,5,0)
        
        # translate(-5,-5,0)
        # tur_x, tur_y, tur_z = turbine(1,1)
        # rotate(radians((30+180)))
        # shearX((s_angle+radians(180)))
        # wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        # wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        # shearX(-(s_angle+radians(180)))
        # rotate(radians(-(30+180)))
        # translate(5,5,0)
   
        popMatrix()
        camera (100, 0, 50, 0, 0, 0, 0,  1, 0)

        # fill(0,100,100)
        # pushMatrix()
        # translate(30, 0, 0)
        # rotateX(60 * time * 0.05)
        # scale(10, 10, 10)
        # torus()
        # popMatrix()

    except Exception:
        traceback.print_exc()
