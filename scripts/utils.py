"""
- LICENSE: GPL-3.0
- Made by sByte

A script where i will add useful functions i use when
coding scripts, like create_block, destroy_block, etc

- How to use?
Put this script on the top of the script list in config.toml,
to be able to use the functions.

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━> FUNCTIONS <━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> create_block(coords: tuple, save: bool=False, color: tuple=None)┃
┣> Available on protocol and connection classes.                    ┃
┃                                                                   ┃
┣> Create a block, on the map. If Save is True, block               ┃
┃  will be saved in the map for future connections.                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> destroy_block(coords: tuple, save: bool=False)                  ┃
┣> Available on protocol and connection classes.                    ┃
┃                                                                   ┃
┣> Destroy a block. If Save is True, destroyed block                ┃
┃  will be saved in the map for future connections.                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> gravity(body: dict)                                             ┃
┣> Available only in protocol                                       ┃
┃                                                                   ┃
┣> Calculate how the gravity will work passing the                  ┃
┃  mass and velocity.                                               ┃
┃                                                                   ┃
┣━> Body structure                                                  ┃
┣> position: z_coordinate (Float)                                   ┃
┣> mass: Int                                                        ┃
┣> velocity: Int                                                    ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> gradient_fog(tuple: fog, float: speed)							┃
┣> Available only in protocol										┃
┃																	┃
┣> Change fog color in a gradient effect.							┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━> FUNCTIONS <━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
from pyspades.contained import BlockAction, SetColor
from pyspades.constants import BUILD_BLOCK, DESTROY_BLOCK
from twisted.internet.reactor import callLater
from pyspades.common import make_color

def destroy_block(c, coords):
	x,y,z = coords

	block_action = BlockAction()
	block_action.value = DESTROY_BLOCK
	block_action.x = x
	block_action.y = y
	block_action.z = z
	block_action.player_id = 33
	c.send_contained(block_action)

def create_block(c, coords, color=False):
	x,y,z = coords
	if color:
		set_color = SetColor()
		set_color.player_id = 33
		set_color.value = make_color(*color)
		c.send_contained(set_color)

	block_action = BlockAction()
	block_action.value = BUILD_BLOCK
	block_action.x = x
	block_action.y = y
	block_action.z = z
	block_action.player_id = 33
	c.send_contained(block_action)

def apply_script(protocol, connection, config):
	class utilProtoc(protocol):
		def create_block(self, coords, save=False, color=False):
			create_block(self, coords, color)

			if save:
				if not color:
					color = (0,0,0)
				self.map.set_point(*coords, color)

		def destroy_block(self, coords, save=False):
			destroy_block(self, coords)

			if save:
				self.map.destroy_point(*coords)

		def gravity(self, body):
			force = body["mass"]*-9.87
			body["velocity"] -= force*-0.02
			body["position"] += body["velocity"]*-0.02

			return body

		def gradient_fog(self, color_to, speed=0.01):
			r,g,b = self.fog_color
			rt,gt,bt = color_to
			if r != rt or g != gt or b != bt:
				if r > rt:
					r-=1
				elif r < rt:
					r+=1

				if g > gt:
					g-=1
				elif g < gt:
					g+=1

				if b > bt:
					b-=1
				elif b < bt:
					b+=1

				self.set_fog_color((r,g,b))
				callLater(speed, self.gradient_fog, color_to, speed)

	class utilConnec(connection):
		def create_block(self, coords, save=False, color=False):
			create_block(self, coords, color)

		def destroy_block(self, coords, save=False):
			destroy_block(self, coords)

	return utilProtoc, utilConnec