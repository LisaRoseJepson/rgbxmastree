from tree import RGBXmasTree
from time import sleep
from colorzero import Color
import random

tree = RGBXmasTree()
#tree.color = Color('red')

#for pixel in tree:
#	pixel.color = Color('purple')
#	sleep(1)

def lights():
	i = 0
	for pixel in tree:

		if i == 3:
			tree[i].color = Color('yellow')
		elif random.randint == 1:
 			if i in [0, 6, 7, 12, 15, 16, 19, 24]:
				tree[i].color = (0, 0, 1)
			elif i in [1, 5, 8, 11, 14, 17, 20, 23]:
				tree[i].color = (1, 0, 0)
			else:
				tree[i].color = (0, 0, 1) 
		else:
			tree[i].color = (0, 0, 0)
		i += 1
	time.sleep(1)

while True:
	lights()
#for pixel in tree:
#	print(pixel)
