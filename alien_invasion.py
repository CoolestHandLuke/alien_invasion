import pygame, sys
from settings import Settings
from alien import Alien
from player import Player

# TODO: Add clipping at screen's edge, refctor to it's own file, add shooting, add more enemy sprites, add UI (lives, health, level number, ...), add ESC key exiting the game, add fullscreen mode and stretching the background
# Bullet can be it's own object. attributes of size, speed, color, damage (for later). Spawn one on spacebar push, add to a list that tracks it, blit it to the screen, update on every loop.
# Figure out if bullets are sprites too. Figure out how to clip at the screen's edge. Refactor your code in to functions and abstract it away to different files. Write out a wireframe of how the main game loop is supposed to run. Model your code after this diagram. ORGANIZE AND MAKE IT LOOK NEAT. 

# This is fun
def run_game():


    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    dt = 0
    settings = Settings()

    # Load assets
    background = pygame.image.load("images/background.jpg")

    # Draw the screen, sprites, and UI
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen.blit(background, (0, 0))
    alien = Alien(screen.get_width() / 2, screen.get_height() / 2)
    alien_group = pygame.sprite.Group(alien)
    alien_group.draw(screen)
    player = Player(screen.get_width() / 2, screen.get_height() / 4)
    player_group = pygame.sprite.Group(player)
    player_group.draw(screen)

    # Main game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                sys.exit()

        # Erase the old frame
        screen.blit(background, player.get_rect(), player.get_rect())
        # player_group.clear(player.get_surface(), screen)
        keys = pygame.key.get_pressed()
        current_player_rect = player.get_rect()
        
        if keys[pygame.K_w]:
            print("player moving up")
            player.update_rect(0, -600 * dt)
            # if player.get_rect().y <= 0:
            #     player.set_rect(0, 600 * dt)
        if keys[pygame.K_s]:
            print("player moving down")
            player.update_rect(0, 600 * dt)
            # if player.get_rect().y >= screen.get_height():
            #     player.set_rect(0, -600 * dt)
        if keys[pygame.K_a]:
            print("player moving left")
            player.update_rect(-600 * dt , 0)
            # if player.get_rect().x <= 0:
            #     player.set_rect(600 * dt, 0)
        if keys[pygame.K_d]:
            print("player moving right")
            player.update_rect(600 * dt, 0)
            # if player.get_rect() >= screen.get_width() :
            #     player.set_rect(-600 * dt, 0)

        if pygame.sprite.spritecollideany(player, alien_group):
            print("Collision detected")
            print("Current Position: x:" + str(current_player_rect.x) + "\ny: " + str(current_player_rect.y))
            player.set_rect(current_player_rect.x, current_player_rect.y)
        if keys[pygame.K_SPACE]:
            pass
            #TODO: Add shooting here


        player_group.draw(screen)
        pygame.display.flip()
        dt = clock.tick(120) / 750

run_game()