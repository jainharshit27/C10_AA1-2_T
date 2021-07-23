import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
space = pymunk.Space()
space.gravity = 0, 1000
draw_options = pymunk.pygame_util.DrawOptions(screen)

target_body = pymunk.Body(body_type=pymunk.Body.STATIC)
target_shape = pymunk.Segment(target_body, (0,0), (width, height), 1)
space.add(target_body, target_shape)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    space.debug_draw(draw_options)    

    #space reload
    space.step(1/60)
    clock.tick(60)
    pygame.display.update()