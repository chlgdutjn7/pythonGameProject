#맵 생성 프로젝트 
from os import system

from pygame.constants import MOUSEBUTTONDOWN
from Scene.GameScene import *
from PyGameClass import camera, pygamewarpper
import pygame

_Width = 680
_Height = 480

_Mousepos = (0,0)

_MapWidth = int(input("X크기를 입력해주세요 : "))
_MapHeight = int(input("Y크기를 입력해주세요 : "))

_tileinfo = {}
_map = []

_cam = camera()

pygamewarpper().init((_Width,_Height) ,"게임 프로젝트" , )
pygamewarpper().GameStart()



for x in range(_MapWidth):
    _map.append([])
    for y in range(_MapHeight):
        _map[x].append(0)


_tileinfo[0] = pygamewarpper().LoadObj("C:\\pythonproject\\Resource\\Image\\Nature\\backyard_00.png" , "backyard_00")
_tileinfo[1] = pygamewarpper().LoadObj("C:\\pythonproject\\Resource\\Image\\Nature\\Bush1.png" , "Bush_1")
_tileinfo[2] = pygamewarpper().LoadObj("C:\\pythonproject\\Resource\\Image\\Nature\\Bush2.png" , "Bush_2")
                
for item in _tileinfo:
    _tileinfo[item] = pygame.transform.scale(_tileinfo[item], (15,15))



while pygamewarpper._instance.isinGame:
    
    for x in range(_MapWidth):
        for y in range(_MapHeight):
            pygamewarpper().blit(_tileinfo[_map[x][y]] , (x * 16 , y * 16))
           

           
    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygamewarpper()._scrren.set
        elif event.type == pygame.MOUSEBUTTONUP:
            _Mousepos = pygame.mouse.get_pos()
            pass

            
    pygame.display.update();
    
    

    


