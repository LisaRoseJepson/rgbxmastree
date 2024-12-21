from tree import RGBXmasTree
from time import sleep
from colorzero import Color
import random

tree = RGBXmasTree()
#tree.color = Color('green')

#for pixel in tree:
#	pixel.color = Color('purple')
#	sleep(1)

#def lights():
#    i = 0
#    for pixel in tree:
#        on = random.randint(0, 1)
#        if i == 3:
#            tree[i].color = Color('yellow')
#        elif on  == 1:
#            if i in [0, 6, 7, 12, 15, 16, 19, 24]:
#                tree[i].color = (0, 0, 1)
#            elif i in [1, 5, 8, 11, 14, 17, 20, 23]:
#                tree[i].color = (1, 0, 0)
#            else:
#                tree[i].color = (0, 1, 0) 
#        else:
#            tree[i].color = (0, 0, 0)
#        i += 1
#    sleep(0.25)
#
#
#def lights2():
#    i = 0
#    for pixel in tree:
#        if i == 3:
#            tree[i].color = Color('yellow')
#        elif i in [0, 6, 7, 12, 15, 16, 19, 24]:
#            tree[i].color = (0, 0, 1)
#        elif i in [1, 5, 8, 11, 14, 17, 20, 23]:
#            tree[i].color = (1, 0, 0)
#        else:
#            tree[i].color = (0, 1, 0) 
#        i += 1
#    sleep(0.25)
#
#    for pixel in tree:
#       pixel.color = (0, 0, 0)
#    sleep(0.25)


#while True:
#	lights2()
i = 0

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
#    sleep(0.25)
#    tree.color = (0, 0, 0) 
