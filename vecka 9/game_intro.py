import pygame
import random
from simulation import PhysicsObject, Player, PhysicsSim
SCREEN_HEIGHT = 768

SCREEN_WIDTH = 1024

# Pygame
# 1. En yta att rita på.
# 2. Kan spela upp ljud
# 3. Hanterar input från mus och tangentbord



# Ett spel gör typiskt följande
#
# 1. Öppnar upp ett fönster att rita gränssnittet på.
# 2. Skapar någon typ av simulering
# 3. Tar emot input från användaren, kan var mus, tangentbord, joystick etc.
# 4. Uppdaterar simuleringen
# 5. Ritar ut en grafisk representation av simuleringen.
# 6. Gå till steg 3


pygame.init()


font = pygame.freetype.SysFont(None, size=20)
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
# player_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
# boll_pos = (100, 0)
# boll_vel = (0, 0)
# player_vel = (0, 0)
clock = pygame.time.Clock()
physical_objects = []

player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (0,0))
boll = PhysicsObject((100, 0), (0, 0))

physical_objects.append(player)
physical_objects.append(boll)

sim = PhysicsSim(SCREEN_WIDTH, SCREEN_HEIGHT)

for _ in range(300):
    p = PhysicsObject((random.randint(0, 1024), random.randint(0, 150)), (0, 0))
    physical_objects.append(p)


sim.objects.extend(physical_objects)

while running:
    dt = clock.tick(30)
    seconds = 0.001 * dt
    # Ta emot input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            elif event.key == pygame.K_RIGHT:
                player.go_right()
            elif event.key == pygame.K_UP:
                player.jump()

    sim.update(seconds)
    # Rita ut en grafisk representation
    display.fill((136, 198, 231))

    text_surface, text_rect = font.render("En text", fgcolor=(0, 0, 0))
    display.blit(text_surface, (500, 50))
    for po in physical_objects:
        pygame.draw.rect(display, (255, 0, 0), (int(po.pos[0]), int(po.pos[1]), 10, 10))

    pygame.display.flip()

