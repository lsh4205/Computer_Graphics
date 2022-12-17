from __future__ import division
import traceback
from classes import *

debug_flag = False   # print debug information when this is True

# Global objects
shapes = []
lightSrc = []
uvw = []
bgColors = (0,0,0)
eye = (0,0,0)
fov = 0
surface = None
t_vertices = []

def setup():
    size(320, 320) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    frameRate(30)

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# read and interpret a scene description .cli file based on which key has been pressed
def handleKeyPressed():
    if key == '1':
        interpreter("01_one_sphere.cli")
    elif key == '2':
        interpreter("02_three_spheres.cli")
    elif key == '3':
        interpreter("03_shiny_sphere.cli")
    elif key == '4':
        interpreter("04_many_spheres.cli")
    elif key == '5':
        interpreter("05_one_triangle.cli")
    elif key == '6':
        interpreter("06_icosahedron_and_sphere.cli")
    elif key == '7':
        interpreter("07_colorful_lights.cli")
    elif key == '8':
        interpreter("08_reflective_sphere.cli")
    elif key == '9':
        interpreter("09_mirror_spheres.cli")
    elif key == '0':
        interpreter("10_reflections_in_reflections.cli")
    elif key == '-':
        interpreter("11_star.cli")

# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global shapes, lightSrc, uvw, bgColors, surface, fov, eye, t_vertices
    reset_scene()  # you should initialize any data structures that you will use here
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse the lines in the file in turn
    for line in lines:
        words = line.split()  # split up the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])

            # call your sphere making routine here
            # for example: create_sphere(x,y,z,radius)

            center = PVector(x,y,z)
            shapes.append(Sphere(radius, center, surface))
            
        elif words[0] == 'fov':
            fov = float(words[1])
            pass

        elif words[0] == 'eye':
            # Set the position of the eye to (ex, ey, ez).
            eX = float(words[1])
            eY = float(words[2])
            eZ = float(words[3])
            eye = (eX, eY, eZ)
            pass

        elif words[0] == 'uvw':
            # Specifies the (u, v, w) coordinate frame 
            # that helps to define the eye rays.
            ux = float(words[1])
            uy = float(words[2])
            uz = float(words[3])

            vx = float(words[4])
            vy = float(words[5])
            vz = float(words[6])

            wx = float(words[7])
            wy = float(words[8])
            wz = float(words[9])
            
            uvw = [PVector(ux,uy,uz), PVector(vx,vy,vz), PVector(wx,wy,wz)]
            pass

        elif words[0] == 'background':
            bgR = float(words[1])
            bgG = float(words[2])
            bgB = float(words[3])
            bgColors = (bgR, bgG, bgB)
            pass
            
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])

            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            l_pos = PVector(x,y,z)

            light = Light(l_pos, r, g, b)
            lightSrc.append(light)
            pass

        elif words[0] == 'surface':
            dr = float(words[1])
            dg = float(words[2])
            db = float(words[3])

            ar = float(words[4])
            ag = float(words[5])
            ab = float(words[6])

            sr = float(words[7])
            sg = float(words[8])
            sb = float(words[9])

            spec_power = float(words[10])
            k_refl = float(words[11])

            surface = Surface(dr, dg, db, ar, ag, ab, sr, sg, sb, spec_power, k_refl)
            pass

        elif words[0] == 'begin':
            t_vertices = []
            pass

        elif words[0] == 'vertex':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            t_vertices.append(PVector(x, y, z))
            # print(t_vertices)
            pass

        elif words[0] == 'end':
            triangle = Triangle(t_vertices[0], t_vertices[1], t_vertices[2], surface)
            # print(triangle)
            shapes.append(triangle)
            pass

        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

def rayIntersectScene(ray):
    minT = 999999999
    hit_object = None
    for shape in shapes:
        c = shape.intersect(ray)
        # t < 0 , no Hit / Intersection
        if c != None and c.t < minT:
            minT = c.t
            hit_object = c
    return hit_object 


def shade(hit_obj, ray, max_depth):
    sum_colors = PVector(0,0,0)
    # print(hit_obj)
    if hit_obj == None or hit_obj.surface == None:
        # No intersections -> Background Color
        return PVector(bgColors[0], bgColors[1], bgColors[2])
    
    else:
        # print(hit_obj)
        tiny_offset = PVector.mult(hit_obj.normal_v, 0.0001)

        if max_depth > 0 and hit_obj.surface.k_refl > 0:
            # Reflection
            # Reflection - Create a Reflection ray
            reflect_ray_origin = PVector.add(hit_obj.intersect, tiny_offset)
            N_neg_D = (PVector.dot(hit_obj.normal_v, PVector.mult(ray.direc, -1))) * 2
            reflect_ray_direc = (PVector.add(ray.direc, PVector.mult(hit_obj.normal_v, N_neg_D))).normalize()
            
            reflect_ray = Ray(reflect_ray_origin, reflect_ray_direc)

            reflect_hit = rayIntersectScene(reflect_ray)
   
            reflect_color = shade(reflect_hit, reflect_ray, max_depth - 1)
            reflect_c = PVector.mult(reflect_color, hit_obj.surface.k_refl)
            sum_colors = PVector.add(sum_colors, reflect_c)

        for l in lightSrc:
            # Light Color
            lColor = PVector(l.r, l.g, l.b)

            # Shadows - Create a shadow ray
            s_ray_origin = PVector.add(hit_obj.intersect, tiny_offset)
            s_ray_direc = (PVector.sub(l.pos, hit_obj.intersect)).normalize()
            shadow_ray = Ray(s_ray_origin, s_ray_direc)

            shadow_hit = rayIntersectScene(shadow_ray)

            if shadow_hit and shadow_hit.t < PVector.dist(l.pos, hit_obj.intersect):
                continue

            else: 
                # Specular Shading : Per Light
                # Specular - 1. H-Vector
                N = hit_obj.normal_v
                L = (PVector.sub(l.pos, hit_obj.intersect)).normalize()
                D = (ray.direc).normalize()
                neg_D = PVector.mult(D, -1)
                H = (PVector.add(L, neg_D)).normalize()

                # Specular - 2. Specular Coefficients 
                # max(0, (H * N))^P
                HN = PVector.dot(H, hit_obj.normal_v)
                max_specular = (max(0, HN)) ** hit_obj.surface.spec_power

                # Specular - 3. Specular Contribution
                hit_obj_specular = PVector(hit_obj.surface.sr, hit_obj.surface.sg, hit_obj.surface.sb)
                specular_color = PVector.mult(PVector.pairwise_mult(lColor, hit_obj_specular), max_specular)

                # Diffuse Color 
                hit_obj_diffuse = PVector(hit_obj.surface.dr, hit_obj.surface.dg, hit_obj.surface.db)
                NL = PVector.dot(N, L)
                max_diffuse = max(0, NL)
                diffuse_color = PVector.mult(PVector.pairwise_mult(hit_obj_diffuse, lColor), max_diffuse)

                sum_colors = PVector.add(sum_colors, PVector.add(specular_color, diffuse_color))
       
        # Ambient Contribution : adding it ONCE
        ambient_color = PVector(hit_obj.surface.ar, hit_obj.surface.ag, hit_obj.surface.ab)
        
        sum_colors = PVector.add(ambient_color, sum_colors)
        return sum_colors

# render the ray tracing scene
def render_scene():
    global debug_flag
    d = 1/(tan(radians(fov)/ 2.0))
    for j in range(height):
        for i in range(width):
            # Change Coordinate
            U = 2.0 * i / width - 1
            V = -1 * (2.0 * j / height - 1)
            uU = PVector.mult(uvw[0], U)
            vV = PVector.mult(uvw[1], V)
            dW = PVector.mult(uvw[2], d)

            ray_direc = PVector.sub(PVector.add(uU, vV), dW)
            ray_origin = PVector(eye[0], eye[1], eye[2])
            ray = Ray(ray_origin, ray_direc.normalize())
            
            hit_obj = rayIntersectScene(ray)
            pix_color_vec = shade(hit_obj, ray, 10)
            if hit_obj == None:
                pix_color_vec = PVector(bgColors[0], bgColors[1], bgColors[2])
            # Maybe set a debug flag to true for ONE pixel.
            # Have routines (like ray/sphere intersection)print extra information if this flag is set.
            debug_flag = False
            if i == 165 and j == 195:
                debug_flag = True
            # create an eye ray for pixel (i,j) and cast it into the scene
            # you will calculate the correct pixel color here using ray tracing

            pix_color = color(pix_color_vec.x, pix_color_vec.y, pix_color_vec.z)
            set (i, j, pix_color)         # draw the pixel with the calculated color



# here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global shapes, lightSrc, uvw, bgColors, eye, fov, surface, t_vertices
    shapes = []
    lightSrc = []
    uvw = []
    bgColors = (0,0,0)
    eye = (0,0,0)
    fov = 0
    surface = None
    t_vertices = []
    pass

# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
