import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE
from math import sqrt


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float, color: tuple[int, int, int] = COLOR_WHITE) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.default_color = color
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass
    
    def collides_with(self, other: "CircleShape") -> bool:
        return pygame.Vector2.distance_to(self.position, other.position) < (self.radius + other.radius)*0.85
    
    def move_to_other_side_if_out_of_bounds(self) -> None:
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
