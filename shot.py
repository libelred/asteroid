from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame
from constants import LINE_WIDTH, SHOOT_TIME_TO_LIVE
from colors import COLOR_YELLOW
class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS, color=COLOR_YELLOW)
        self.time_to_live = SHOOT_TIME_TO_LIVE

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.move_to_other_side_if_out_of_bounds()
        self.time_to_live -= dt
        if self.time_to_live <= 0:
            self.kill()