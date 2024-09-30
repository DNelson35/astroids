import pygame 
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  game = True
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  AsteroidField.containers = (updatable)
  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)

  feild = AsteroidField()

  player = Player(x, y)
  
  while game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill(000)
    for update in updatable:
      update.update(dt)
    for draw in drawable:
      draw.draw(screen)
    for asteroid in asteroids:
      if asteroid.check_collision(player):
        print("Game over!")
        game = False
    for asteroid in asteroids:
      for shot in shots:
        if shot.check_collision(asteroid):
          asteroid.split()
          shot.kill()
        
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000


  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
  main()