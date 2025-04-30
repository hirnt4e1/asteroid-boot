import pygame
import circleshape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_fragment = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        second_fragment = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        first_fragment.velocity = self.velocity.rotate(random_angle) * 1.2
        second_fragment.velocity = self.velocity.rotate(-random_angle) * 1.2

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)