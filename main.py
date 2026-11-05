import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from gamestate import GameState
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gameworld import GameWorld
import sys

def handle_events_by_state(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if game_state == GameState.INTRO:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while pygame.key.get_pressed()[pygame.K_SPACE]:
                    for release_event in pygame.event.get():
                        if release_event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                    pygame.time.Clock().tick(60)
                return GameState.START
        if game_state == GameState.GAME_OVER:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                while pygame.key.get_pressed()[pygame.K_r]:
                    for release_event in pygame.event.get():
                        if release_event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                    pygame.time.Clock().tick(60)
                return GameState.START
    return game_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock=pygame.time.Clock()
    dt=0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_world = GameWorld(screen)
    game_world.create_world(withPlayer=False)
    game_state = GameState.INTRO
    counter = 0
    score_font = pygame.font.Font(None, 40)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        dt=clock.tick(60)/1000.0
        game_world.update(dt)
        game_world.draw() 
        
        game_state = handle_events_by_state(game_state)
        
        if game_state == GameState.PLAYING:
            game_world.shot()
            game_state = game_world.collision_check()

        if game_state == GameState.INTRO:
            title_font = pygame.font.Font(None, 96)
            prompt_font = pygame.font.Font(None, 48)
            title_text = title_font.render("Asteroids", True, "yellow")
            prompt_text = prompt_font.render("Press SPACE to start", True, "white")
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60))
            prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20))
            screen.blit(title_text, title_rect)
            if counter < 20:
                screen.blit(prompt_text, prompt_rect)
            counter +=1
            counter = counter % 30

        if game_state == GameState.START:
            game_world.dispose_world()
            game_world.create_world(withPlayer=True)
            game_state = GameState.PLAYING
            
        if game_state == GameState.GAME_OVER:
            title_font = pygame.font.Font(None, 96)
            prompt_font = pygame.font.Font(None, 48)
            title_text = title_font.render("Game Over", True, "red")
            prompt_text = prompt_font.render("Press R to restart or Q to quit", True, "white")
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60))
            prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20))
            screen.blit(title_text, title_rect)
            screen.blit(prompt_text, prompt_rect)

        if game_world.get_score() > 0:
            score_text = score_font.render(f"{game_world.get_score()}", True, "white")
            score_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 20, 20))
            screen.blit(score_text, score_rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
