#맵 생성 프로젝트 


from os import system
from Scene.GameScene import *
from PyGameClass import camera, pygamewarpper
import pygame

_Width = 680
_Height = 480

_MapWidth = int(input("X크기를 입력해주세요 : "))

_MapHeight = int(input("Y크기를 입력해주세요 : "))

_tileinfo = {}
_map = []
_MouseClickCheck = False
_beforemousePos = (0,0)

_Cam = camera(pygame.Vector2(0,0) , pygame.Vector2(0,0))
pygamewarpper().init((_Width,_Height) ,"게임 프로젝트" ,_Cam )
pygamewarpper().GameStart()



for x in range(_MapWidth):
    _map.append([])
    for y in range(_MapHeight):
        _map[x].append(0)


_tileinfo[0] = pygamewarpper().LoadObj("/Users/choihyeongsun/Github/GameProjectPython/Resource/Image/Nature/backyard_00.png" , "backyard_00")
_tileinfo[1] = pygamewarpper().LoadObj("/Users/choihyeongsun/Github/GameProjectPython/Resource/Image/Nature/Bush1.png" , "Bush_1")
_tileinfo[2] = pygamewarpper().LoadObj("/Users/choihyeongsun/Github/GameProjectPython/Resource/Image/Nature/Bush2.png" , "Bush_2")
                
for item in _tileinfo:
    _tileinfo[item] = pygame.transform.scale(_tileinfo[item], (15,15))



while pygamewarpper._instance._isinGame:
    
    mouse = pygame.Vector2(pygame.mouse.get_pos());
    
    
    
    for x in range(_MapWidth):
        for y in range(_MapHeight):
            pygamewarpper().blit(_tileinfo[_map[x][y]] , (x * 16 , y * 16))
           

           
    for event in pygame.event.get():        
        
        if event.type==pygame.QUIT:
            pygame.quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            _MouseClickCheck = True
         
            
        elif event.type == pygame.MOUSEBUTTONUP:
            _MouseClickCheck = False
            _beforemousePos = _Cam.camera
            
            
    if _MouseClickCheck == True:
        _Cam.camera = _beforemousePos + (mouse - _beforemousePos) * 0.3
        print (_Cam.camera)
    

    pygame.display.update();
    
    

    


