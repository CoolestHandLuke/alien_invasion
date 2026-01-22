import pygame, sys
from alien import Alien
from player import Player
from exhaust import Exhaust
from explosions import Explosion
import json


# TODO:add UI (lives, health, ), add hotkey to change the bullets
# Add in death from touching aliens. Add in alien shooting. Balance damage and speed. Add lives and lose condition.
# Add different explosions. Put them away in to a json file. Add powerups to different bullets (change size, damage, explosions). Add a death animation (explosions). 
# Add exhaust to the ship
# Add button to start a new game. 
# CLEAN UP YOUR DAMN COMMENTS.
# Make it PEP8 standardized. 
# There's a lot to do here. But the process is fun. And that's why I do it :)

def run_game():


    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    dt = 0

    # Draw the screen
    #TODO: Figure out how to import an image and blit it to the entire background to fit. I don't know if pygame can do it, I might need another module.
    background = (51, 209, 176)
    screen_size = pygame.display.get_desktop_sizes()
    screen = pygame.display.set_mode(screen_size[0])
    screen.fill(background)

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # Create the group to hold the aliens, and load in the JSON holding alien information
    alien_group = pygame.sprite.Group()
    SCREEN_CHUNK = screen_width / 10
    RIGHT = 1
    LEFT = -1
    level_tracker = 0
    level_nums = ["level_1", "level_2", "level_3"]
    current_level = "level_1"
    with open("alien_types.json", 'r') as file:
        data = json.load(file)
    

    #Create the player and exhaust sprites and put it in to a Group for ease of QOL purposes
    player = Player(screen.get_width() / 2, screen.get_height() * 0.75)
    exhaust = Exhaust(player.get_rect().x, player.get_rect().y + player.get_height() / 3)
    player_group = pygame.sprite.Group(exhaust, player)
    player_group.draw(screen)

    # Create Groups to keep track of bullets on the screen
    player_bullet_group = pygame.sprite.Group() 
    aliens_bullet_group = pygame.sprite.Group()  # TODO Add in aliens shooting back.
    player_shoot_timer = 0

    # Create group for keeping track of explosions on the screen
    explosions_group = pygame.sprite.Group()

    new_level = True
    PLAYER_IDLE = True
    LAST_MOVEMENT = None

    # Main game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Check and see if we moved to a new level (all aliens dead)


        # If so, load in player and appropriate batch of aliens
        if new_level and current_level:
            for i in range(0, 5):
                    new_alien_first_row = Alien(data[current_level], i * SCREEN_CHUNK + SCREEN_CHUNK, screen.get_height() / 4, RIGHT)
                    new_alien_second_row = Alien(data[current_level], i * SCREEN_CHUNK + SCREEN_CHUNK, screen.get_height() / 2, LEFT)
                    alien_group.add(new_alien_first_row)
                    alien_group.add(new_alien_second_row)

            alien_group.draw(screen)
            new_level = False


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
            sys.exit()
        if keys[pygame.K_w] and player.rect.y > 0:
            player.update_rect(0, -600 * dt)
        elif keys[pygame.K_s] and player.rect.y + player.get_rect().height < screen.get_height():
            player.update_rect(0, 600 * dt)
        if keys[pygame.K_a] and player.rect.x > 0:
            player.update_rect(-600 * dt , 0)
            PLAYER_IDLE = False
            player.set_image(LEFT, PLAYER_IDLE)
            LAST_MOVEMENT = LEFT
        elif keys[pygame.K_d] and player.rect.x + player.get_rect().width < screen.get_width():
            player.update_rect(600 * dt, 0)
            PLAYER_IDLE = False
            player.set_image(RIGHT, PLAYER_IDLE)
            LAST_MOVEMENT = RIGHT

        if PLAYER_IDLE and LAST_MOVEMENT == RIGHT:
            player.set_image(LEFT, PLAYER_IDLE)

        elif PLAYER_IDLE and LAST_MOVEMENT == LEFT:
            player.set_image(RIGHT, PLAYER_IDLE)

        PLAYER_IDLE = True

        # Update the exhaust sprite
        exhaust.set_image()

        if pygame.sprite.spritecollideany(player, alien_group):
            player.set_rect(current_player_rect.x, current_player_rect.y)

        # Update the positions of aliens. Check for clipping and make them move the other direction if they hit the screen edge. 
        for alien in alien_group.sprites():
            alien.move()

        # Update bullet positions and check for collisions
        for bullet in player_bullet_group.sprites():
            bullet.update_rect()
            struck_alien = pygame.sprite.spritecollideany(bullet, alien_group)
            if struck_alien:
                struck_alien.update_health(bullet.get_damage())
                explosions_group.add(Explosion(bullet.get_rect().x - 20, bullet.get_rect().y - 30))
                bullet.remove(player_bullet_group)
            if bullet.get_rect().y < 0: # Bullet has left the screen
                player_bullet_group.remove(bullet)

        #  
        if keys[pygame.K_SPACE] and player_shoot_timer > player.get_shooting_speed():
            player_bullet_group.add(player.fire_bullet())
            player_shoot_timer = 0

        
        # Draw everything        

        player_bullet_group.draw(screen)
        player_group.draw(screen)
        alien_group.draw(screen)
        explosions_group.draw(screen)

        # Check for victory. SHOULD THIS BE SOMEWHERE ELSE? 
        if len(alien_group.sprites()) == 0 and current_level == "level_3":
            you_win = pygame.font.Font("PublicPixel.ttf", size=200).render("YOU WIN", False, (0, 0, 0), (255, 255, 255))
            screen.blit(you_win, (screen_width / 2 - you_win.get_width() / 2, screen_height / 2 - you_win.get_height() / 2), )
        elif len(alien_group.sprites()) == 0:
            new_level = True
            level_tracker += 1
            current_level = level_nums[level_tracker]

        level_indicator = pygame.font.Font("PublicPixel.ttf", size=40).render(current_level.upper(), False, (0, 0, 0), (255, 255, 255))
        screen.blit(level_indicator, (level_indicator.get_width() / 4, level_indicator.get_height() / 2), )
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player_shoot_timer += dt

run_game()