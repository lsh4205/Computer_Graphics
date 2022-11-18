from shapes import *
from structure import *

# cpos=center.pos, pos, s=scale, c1=color.component1, c2=color.component2, c3=color.component3
def back_cylinder(cpos, pos, s, r, c1,c2,c3, radius):
        fill (c1, c2, c3)
        pushMatrix()
        translate (pos[0] + cpos[0], pos[1] + cpos[1], pos[2] + cpos[2])
        rotateX (r)
        scale (s, s, s * 1.3)
        d_cylinder(radius)
        popMatrix()
        
        fill (c1, c2, c3)
        pushMatrix()
        translate (cpos[0]-pos[0], cpos[1]-pos[1], cpos[2]-pos[2])
        rotateX (r)
        scale (s, s, s * 1.3)
        d_cylinder(radius)
        popMatrix()

def eng_cylinder_with_arm(time):
        x, y, z = eng_cylinder1(1, time)
        radius = 1 

        pushMatrix()
        c_z = 0.3
        translate(x, y, (z) + c_z + 0.2)
        bearing(radius)
        popMatrix()

        pushMatrix()
        translate(x, y, z + 0.4 + 0.2)
        rotateX(abs(sin(radians(time * 20))))
        x_a, y_a, z_top, z_bottom = armStructure(radius, x, y, z, 0.2, time)
        translate(x_a, y_a, z_bottom)
        x_b, y_b = bearing(radius)

        popMatrix()
        

def wing_position(x,y,z, time, s_angle):
        # Left-Below 
        translate(x,y,0)
        tur_x, tur_y, tur_z = turbine(1,1)
        rotateZ(radians(30))
        shearX(s_angle)
        wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        shearX(-s_angle)
        wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        rotateZ(radians(-30))
        translate(-x,-y,0)
        
        # Right-Below 
        translate(-x,y,0)
        tur_x, tur_y, tur_z = turbine(1,1)
        rotateZ(radians(-210))
        shearX(-s_angle)
        wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        shearX(s_angle)
        wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        rotateZ(radians(210))
        translate(x,-y,0)
        
        # Upper-Left
        translate(x,-y,0)
        tur_x, tur_y, tur_z = turbine(1,1)
        rotate(radians(-30))
        shearX(-(s_angle+radians(180)))
        wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        shearX(s_angle+radians(180))
        wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        rotate(radians(30))
        translate(-x,y,0)
        
        # Upper-Right
        translate(-x,-y,0)
        tur_x, tur_y, tur_z = turbine(1,1)
        rotate(radians((30+180)))
        shearX((s_angle+radians(180)))
        wing_ed_x, wing_ed_y, wing_ed_z = wings(tur_x, 0, 0, 5, time)
        shearX(-(s_angle+radians(180)))
        wing_edge(wing_ed_x, wing_ed_y, wing_ed_z)
        rotate(radians(-(30+180)))
        translate(x,y,0)

        ship_body(0,0,0, time)

