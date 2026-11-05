from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event
import pygame

from gamestate import GameState

class GameWorld:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.updatable : pygame.sprite.Group | None = None
        self.drawable : pygame.sprite.Group | None = None
        self.asteroids : pygame.sprite.Group | None = None
        self.shots : pygame.sprite.Group | None = None
        self.player : Player | None = None
        self.asteroidField : AsteroidField | None = None
        self.score : long = 0
    
    def create_world(self, withPlayer: bool) -> None:
        self.score = 0
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        self.asteroidField  = AsteroidField()

        if withPlayer:
            self.shots = pygame.sprite.Group()
            Shot.containers = (self.shots, self.updatable, self.drawable)
            Player.containers = (self.updatable, self.drawable)
            self.player = Player(self.width // 2, self.height // 2)
            self.updatable.add(self.player)
            self.drawable.add(self.player)
            
    def dispose_world(self) -> None:
        if self.player is not None:
            self.player.kill()
            self.player = None
        if self.asteroidField is not None:
            self.asteroidField.kill()
            self.asteroidField = None
        if self.shots is not None:
            self.shots.empty()
            self.shots = None
        if self.asteroids is not None:
            self.asteroids.empty()
            self.asteroids = None
        if self.drawable is not None:
            self.drawable.empty()
            self.drawable = None
        if self.updatable is not None:
            self.updatable.empty()
            self.updatable = None
        if self.drawable is not None:
            self.drawable.empty()
            self.drawable = None
            
    def update(self, dt: float) -> None:
        if self.updatable is not None:
            self.updatable.update(dt)
    def draw(self) -> None:
        if self.drawable is not None:
            for draw in self.drawable:
                draw.draw(self.screen)
                
    def get_score(self) -> int:
        return self.score
    
    def shot(self) -> None:
        if self.shots is not None and self.asteroids is not None:
            for shot in self.shots:
                for asteroid in self.asteroids:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        self.score += int(asteroid.get_score())
                        asteroid.split()
    
    def collision_check(self) -> GameState:
        if self.player is not None and self.asteroids is not None:
            for asteroid in self.asteroids:
                if self.player.collides_with(asteroid):
                    log_event("player_hit")
                    self.player.kill()
                    self.player = None
                    return GameState.GAME_OVER
        return GameState.PLAYING