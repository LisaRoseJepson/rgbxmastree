from tree import RGBXmasTree
from time import sleep
from colorzero import Color

tree = RGBXmasTree()
i = 0
#tree.color = Color('red')

#for pixel in tree:
#	pixel.color = Color('purple')
#	sleep(1)

for pixel in tree:
	
	if i == 3:
		tree[i].color = Color('yellow')
	elif i in [0, 6, 7, 12, 15, 16, 19, 24]:
		tree[i].color = Color('blue')
	elif i in [1, 5, 8, 11, 14, 17, 20, 23]:
		tree[i].color = Color('red')
	else:
		tree[i].color = Color('green')
	i += 1


#for pixel in tree:
#	print(pixel)
