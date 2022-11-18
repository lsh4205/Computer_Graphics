# This is the provided code for the ray tracing project.
#
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

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

# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global shapes, lightSrc, uvw, bgColors, surface, fov, eye
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
            ## need to add other color variables for 3B
            surface = Surface(dr, dg, db)
            pass

        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

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

            ray_direc = uU + vV - dW
            ray_origin = PVector(eye[0], eye[1], eye[2])
            ray = Ray(ray_origin, ray_direc.normalize())
            
            minT = 9999
            hit_object = None
            for shape in shapes:
                c = shape.canonical_sphere_interesect(ray)
                if c != None and c < minT and c > 0:
                    minT = c
                    hit_object = shape

            # Diffuse Shading
            pix_color_arry = [0,0,0]
            if hit_object == None or hit_object.surface == None:
                # No intersections -> Background Color
                pix_color_arry = [bgColors[0], bgColors[1], bgColors[2]]
            else:
                hit_obj = Hit(hit_object, minT, ray, ray.parametric_eq(minT))
                intersection_pt_with_ray = ray.parametric_eq(minT)
                N = PVector.sub(ray.parametric_eq(minT), hit_obj.sphere.center)
                N.normalize()
                for l in lightSrc:
                    L = PVector.sub(l.pos, ray.parametric_eq(minT))
                    L.normalize()
                    
                    pix_color_arry[0] += hit_obj.sphere.surface.dr * l.r * max(0, PVector.dot(N, L))
                    pix_color_arry[1] += hit_obj.sphere.surface.dg * l.g * max(0, PVector.dot(N, L))
                    pix_color_arry[2] += hit_obj.sphere.surface.db * l.b * max(0, PVector.dot(N, L))

            # Maybe set a debug flag to true for ONE pixel.
            # Have routines (like ray/sphere intersection)print extra information if this flag is set.
            debug_flag = False
            if i == 211 and j == 131:
                debug_flag = True
            if debug_flag:
                print "a, b, c coefficients of the quadratic: ", hit_obj.sphere.A, hit_obj.sphere.B, hit_obj.sphere.C
                print "uvw vectors:", uvw
                print "scalar u, v:", U, V
                print "ray origin: ", eye
                print "ray direction: ", ray_direc
                print "testing intersection with the sphere whose color is ", shape.surface.dr, shape.surface.dg, shape.surface.db
                print "t :" , minT
                print "intersection point: ", ray.parametric_eq(minT)
                print "normal : ", N
                print "found a hit: ", hit_obj
                print ''
            
            # create an eye ray for pixel (i,j) and cast it into the scene
            # you will calculate the correct pixel color here using ray tracing
            pix_color = color(pix_color_arry[0], pix_color_arry[1], pix_color_arry[2])
            set (i, j, pix_color)         # draw the pixel with the calculated color

# here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global shapes, lightSrc, uvw, bgColors, eye, fov, surface
    shapes = []
    lightSrc = []
    uvw = []
    bgColors = (0,0,0)
    eye = (0,0,0)
    fov = 0
    surface = None
    pass

# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
