from comage_core import Pool_maker, Animate_water
from time import sleep
from termcolor import *
from colorama import init
init()
def Water_paint(sprite_chain):
	# sprite_chain = sprite_chain.replace("-",colored("-", color="cyan"))
	# sprite_chain = sprite_chain.replace("/",colored("/", color="cyan"))
	# sprite_chain = sprite_chain.replace("_",colored("_", color="cyan"))
	# sprite_chain = sprite_chain.replace("^",colored("^", color="cyan"))

	sleep(0.1)
	return sprite_chain

our_pool = Pool_maker(lenght=13,height=13,echelles=1)
print(our_pool)
sleep(1)

while True:
	our_pool = Animate_water(our_pool)
	sleep(0.1)
	print(Water_paint(our_pool))
	our_pool = Animate_water(our_pool)
	sleep(0.1)
	print(Water_paint(our_pool))

input("")