from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *

class Block(Button):
    def __init__(self, pos, texture_id=1, **kwargs):
        super().__init__(model='cube', 
                         color = color.white,
                         highlight_color = color.gray,
                         texture=block_textures[texture_id],
                         position = pos, 
                         scale=1, collider='box', 
                         origin_y =-.5,
                         parent=scene,
                         **kwargs)
        
class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None,**kwargs)
        self.blocks = {}

    def generate(self):
        for x in range(MAP_SIZE):
            cube = Block((x,0,0), 2)
            for z in range(MAP_SIZE):
                cube = Block((x,0,z), 2)

    
        
