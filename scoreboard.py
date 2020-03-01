from display import *



#screen_size = (width, height) = (600, 150)
#screen = pygame.display.set_mode(screen_size)

class Scoreboard():
    def __init__(self,x=-1,y=-1):
        self.score = 0
        self.tempimages,self.temprect = load_sprites('numbers.png',12,1,11,int(11*6/5))
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, score):
        score_digits = [int(i) for i in str(score)]
        for _ in range(len(score_digits), 5):
            score_digits.insert(0, 0)
        self.image.fill(background_color)
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0
