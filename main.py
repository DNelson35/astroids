import pygame 
from constants import * 
from player import Player

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  game = True
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)
  updatable = pygame.sprite.Group(player)
  drawable = pygame.sprite.Group(player)

  while game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill(000)
    for draw in drawable:
      draw.draw(screen)
    for update in updatable:
      update.update(dt)
      
    pygame.display.flip()
    dt = clock.tick(60) / 1000


  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
  main()