from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SPLIT_SPEED, COLOR_WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius, color=COLOR_WHITE)
        self.split_speed = SPLIT_SPEED
        self.move_boundaries = False

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)
        if not self.move_boundaries and self.position.x > 0 and self.position.x < SCREEN_WIDTH and self.position.y > 0 and self.position.y < SCREEN_HEIGHT:
            self.move_boundaries = True
        
    def move_to_other_side_if_out_of_bounds(self) -> None:
        if not self.move_boundaries:
            return
        if (self.position.x + self.radius) < 0:
            self.position.x += SCREEN_WIDTH + 2*self.radius
        elif (self.position.x - self.radius) > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH + 2*self.radius
        if (self.position.y + self.radius) < 0:
            self.position.y += SCREEN_HEIGHT + 2*self.radius
        elif (self.position.y - self.radius) > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT + 2*self.radius

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.move_to_other_side_if_out_of_bounds()
        
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
        a1.velocity=vel1*self.split_speed
        a2=Asteroid(self.position.x, self.position.y, radius)
        a2.velocity=vel2*self.split_speed