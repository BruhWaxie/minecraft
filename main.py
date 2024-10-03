from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
sky = Sky(texture='sky_sunset')
cube = Entity(model='cube', texture='grass', scale=1, collider='box', origin_y =-.5)
tree = Entity(model='assets\\models\\minecraft_tree\\scene.gltf',origin_y =-.5)

ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
ground.y = 0

def spin():
    cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)

cube.on_click = spin
player = FirstPersonController() 

app.run()