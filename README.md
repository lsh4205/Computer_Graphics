# Computer Graphics
Computer graphic projects with [Processing](https://processing.org/) (python) and GLSL (OpenGL)

## 3D Object Design & Animation
[project_2a](https://github.com/lsh4205/Computer_Graphics/tree/main/project_2a) and [project_2b](https://github.com/lsh4205/Computer_Graphics/tree/main/project_2b)
* [project_2a](https://github.com/lsh4205/Computer_Graphics/tree/main/project_2a) - 3D Object Design
* [project_2b](https://github.com/lsh4205/Computer_Graphics/tree/main/project_2b) - 3D Animation
 
[3D Animation Video Link] (https://youtu.be/NId3u7zZ8AM)

![C11D9A5D-C305-4BCC-A49B-CEB6150D](https://user-images.githubusercontent.com/63761734/208246917-4b4e92d1-69e6-4a91-8fd5-cfbe230c98c5.gif)
![DCDACE51-F150-4204-BCAB-EDC28B2E](https://user-images.githubusercontent.com/63761734/208246918-f969f083-0844-40e8-b756-caa5d4051598.gif)

## Ray Tracing
[ray_tracing_3a](https://github.com/lsh4205/Computer_Graphics/tree/main/ray_tracing_p3a) and [ray_tracing_3b](https://github.com/lsh4205/Computer_Graphics/tree/main/ray_tracing_p3b)
* Implement shading algorithm with ambient and specular terms to cast rays at light sources.
* Implement reflection algorithm.

<img width="315" alt="Screen Shot 2022-12-17 at 7 38 45 AM" src="https://user-images.githubusercontent.com/63761734/208244679-39e4a951-2a1a-4969-9cc1-69a5445f12b1.png">  <img width="315" alt="Screen Shot 2022-12-17 at 7 39 17 AM" src="https://user-images.githubusercontent.com/63761734/208244683-fee1d292-833a-4683-9fe9-5a9e0ea1a46a.png">

<img width="315" alt="Screen Shot 2022-12-17 at 8 35 25 AM" src="https://user-images.githubusercontent.com/63761734/208244687-bf845a26-7714-4412-9437-203bd115705f.png">  <img width="314" alt="Screen Shot 2022-12-17 at 7 40 00 AM" src="https://user-images.githubusercontent.com/63761734/208244689-768348e9-f7fe-4df5-a9c9-b0004a41b5fe.png">

## GPU Rendering
[p4_gpu](https://github.com/lsh4205/Computer_Graphics/tree/main/p4_gpu)

## Subdivision and Geodesic Spheres
[p5_meshes](https://github.com/lsh4205/Computer_Graphics/tree/main/p5_meshes)
* Processing that reads in polyhedral models and creates geodesic surface using triangle subdivision.

<img width="318.4" alt="Screen Shot 2022-12-27 at 7 26 47 PM" src="https://user-images.githubusercontent.com/63761734/209739481-2a278370-a89a-4af2-9e0c-080ec8c8cbd6.png"> <img width="318.4" alt="Screen Shot 2022-12-27 at 7 27 55 PM" src="https://user-images.githubusercontent.com/63761734/209739518-85ad6ed0-ef12-48bb-9bff-5fdcd841f391.png">

* After division

<img width="318.4" alt="Screen Shot 2022-12-27 at 7 26 55 PM" src="https://user-images.githubusercontent.com/63761734/209739502-978aefa8-5fba-41c8-9a05-fb725179ec02.png"> <img width="318.4" alt="Screen Shot 2022-12-27 at 7 28 12 PM" src="https://user-images.githubusercontent.com/63761734/209739530-7c1c1740-0a77-48b4-b712-5ab539d734d2.png">

* After normalizaiton

<img width="318.4" alt="Screen Shot 2022-12-27 at 7 30 22 PM" src="https://user-images.githubusercontent.com/63761734/209739550-b1b2bf9e-2d32-4c70-838c-9bbc7c35fe81.png"> <img width="318.4" alt="Screen Shot 2022-12-27 at 7 30 53 PM" src="https://user-images.githubusercontent.com/63761734/209739598-9449eae6-cd4a-46b4-b5d0-9cc728fe430b.png">

* Random color generated in divided traingle plane

<img width="318.4" alt="Screen Shot 2022-12-27 at 7 31 31 PM" src="https://user-images.githubusercontent.com/63761734/209739613-f05e6bd2-a987-4eec-ae57-39cc83c275d3.png"> <img width="318.4" alt="Screen Shot 2022-12-27 at 7 36 48 PM" src="https://user-images.githubusercontent.com/63761734/209740120-68c859ce-c815-4628-9f5b-075c14c3bf12.png">

This program responds to the following keystroke commands:
* 1 - 4 : Read in a mesh file (tetrahedron, octahedron, icosahedron, star).
* d : Create the triangle subdivided current mesh (you should be able to do this more than once).
* i : Inflate the points of the mesh so that they lie on the unit sphere.
* r : Toggle between white and randomly colored faces.
* c : Toggle between showing and not showing the current corner as a sphere.
* n : Change the current corner using the "next" operator.
* p : Change the current corner using the "previous" operator.
* o : Change the current corner using the "opposite" operator.
* s : Change the current corner using the "swing" operator.




