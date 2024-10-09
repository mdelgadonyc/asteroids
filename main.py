import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatable, drawable
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.detection(player):
                print("Game Over!")
                pygame.quit()
                return
            for shot in shots:
                if shot.detection(asteroid):
                    shot.kill()
                    asteroid.split()
                    break
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
