import pygame, sys
from alien import Alien
from player import Player
from explosions import Explosion


# TODO: Add clipping at screen's edge, refctor to it's own file, add shooting, add more enemy sprites, add UI (lives, health, level number, ...), add ESC key exiting the game, add fullscreen mode and stretching the background
# Bullet can be it's own object. attributes of size, speed, color, damage (for later). Spawn one on spacebar push, add to a list that tracks it, blit it to the screen, update on every loop.
# Figure out if bullets are sprites too. Figure out how to clip at the screen's edge. Refactor your code in to functions and abstract it away to different files. Write out a wireframe of how the main game loop is supposed to run. Model your code after this diagram. ORGANIZE AND MAKE IT LOOK NEAT. 


# Alright. Start from scratch and build this the right way. 
# - Everything is a Sprite: player, aliens, bullets (for now, that's it)
# - player should be it's own class inheriting from Sprte. Addition atrributes: Health, Lives, move speed, firerate, damage/shot, shields, armor, what else?
# - bullets will be their own class. Additonal attributes are: Size, damage, speed, color?
# - aliens will be their own class. Additonal atrributes are: Health, move speed, color, projectil type, damage/shot, more here?
# - Collision detection between sprites, walls
# - Fullscreen option needs to be implemented right away
# - Scrolling background? Multiple backgrounds?
# - Optimize framerate, smoothness, and controls. 
# Here we go. 

# This is fun
def run_game():


    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    dt = 0

    # Load assets
    # background = pygame.image.load("images/background.jpg")

    # Draw the screen
    #TODO: Figure out how to import an image and blit it to the entire background to fit. I don't know if pygame can do it, I might need another module.
    background = (51, 209, 176)
    screen_size = pygame.display.get_desktop_sizes()
    screen = pygame.display.set_mode(screen_size[0])
    screen.fill(background)

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # Spwawn 20 aliens to the screen
    alien_group = pygame.sprite.Group()
    screen_chunk = screen_width / 10
    for i in range(0, 10):


        new_alien_first_row = Alien(i * screen_chunk + screen_chunk, screen.get_height() / 4)
        new_alien_second_row = Alien(i * screen_chunk + screen_chunk, screen.get_height() / 2)
        alien_group.add(new_alien_first_row)
        alien_group.add(new_alien_second_row)

    alien_group.draw(screen)

    player = Player(screen.get_width() / 2, screen.get_height() * 0.75)
    player_group = pygame.sprite.Group(player)
    player_group.draw(screen)

    # Create Groups to keep track of bullets on the screen
    player_bullet_group = pygame.sprite.Group() 
    aliens_bullet_group = pygame.sprite.Group()
    player_shoot_timer = 0

    # Create group for keeping track of explosions on the screen
    explosions_group = pygame.sprite.Group()

    # Main game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Check and see if we moved to a new level (all aliens dead)
        # If so, load in player and appropriate batch of aliens


        # Erase the old frame
        screen.fill(background)
        # player_group.clear(player.get_surface(), screen)

        # Update explosions, if any
        for explosion in explosions_group:
            if not explosion.update_image():
                explosions_group.remove(explosion)


        keys = pygame.key.get_pressed()
        current_player_rect = player.get_rect()
        
        if keys[pygame.K_ESCAPE]:
            print(player_bullet_group)
            sys.exit()
        if keys[pygame.K_w] and player.rect.y > 0:
            player.update_rect(0, -600 * dt)
        if keys[pygame.K_s] and player.rect.y + player.get_rect().height < screen.get_height():
            player.update_rect(0, 600 * dt)
        if keys[pygame.K_a] and player.rect.x > 0:
            player.update_rect(-600 * dt , 0)
        if keys[pygame.K_d] and player.rect.x + player.get_rect().width < screen.get_width():
            player.update_rect(600 * dt, 0)

        if pygame.sprite.spritecollideany(player, alien_group):
            player.set_rect(current_player_rect.x, current_player_rect.y)

        # Update bullet positions and check for collisions
        for bullet in player_bullet_group.sprites():
            bullet.update_rect()
            if pygame.sprite.spritecollideany(bullet, alien_group):
                explosions_group.add(Explosion(bullet.get_rect().x - 20, bullet.get_rect().y - 20))
                bullet.remove(player_bullet_group)
            if bullet.get_rect().y < 0: # Bullet has left the screen
                player_bullet_group.remove(bullet)

        #  
        if player_shoot_timer >= 0.1 and keys[pygame.K_SPACE]:
            player_bullet_group.add(player.fire_bullet())
            player_shoot_timer = 0

        
        # Draw everything        

        explosions_group.draw(screen)
        player_bullet_group.draw(screen)
        player_group.draw(screen)
        alien_group.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player_shoot_timer += dt

run_game()