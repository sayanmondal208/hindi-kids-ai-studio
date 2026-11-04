import bpy
import math

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Materials
def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    return mat

white = material("Rabbit White", (0.95, 0.88, 0.78))
pink = material("Ear Pink", (1.0, 0.35, 0.45))
black = material("Eyes", (0.02, 0.02, 0.02))
green = material("Grass", (0.12, 0.45, 0.12))

def sphere(name, location, scale, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32, ring_count=16, location=location
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.shade_smooth()
    obj.data.materials.append(mat)
    return obj

# Rabbit body and head
sphere("Rabbit Body", (0, 0, 1), (0.65, 0.45, 0.75), white)
sphere("Rabbit Head", (0, -0.15, 2), (0.65, 0.55, 0.62), white)

# Ears
for x in [-0.35, 0.35]:
    sphere("Rabbit Ear", (x, -0.1, 2.85), (0.18, 0.16, 0.65), white)
    sphere("Pink Ear", (x, -0.245, 2.85), (0.10, 0.035, 0.48), pink)

# Eyes
for x in [-0.23, 0.23]:
    sphere("Rabbit Eye", (x, -0.65, 2.1), (0.09, 0.06, 0.12), black)

# Nose
sphere("Rabbit Nose", (0, -0.7, 1.88), (0.11, 0.07, 0.08), pink)

# Ground
bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, 0))
ground = bpy.context.object
ground.name = "Green Grass"
ground.data.materials.append(green)

# Camera
bpy.ops.object.camera_add(location=(5, -9, 4))
camera = bpy.context.object
camera.rotation_euler = (math.radians(68), 0, math.radians(29))
bpy.context.scene.camera = camera

# Lighting
bpy.ops.object.light_add(type='AREA', location=(0, -5, 7))
light = bpy.context.object
light.data.energy = 1200
light.data.shape = 'DISK'
light.data.size = 5

# Animation: rabbit moves forward
body = bpy.data.objects["Rabbit Body"]
head = bpy.data.objects["Rabbit Head"]

body.location.x = -2
head.location.x = -2
body.keyframe_insert(data_path="location", frame=1)
head.keyframe_insert(data_path="location", frame=1)

body.location.x = 2
head.location.x = 2
body.keyframe_insert(data_path="location", frame=72)
head.keyframe_insert(data_path="location", frame=72)

# Render settings
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 72
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "//rabbit.png"

print("3D Rabbit scene created!")
