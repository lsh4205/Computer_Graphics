// Fragment shader
// The fragment shader is run once for every pixel
// It can change the color and transparency of the fragment.

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXLIGHT_SHADER

// Set in Processing
uniform sampler2D my_texture;
uniform sampler2D my_mask;
uniform float blur_flag;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 

  // grab the color values from the texture and the mask
  vec4 diffuse_color = texture2D(my_texture, vertTexCoord.xy);
  vec4 mask_color = texture2D(my_mask, vertTexCoord.xy);
  
  vec4 blur_color = vec4(0,0,0,0);
  float blur_r = 3.0;
  float texel_size = 1.0/768.0;
  float i;
  float j;
  for (i = -blur_r; i < blur_r; i++) {
    for (j = -blur_r; j < blur_r; j++) {
      vec2 newVert = vec2(vertTexCoord.x + i * texel_size, vertTexCoord.y + j * texel_size);
      vec4 sample_tex = texture2D(my_texture, newVert);
    }
    blur_color /= (blur_r * blur_r);
  }
  diffuse_color = blur_color;

  // simple diffuse shading model
  float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);

  gl_FragColor = vec4(diffuse * diffuse_color.rgb, 1.0);
}
