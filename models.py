from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *
from perlin_noise import PerlinNoise
from numpy import *
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader


class Tree(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(model='assets\\models\\minecraft_tree\\scene.gltf', 
                         color = color.white,
                         highlight_color = color.gray,
                         position = pos, 
                         scale=5, 
                         collider='box', 
                         origin_y =.5,
                         shader = basic_lighting_shader,
                         parent=scene,
                         **kwargs)

class Block(Button):
    current_block = DEFAULT_BLOCK

    def __init__(self, pos, texture_id=1, **kwargs):
        super().__init__(model='cube', 
                         color = color.color(0, 0, random.uniform(0.9, 1)),
                         highlight_color = color.gray,
                         texture=block_textures[texture_id],
                         position = pos, 
                         scale=1, collider='box', 
                         origin_y =-.5,
                         parent=scene,
                         shader = basic_lighting_shader,
                         **kwargs)
        
class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None,**kwargs)
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=3000)

    def generate(self):
        for x in range(MAP_SIZE):
            cube = Block((x,0,0), 2)
            for z in range(MAP_SIZE):
                y = floor(self.noise([x/24, z/24])*6)
                cube = Block((x,y,z), DEFAULT_BLOCK)

                rand_num = random.randint(1, TREE_DENSITY)
                if rand_num == 32:
                    tree = Tree((x,y+1,z))


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.held_block = Entity(model ='cube', texture=block_textures[Block.current_block], parent=camera.ui, position=(0.6, -0.4),
                                 rotation = Vec3(30, -30, 10),
                                 shader = basic_lighting_shader,
                                 scale=0.2
                                 )
    def input(self, key):
        super().input(key)
        if key == 'left mouse down' and mouse.hovered_entity:
            destroy(mouse.hovered_entity)
        if key == 'right mouse down' and mouse.hovered_entity:
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit and isinstance(hit_info.entity,Block):
                Block(hit_info.entity.position + hit_info.normal, Block.current_block)
        
        if key == 'scroll up':
            Block.current_block += 1
            if Block.current_block >= len(block_textures):
                Block.current_block = 0
            self.held_block.texture = block_textures[Block.current_block]
        if key == 'scroll down':
            Block.current_block -= 1
            if Block.current_block < 0:
                Block.current_block = len(block_textures) - 1
            self.held_block.texture = block_textures[Block.current_block]


    
        
