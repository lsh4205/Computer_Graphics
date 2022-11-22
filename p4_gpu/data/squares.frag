// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;
// Rotate Function
// Create 2x2 transformation matrix
vec2 rotate(vec2 v, float theta) {
	float s = sin(theta);
	float c = cos(theta);
	mat2 rot = mat2(c, -s, s, c);
	return rot * v;
}

void main() { 
  vec2 dist = vertTexCoord.xy - vec2(0.5, 0.5);
  dist = rotate(dist, radians(45));
  vec2 new_dist = dist + vec2(0.5, 0.5);

  float alpha = 1.0;
  float start_x = 0.1;
  float start_y = 0.1;
  float padding = 0.20;
  float punch_size = 0.085;

  // Create 5 x 5 screen and punch in each certain index
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      if (abs(i - 2) + abs(j - 2) > 2) {
        start_x += padding;
        continue;
      } else {
        if (start_x < new_dist.x + punch_size && 
        new_dist.x - punch_size < start_x &&
        start_y < new_dist.y + punch_size &&
        new_dist.y - punch_size < start_y
        ) {
          alpha = 0.0;
        }
      }
      start_x += padding;
    }
    start_x = 0.1;
    start_y += padding;
  }
  gl_FragColor = vec4(0.2, 0.4, 1.0, alpha);
}

