import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
run = True
game_run = True
globals_statue = "YOU WIN"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Dash")
icon = pygame.image.load("data/player/player.png")
pygame.display.set_icon(icon)

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, skin, size, speed):
        super().__init__()
        self.image = pygame.image.load(skin).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.base_pos = self.rect
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.time = 0

    def reset(self):
        self.rect = self.base_pos

    def move(self, dt):
        self.time = dt * self.speed
        self.rect.x -= self.time

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, dt):
        self.draw()
        self.move(dt)

block_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

class Map():
    def __init__(self, speed):
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 3, 4, 1, 4, 3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 5],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.size = SCREEN_HEIGHT // len(self.map)

        self.dale = pygame.image.load("data/map/dale_high.png").convert_alpha()
        self.dale = pygame.transform.scale(self.dale, (self.size, self.size))

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 1:
                    block = Block(self.size * x, self.size * y, "data/map/block.png", self.size, speed)
                    block_group.add(block)
                elif self.map[y][x] == 2:
                    dale_h = Block(self.size * x, self.size * y, "data/map/dale_high.png", self.size, speed)
                    block_group.add(dale_h)
                elif self.map[y][x] == 3:
                    spike = Block(self.size * x, self.size * y, "data/map/spike.png", self.size, speed)
                    spike_group.add(spike)
                elif self.map[y][x] == 4:
                    spike_low = Block(self.size * x, self.size * y, "data/map/spike _low.png", self.size, speed)
                    spike_group.add(spike_low)
                elif self.map[y][x] == 5:
                    door = Block(self.size * x, self.size * y, "data/map/end_door.png", self.size, speed)
                    door_group.add(door)


    def draw(self):
        screen.fill("#555599")
    def update(self):
        self.draw()

map_use = Map(1000)

class Player():
    def __init__(self):
        self.size = map_use.size
        self.player = pygame.image.load("data/player/player.png").convert_alpha()
        self.player = pygame.transform.scale(self.player, (self.size, self.size))
        self.rect = self.player.get_rect(center=(self.size * 3, 0))
        self.base_pos = self.rect
        self.mask = pygame.mask.from_surface(self.player)

        self.gravity = 5
        self.velocity_y = 0
        self.can_jump = False

    def reset(self):
        self.rect = self.player.get_rect(center=(self.size * 3, 0))
        self.velocity_y = 0

    def move(self):
        key = pygame.key.get_pressed()
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        colide_block = False

        for block in block_group:
            if self.rect.colliderect(block.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = block.rect.top
                    self.velocity_y = 0
                    self.can_jump = True
                    colide_block = True
                elif self.velocity_y < 0:
                    self.rect.top = block.rect.bottom
                    self.velocity_y = 0

            if colide_block == False:
                self.can_jump = False

        if key[pygame.K_SPACE] and self.can_jump or pygame.mouse.get_pressed()[0] and self.can_jump:
            self.velocity_y -= 40
            self.can_jump = False

    def death(self):
        global game_run
        global globals_statue
        if pygame.sprite.spritecollide(player, spike_group, False, pygame.sprite.collide_mask):
            game_run = False
            globals_statue = "YOU LOSE"

        if self.rect.top > SCREEN_HEIGHT:
            game_run = False
            globals_statue = "YOU LOSE"

        for block in block_group:
            if self.rect.colliderect(block.rect):
                if self.rect.x < block.rect.x:
                    game_run = False
                    globals_statue = "YOU LOSE"

                if self.rect.y < block.rect.y:
                    game_run = False
                    globals_statue = "YOU LOSE"

        for door in door_group:
            if self.rect.colliderect(door.rect):
                    game_run = False
                    globals_statue = " YOU WIN"

    def draw(self):
        screen.blit(self.player, (self.rect.x, self.rect.y))

    def update(self):
        self.death()
        self.move()
        self.draw()

player = Player()

class Game():
    def __init__(self):
        self.game_run = True
        self.police = pygame.font.SysFont(None, 50)
        self.try_again_pos = pygame.Rect(0, 0, 200, 50)
        self.try_again_pos.centerx = SCREEN_WIDTH * 1 // 4
        self.try_again_pos.centery = SCREEN_HEIGHT * 1 // 2

        self.exit_pos = pygame.Rect(0, 0, 200, 50)
        self.exit_pos.centerx = SCREEN_WIDTH * 3 // 4
        self.exit_pos.centery = SCREEN_HEIGHT * 1 // 2

        self.game_statue_pos = pygame.Rect(0, 0, 200, 50)
        self.game_statue_pos.centerx = SCREEN_WIDTH * 1 // 2
        self.game_statue_pos.centery = SCREEN_HEIGHT * 1 // 4

        self.police_credit = pygame.font.SysFont(None, 40)
        self.game_credit = pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.reset_game_or_not = False

    def reset_game(self):
        if self.reset_game_or_not == True:
            self.reset_game_or_not = False
            return True

    def death_screen(self, game_statue):
        mouse = pygame.mouse.get_pos()
        if self.try_again_pos.collidepoint(mouse):
            pygame.draw.rect(screen, (0, 0, 0), self.try_again_pos, 30)
            if pygame.mouse.get_pressed()[0]:
                self.reset_game_or_not = True

        pygame.draw.rect(screen, (200, 200, 200), self.try_again_pos, 3)
        try_again_text = self.police.render("Try Again ?", True, (200, 200, 200))
        screen.blit(try_again_text, (self.try_again_pos.x + 10, self.try_again_pos.y + 10))

        pygame.draw.rect(screen, (200, 200, 200), self.game_statue_pos, 3)
        try_again_text = self.police.render(game_statue, True, (200, 200, 200))
        screen.blit(try_again_text, (self.game_statue_pos.x + 10, self.game_statue_pos.y + 10))

        if self.exit_pos.collidepoint(mouse):
            pygame.draw.rect(screen, (0, 0, 0), self.exit_pos, 30)
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (200, 200, 200), self.exit_pos, 3)
        try_again_text = self.police.render("Exit ?", True, (200, 200, 200))
        screen.blit(try_again_text, (self.exit_pos.x + 10, self.exit_pos.y + 10))

        pygame.draw.rect(screen, (0, 0, 0), self.game_credit)
        game_credit_text_1 = self.police_credit.render("Made by : Zraky", True, (200, 200, 200))
        game_credit_text_2 = self.police_credit.render("code : Zraky   map : Zraky", True, (200, 200, 200))

        screen.blit(game_credit_text_1, (self.game_credit.x + 30, self.game_credit.y  + 20))
        screen.blit(game_credit_text_2, (self.game_credit.x + 30, self.game_credit.y + 60))


game = Game()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        run = False

    if game.reset_game() or pygame.key.get_pressed()[pygame.K_r]:
        for b in block_group:
            b.kill()
        for s in spike_group:
            s.kill()
        for d in door_group:
            d.kill()
        player.reset()
        map_use = Map(1000)
        game_run = True

    if game_run == False:
        map_use.draw()
        block_group.draw(screen)
        spike_group.draw(screen)
        door_group.draw(screen)
        game.death_screen(globals_statue)
        pygame.mouse.set_visible(1)

    else:
        pygame.mouse.set_visible(0)
        dt = clock.tick(60) / 1000

        map_use.update()
        block_group.update(dt)
        spike_group.update(dt)
        door_group.update(dt)
        player.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()