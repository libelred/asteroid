from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        rndm=random.uniform(20,50)
        vel1=self.velocity.rotate(rndm)
        vel2=self.velocity.rotate(-rndm)
        radius=self.radius - ASTEROID_MIN_RADIUS
        a1=Asteroid(self.position.x, self.position.y, radius)
        a1.velocity=vel1*1.5
        a2=Asteroid(self.position.x, self.position.y, radius)
        a2.velocity=vel2*1.5