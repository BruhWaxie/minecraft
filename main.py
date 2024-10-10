from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

from settings import *
from models import Block, Map

sky = Sky(texture='sky_sunset')
cube = Block((3,0,0), 2)
#tree = Entity(model='assets\\models\\minecraft_tree\\scene.gltf',origin_y =-.5)
map = Map()
map.generate()
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
ground.y = 0

player = FirstPersonController() 
window.fullscreen = True
app.run()