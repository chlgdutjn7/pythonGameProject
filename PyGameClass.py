#이 로직들은 라이브 러리입니다.
#게임프로젝트 보조 프로젝트 모두 사용합니다.
from typing import Tuple
from pygame import Vector2, math
import pygame


#object 기본정보  (위치 회전 크기), 이미지 정보
class ObjInfo:
    def __init__ (self,Image, Position , rotate , scale):
        self.position = Position
        self.rotate = rotate
        self.scale = scale
        self.image = Image;
        
        
class camera:
    
    def __init__ (self , camera , player):
        self.camera = camera
        self.player = player
        
    
    
     


class pygamewarpper:
    
    _instance = None
       
    #싱글터 제작
    def __new__(cls, *args, **kwargs):
        if not cls._instance :
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    #pygame 초기화
    def init(self, scrrenSize = Tuple , title = str , cam = camera):
        pygame.init()
        self._scrrenSize = scrrenSize
        self._scrren = pygame.display.set_mode(scrrenSize)
        self.isinGame = False
        self.ImageInfo = {}
        self.Cam = cam;
        pygame.display.set_caption(title)
    
    
    #게임 시작
    def GameStart(self):
        self.isinGame = True    
    
    #게임 종료
    def GameQuit(self):
        self.isinGame = False
        
    #이미지 저장
    def LoadObj(self, Imagepath = str , ImageName = str):
        image = pygame.image.load(Imagepath)
        self.ImageInfo[ImageName] = image
        return image
                
    def MousePos():
        return pygame.mouse.get_pos()
    
    def Clock(self):
        self.clock = pygame.time.Clock()    
    
    def blit(self , img , position):
        self._scrren.blit(img , position + self.Cam);
        
        
    def pygameUpdate():
        pygame.display.update();

    
        
        

    