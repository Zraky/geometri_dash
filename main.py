import pygame, sys, random, math

pygame.init()

SCREEN_WIDTH  = 1600
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


FPS = 0
NB_FISHS = 100
SPEED = 200
REFRESH = 0

#by nb
NB_CLOSER_FISHES = 10

#by distance
REPOLSION = 0
FIRST_ROW = 100
SECOND_ROW = 150
THIRD_ROW = 200


def draw_circle(fish):
        pygame.draw.circle(screen, (55, 255, 55), fish.center.get_pos(), FIRST_ROW, 5)
        pygame.draw.circle(screen, (55, 55, 255), fish.center.get_pos(), SECOND_ROW, 5)
        pygame.draw.circle(screen, (255, 55, 55), fish.center.get_pos(), THIRD_ROW, 5)

def draw_line(fishs, name=None, level=0):
    if (name == None):
        for i, fish in enumerate(fishs):
            for j in range(len(fish.close_fish)):
                pygame.draw.line(screen, (255, 0, 0), fish.center.get_pos(), fish.close_fish[j].center.get_pos(), 2)

    else:
        for i in range(len(fishs)):
            if (name == fishs[i].name):
                for j in range(len(fishs[i].close_fish)):
                    pygame.draw.line(screen, (0, 0, 255), fishs[i].center.get_pos(), fishs[i].close_fish[j].center.get_pos(), 2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, vector, speed, dt):
        self.x += vector.x * speed * dt
        self.y += vector.y * speed * dt

    def get_pos(self):
        return self.x, self.y

    def draw(self):
        pygame.draw.circle(screen, (155, 155, 255), (int(self.x), int(self.y)), 3)


class Fish:
    def __init__(self, name, x, y, refresh=(0, 0), speed=None):
        self.name = name
        self.center = Point(x, y)
        self.vector = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if self.vector.length() > 0:
            self.vector = self.vector.normalize()
        self.refresh_time, self.refresh_wait = refresh
        self.speed = speed if speed else random.randint(SPEED // 2, SPEED)
        self.bank_move = pygame.math.Vector2(0, 0)

        self.close_fish = []

    def closerFish(self, fishList):
        self.bank_move = pygame.math.Vector2(0, 0)

        fishList = sorted(fishList, key=lambda f: math.hypot(self.center.x - f.center.x, self.center.y - f.center.y))
        self.close_fish.clear()
        for fish in fishList[1:NB_CLOSER_FISHES]:
            self.bank_move += fish.vector
            self.close_fish.append(fish)


        if self.bank_move.length() > 0:
            bank_move = self.bank_move.normalize() * 0.1
            self.vector += bank_move

        if self.vector.length() > 0:
            self.vector = self.vector.normalize()


    def bounce(self):
        if self.center.x <= 0:
            self.center.x = 0
            self.vector = pygame.math.Vector2(- self.vector.x, self.vector.y)

        elif self.center.x >= SCREEN_WIDTH:
            self.center.x = SCREEN_WIDTH
            self.vector = pygame.math.Vector2(- self.vector.x, self.vector.y)

        if self.center.y <= 0:
            self.center.y = 0
            self.vector = pygame.math.Vector2(self.vector.x, - self.vector.y)

        if self.center.y >= SCREEN_HEIGHT:
            self.center.y = SCREEN_HEIGHT
            self.vector = pygame.math.Vector2(self.vector.x, - self.vector.y)

    def move(self, dt):
        self.center.move(self.vector, self.speed, dt)

    def draw(self):
        self.center.draw()

    def refesh(self, fishs):
        if (self.refresh_time == self.refresh_wait):
            self.closerFish(fishs)
            self.refresh_wait = 0
        else:
            self.refresh_wait += 1

    def update(self, fishs, dt):
        self.refesh(fishs)
        self.bounce()
        self.move(dt)
        self.draw()


class Fishier(Fish):
    def __init__(self, name, x, y, refresh=(0, 0), speed=None):
        Fish.__init__(self, name, x, y, refresh, speed)

    def closerFish(self, fishList):
        self.bank_move = pygame.math.Vector2(0, 0)

        FIRST_ROW = 100
        SECOND_ROW = 50
        THIRD_ROW = 20

        for fish in fishList[1:len(fishList)]:
            dist = ((abs(fish.center.x) + abs(fish.center.y)) - (abs(self.center.x) + abs(self.center.y)))
            if (dist < THIRD_ROW):
                if (dist < SECOND_ROW):
                    if (dist < FIRST_ROW):
                        if (dist < REPOLSION):
                            self.bank_move += fish.vector * -10
                        else:
                            self.bank_move += fish.vector * 4
                    else:
                        self.bank_move += fish.vector * 2
                else:
                    self.bank_move += fish.vector

        if self.bank_move.length() > 0:
            bank_move = self.bank_move.normalize() * 0.1
            self.vector += bank_move

        if self.vector.length() > 0:
            self.vector = self.vector.normalize()


fishs = []

for i in range(1, NB_FISHS + 1):
    fishs.append(Fishier(i, random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), (REFRESH, (REFRESH % i))))


police = pygame.font.SysFont(None, 40)

while True:
    dt = clock.tick(FPS) / 1000
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    for i, fish in enumerate(fishs):
        fish.update(fishs, dt)
        draw_circle(fish)

    #draw_line(fishs)
    #draw_line(fishs, 1)
    game_credit_text_1 = police.render("FPS : " + str(clock.get_fps()), True, (200, 200, 200))
    screen.blit(game_credit_text_1, (0, 0))

    pygame.display.flip()
