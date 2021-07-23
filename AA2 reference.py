import pygame, pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((690, 600))
clock = pygame.time.Clock()

#pymunk space
space = pymunk.Space()
space.gravity = 0, 1000
draw_options = pymunk.pygame_util.DrawOptions(screen)

vs_rect = [(25.0, -40.0), (25.0, 40.0), (-25.0, 40.0), (-25.0, -40.0)]
rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)
rect_shape = pymunk.Poly(rect_body, vs_rect)
rect_body.position = 200,200
space.add(rect_body, rect_shape)

vs_tri = [(0, 0), (0, -80), (80, 0)]
arrow_body = pymunk.Body(body_type=pymunk.Body.STATIC)
arrow_shape = pymunk.Poly(arrow_body, vs_tri)
arrow_body.position = 400,400
space.add(arrow_body, arrow_shape)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    space.debug_draw(draw_options)
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)