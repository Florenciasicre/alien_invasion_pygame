import sys 
import pygame 
from settings import Settings
class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        #Create de window. surface 
        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_hight)
    
        #the entire game window 
        pygame.display.set_caption('ALIEN_INVASION')
        #background-color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        while True: 
            #mouse events and keyboard
            #to access the event 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()
                self.screen.fill(self.bg_color)
            # to make the recently screen visible 
            pygame.display.flip()
            
          
if __name__ == '__main__':
   ai = AlienInvasion()
   ai.run_game()
