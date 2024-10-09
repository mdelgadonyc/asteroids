from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_INCREASE_RATE
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(angle)
        new_velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * ASTEROID_INCREASE_RATE
        new_asteroid2.velocity = new_velocity2 * ASTEROID_INCREASE_RATE
        self.kill()


    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt