# Cylinder with radius = 1, z range in [-1,1]
# Seonghyun Lee
# GT ID: 903452500

def cylinder(radius, sides = 20):
    # first endcap
    v = []
    seg = []
    for i in range(sides):
        v1 = []
        theta = i * 2 * PI / sides
        x = cos(theta) * radius 
        y = sin(theta) * radius
        seg.append([x, y, -1])
    v.append(seg)
    
    #second endcap
    seg = []
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta) * radius
        y = sin(theta) * radius
        seg.append([x, y, 1])
    v.append(seg)
    
    # round main body
    x1 = 1 * radius
    y1 = 0
    seg = []
    for i in range(sides):
        theta = i * 2 * PI / sides
        x2 = cos(theta) * radius
        y2 = sin(theta) * radius
        
        #normal (x1, y1, 0)s
        seg.append([x1, y1, 1])
        seg.append([x1, y1, -1])
        #normal (x2, y2, 0)

        seg.append([x2, y2, -1])
        seg.append([x2, y2, 1])
        x1 = x2
        y1 = y2
    v.append(seg)
    return v

# Draw a cylinder with top and bottom param (z-value)
def o_cylinder(radius, top, bottom, sides = 15):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta) * radius
        y = sin(theta) * radius
        vertex (x, y, bottom)
    endShape(CLOSE)

    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta) * radius
        y = sin(theta) * radius
        vertex (x, y, top)
    endShape(CLOSE)

    # round main body
    x1 = 1 * radius
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta) * radius
        y2 = sin(theta) * radius
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, top)
        vertex (x1, y1, bottom)
        

        normal (x2, y2, 0)
        vertex (x2, y2, bottom)
        vertex (x2, y2, top)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

def nut(radius, top, bottom, sides = 8):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta) * radius
        y = sin(theta) * radius
        vertex (x, y, bottom)
    endShape(CLOSE)

    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta) * radius
        y = sin(theta) * radius
        vertex (x, y, top)
    endShape(CLOSE)

    # round main body
    x1 = 1 * radius
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta) * radius
        y2 = sin(theta) * radius
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, top)
        vertex (x1, y1, bottom)
        

        normal (x2, y2, 0)
        vertex (x2, y2, bottom)
        vertex (x2, y2, top)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

# Draw a hollow cylinder that doesn't have caps 
def hollow_cylinder(radius, top, bottom, sides = 10):
    # round main body
    x1 = 1 * radius
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta) * radius
        y2 = sin(theta) * radius
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, top)
        vertex (x1, y1, bottom)
        
        normal (x2, y2, 0)
        vertex (x2, y2, bottom)
        vertex (x2, y2, top)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
  
# Draw a torus flat in the XY plane
def torus(radius=1.0, tube_radius=0.5, detail_x=16, detail_y=4):
    radius = float(radius)
    tube_radius = float(tube_radius)
    detail_x = int(detail_x)
    detail_y = int(detail_y)

    tube_ratio = (tube_radius / radius)

    def make_torus():
        vertices = []
        normals = []
        for torus_segment in range(detail_x):
            theta = 2 * PI * torus_segment / detail_x
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            segment_vertices = []
            segment_normals = []

            for tube_segment in range(detail_y):
                phi = 2 * PI * tube_segment / detail_y
                cos_phi = cos(phi)
                sin_phi = sin(phi)
                segment_vertices.append(PVector(
                    cos_theta * (radius + cos_phi * tube_radius),
                    sin_theta * (radius + cos_phi * tube_radius),
                    sin_phi * tube_radius,
                ))
                segment_normals.append(PVector(
                    cos_phi * cos_theta,
                    cos_phi * sin_theta,
                    sin_phi,
                ))
            vertices.append(segment_vertices)
            normals.append(segment_normals)
        return vertices, normals

    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("torus", radius, tube_radius, detail_x, detail_y)
    if cache_index in GEOMETRY_CACHE:
        vertices, normals = GEOMETRY_CACHE[cache_index]

    else:
        vertices, normals = make_torus()
        GEOMETRY_CACHE[cache_index] = (vertices, normals)

    for i in range(detail_x):
        for j in range(detail_y):
            beginShape()

            normal(normals[i][j].x, normals[i][j].y, normals[i][j].z)
            vertex(vertices[i][j].x, vertices[i][j].y, vertices[i][j].z)
            normal(normals[(i + 1) % detail_x][j].x, normals[(i + 1) % detail_x][j].y, normals[(i + 1) % detail_x][j].z)
            vertex(vertices[(i + 1) % detail_x][j].x, vertices[(i + 1) % detail_x][j].y, vertices[(i + 1) % detail_x][j].z)
            normal(normals[(i + 1) % detail_x][(j + 1) % detail_y].x, normals[(i + 1) % detail_x][(j + 1) % detail_y].y, normals[(i + 1) % detail_x][(j + 1) % detail_y].z)
            vertex(vertices[(i + 1) % detail_x][(j + 1) % detail_y].x, vertices[(i + 1) % detail_x][(j + 1) % detail_y].y, vertices[(i + 1) % detail_x][(j + 1) % detail_y].z)
            normal(normals[i][(j + 1) % detail_y].x, normals[i][(j + 1) % detail_y].y, normals[i][(j + 1) % detail_y].z)
            vertex(vertices[i][(j + 1) % detail_y].x, vertices[i][(j + 1) % detail_y].y, vertices[i][(j + 1) % detail_y].z)

            endShape(CLOSE)
        
def cone(sides=50):
    sides = int(sides)
    vertices = []
    # draw triangles making up the sides of the cone
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        theta_next = 2.0 * PI * (i + 1) / sides
        
        beginShape()
        #normal(cos(theta), 0.6, sin(theta))
        vertex(cos(theta), 1.0, sin(theta))
        #normal(cos(theta_next), 0.6, sin(theta_next))
        vertex(cos(theta_next), 1.0, sin(theta_next))
        #normal(0.0, -1.0, 0.0)
        vertex(0.0, -1.0, 0.0)
        endShape()

    # draw the cap of the cone
    beginShape()
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        vertex(cos(theta), 1.0, sin(theta))
    endShape()


