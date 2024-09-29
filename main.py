import pygame as pg
from constants import * 

def main():

  pg.init()
  screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  game = True

  while game:
    for event in pg.event.get():
      if event.type == pg.QUIT:
          return
    screen.fill(000)
    pg.display.flip()

  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
  main()