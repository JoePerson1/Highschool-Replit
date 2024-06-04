import pygame
from random import *

class NotSquare(pygame.sprite.Sprite):
  def __init__(self, picture, x, y, speed, scale):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(picture).convert_alpha()
    self.image = pygame.transform.scale(self.image, scale)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.speed = speed

class Car(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((20, 20))
    self.rect = self.image.get_rect()
    type = randint(0, 7)
    self.speed = (type+1)*4
    self.image.fill(colors[type])
    direction = randint(0, 1)
    y = randrange(0, bgY+1, 20)
    if direction:
      self.left = True
      self.rect.center = (-20, y)
    else:
      self.left = False
      self.rect.center = (bgX+20, y)

  def update(self):
    global stationary
    if stationary != 0:
      self.rect.move_ip(0, stationary*character.speed)
    if self.left:
      self.rect.move_ip(self.speed, 0)
    else:
      self.rect.move_ip(-self.speed, 0)
    if self.rect.left < -20 or self.rect.right > bgX+20 or self.rect.bottom > bgY:
      self.kill()

bgX = 400
bgY = 400

run = True
run2 = True
screen = pygame.display.set_mode((bgX, bgY))
pygame.display.set_caption('Passy Street')
clock = pygame.time.Clock()

colors = ['red', 'blue', 'orange', 'green', 'purple', 'navy', 'crimson', 'black']
cars = pygame.sprite.Group()
character = NotSquare('chicken.png', 200, 300, 20, (20, 20))
score = 0
count = 0

while run:
  stationary = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        score += 5
        stationary += 1
      elif event.key == pygame.K_s:
        score -= 5
        stationary -= 1
      elif event.key == pygame.K_a:
        character.rect.centerx -= character.speed
      elif event.key == pygame.K_d:
        character.rect.centerx += character.speed

  if character.rect.right > bgX:
    character.rect.right = bgX
  elif character.rect.left < 0:
    character.rect.left = 0

  count += 1
  if count % 1 == 0:
    car = Car()
    cars.add(car)
  cars.update()
  cars.draw(screen)

  pygame.display.flip()
  pygame.draw.rect(screen, 'white', (0, 0, bgX, bgY))
  screen.blit(character.image, character.rect)

  if pygame.sprite.spritecollide(character, cars, False):
    print('Score: '+str(score))
    while run2:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
          run2 = False

  clock.tick(12)