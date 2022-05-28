import pygame
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 550
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Spot The Difference")

GAME_FOLDER = 'L:/Git/Pygame/Spot the difference/'
BLUE = pygame.Color(0,0, 255)
RED = pygame.Color(255,0,0)
background_image = pygame.image.load(GAME_FOLDER + 'image.jpg')

chances = 5
click_points = []
actual_points = [(570,467),(662,184),(876,147),(905,375),(722,270)]
radius = 30

running = True
FPS = 30
clock = pygame.time.Clock()
while running:
    display_surface.blit(background_image, (0, 0))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:  # LEFT mouse button
                if chances:
                    check = False
                    for i, point in enumerate(actual_points):  # (0,first_point); (1,second_point); ...; (n,last_point)
                        if abs(point[0] - ev.pos[0]) < radius and abs(point[1] - ev.pos[1]) < radius:
                            check = True
                            actual_points.pop(i)
                            break

                    click_points.append((ev.pos, check))
                    chances -= 1

    for point in click_points:
        if point[1]:
            pygame.draw.circle(surface=display_surface, color=BLUE, center=point[0], radius=radius, width=2)
        else:
            pygame.draw.circle(surface=display_surface, color=RED, center=point[0], radius=radius, width=2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()