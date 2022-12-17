# Provided code for Subdivison and Geodesic Spheres

from __future__ import division
import traceback

# parameters used for object rotation by mouse
mouseX_old = 0
mouseY_old = 0
rot_mat = PMatrix3D()

currentCorner = 0
currentCornerVisible = False
showRandomColors = False
V = []
G = []
O = {}

# initalize things
def setup():
    size (800, 800, OPENGL)
    frameRate(30)
    noStroke()

# draw the current mesh (you will modify parts of this routine)
def draw():
    global currnetCorner
    background (100, 100, 180)    # clear the screen to black

    perspective (PI*0.2, 1.0, 0.01, 1000.0)
    camera (0, 0, 6, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    
    # create an ambient light source
    ambientLight (102, 102, 102)

    # create two directional light sources
    lightSpecular (202, 202, 202)
    directionalLight (100, 100, 100, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    stroke (0)                    # draw polygons with black edges
    fill (200, 200, 200)          # set the polygon color to white
    ambient (200, 200, 200)
    specular (0, 0, 0)            # turn off specular highlights
    shininess (1.0)
    
    applyMatrix (rot_mat)   # rotate the object using the global rotation matrix

    # THIS IS WHERE YOU SHOULD DRAW YOUR MESH
    randomSeed(10000)
    for c in range(0, len(V), 3):
        beginShape()
        if showRandomColors:
            fill(random(0, 255), random(0, 255), random(0, 255))
        else:
            fill(255,255,255)
        vertex (G[V[c]].x, G[V[c]].y, G[V[c]].z)
        vertex (G[V[c+1]].x, G[V[c+1]].y, G[V[c+1]].z)
        vertex (G[V[c+2]].x, G[V[c+2]].y, G[V[c+2]].z)
        endShape(CLOSE)
        
    if currentCornerVisible:
        pushMatrix()
        currVertex = G[V[currentCorner]]
        prevVertex = G[V[previousCorner(currentCorner)]]
        nextVertex = G[V[nextCorner(currentCorner)]]
        curr = PVector.mult(currVertex, 0.8) + PVector.mult(prevVertex, 0.1) + PVector.mult(nextVertex, 0.1)
        translate(curr.x, curr.y, curr.z)
        noStroke()
        sphere(0.05)
        popMatrix()
        
    popMatrix()

# read in a mesh file (this needs to be modified)
def read_mesh(filename):
    global V, G, O
    V = []
    G = []
    O = {}
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex: ", x, y, z
        
        G.append(PVector(x,y,z))

    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if (nverts != 3):
            print "error: this face is not a triangle"
            exit()

        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "triangle: ", index1, index2, index3
        
        V.extend([index1, index2, index3])

    O = computeOTable(G, V)
    print_mesh()
        
def print_mesh():
    print "Vertex table (maps corner num to vertex num):"
    print "corner num\tvertex num:"
    for c, v in enumerate(V):
        print c, "\t\t", v
    print ""

    print "Opposite table (maps corner num to opposite corner num):"
    print "corner num\topposite corner num"
    for c, o in O.iteritems():
        print c, "\t\t", o
    print ""

    print "Geometry table (maps vertex num to position): "
    print "vertex num\tposition:"
    for v, g in enumerate(G):
        print v, "\t\t", g
    print ""

    print ""
    print ""
    
# Helper Method
def nextCorner(cornerNum):
    triangleNum = cornerNum // 3
    return 3 * triangleNum + ((cornerNum + 1) % 3)

def previousCorner(cornerNum):
    triangleNum = cornerNum // 3
    return 3 * triangleNum + ((cornerNum - 1) % 3)

def oppositeCorner(cornerNum):
    return O[cornerNum]
    
def swingCorner(cornerNum):
    return nextCorner(oppositeCorner(nextCorner(cornerNum)))

def computeOTable(G, V):
    newO = {}
    triplets = []
    for i in range(len(V)):

        triplets.append([min(V[nextCorner(i)], V[previousCorner(i)]), max(V[nextCorner(i)], V[previousCorner(i)]), i])    
    
    sortedTriplets = sorted(triplets)

    for i in range(0, len(sortedTriplets), 2):
        c_a = sortedTriplets[i][2]
        c_b = sortedTriplets[i+1][2]
        newO[c_a] = c_b
        newO[c_b] = c_a
    return newO
        
def inflate():
    global G
    for i in range(len(G)):
        G[i].normalize()
    
def subdivision():
    global V, G, O
    numEdges = len(V)//2
    # new G-Table should have copy of old G-Table
    newGTable, newVTable = G[:], []
    midpoints = {}
    for a,b in O.iteritems():
        end1 = G[V[previousCorner(a)]]
        end2 = G[V[nextCorner(a)]]

        midpoint = PVector.mult(PVector.add(end1, end2), 0.5)
        midpointIndex = len(newGTable)
        midpoints[a] = midpointIndex
        midpoints[b] = midpointIndex
        newGTable.append(midpoint)
        
    for x in range(0, len(V), 3):
        y = x + 1
        z = x + 2
        # Extend allows append with multiple variables
        # But need to use it with 'tuple'
        newVTable.extend([V[x], midpoints[z], midpoints[y]])
        newVTable.extend([midpoints[z], V[y], midpoints[x]])
        newVTable.extend([midpoints[y], midpoints[x], V[z]])
        newVTable.extend([midpoints[x], midpoints[z], midpoints[y]])
        
    V = newVTable
    G = newGTable
    O = computeOTable(G, V)
    
    print_mesh()
                                        
# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# process key presses (call your own routines!)
def handleKeyPressed():
    global currentCorner
    if key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
        
    elif key == 'n': # next
        currentCorner = nextCorner(currentCorner)
        pass
    elif key == 'p': # previous
        currentCorner = previousCorner(currentCorner)
        pass
    elif key == 'o': # opposite
        currentCorner = oppositeCorner(currentCorner)
        pass
    elif key == 's': # swing
        currentCorner = swingCorner(currentCorner)
        pass
    elif key == 'd': # subdivide mesh
        subdivision()
        pass
    elif key == 'i': # inflate mesh
        inflate()
        pass
    elif key == 'r': # toggle random colors
        global showRandomColors
        if showRandomColors:
            showRandomColors = False
        else: showRandomColors = True
        pass
    elif key == 'c': # toggle showing current corner
        global currentCornerVisible
        currentCornerVisible = True
        pass
    elif key == 'q': # quit the program
        exit()

# remember where the user first clicked
def mousePressed():
    global mouseX_old, mouseY_old
    mouseX_old = mouseX
    mouseY_old = mouseY

# change the object rotation matrix while the mouse is being dragged
def mouseDragged():
    global rot_mat
    global mouseX_old, mouseY_old
    
    if (not mousePressed):
        return
    
    dx = mouseX - mouseX_old
    dy = mouseY - mouseY_old
    dy *= -1

    len = sqrt (dx*dx + dy*dy)
    if (len == 0):
        len = 1
    
    dx /= len
    dy /= len
    rmat = PMatrix3D()
    rmat.rotate (len * 0.005, dy, dx, 0)
    rot_mat.preApply (rmat)

    mouseX_old = mouseX
    mouseY_old = mouseY


    
