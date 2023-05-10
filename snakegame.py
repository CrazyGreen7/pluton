import pygame
import time
import random
from pygame.locals import *
import sys
import numpy as np

def playsnakegame():
   # importing libraries


    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snakegame')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):

        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)
        
        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)
        
        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()
        
        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():

        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)
        
        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        
        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (window_x/2, window_y/4)
        
        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the program
        time.sleep(2)
        
        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()


    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)

def playpingpong():
        

    pygame.init()

    # Font that is used to render the text
    font20 = pygame.font.Font('freesansbold.ttf', 20)

    # RGB values of standard colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Basic parameters of the screen
    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()	
    FPS = 30

    # Striker class


    class Striker:
            # Take the initial position, dimensions, speed and color of the object
        def __init__(self, posx, posy, width, height, speed, color):
            self.posx = posx
            self.posy = posy
            self.width = width
            self.height = height
            self.speed = speed
            self.color = color
            # Rect that is used to control the position and collision of the object
            self.geekRect = pygame.Rect(posx, posy, width, height)
            # Object that is blit on the screen
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

        # Used to display the object on the screen
        def display(self):
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

        def update(self, yFac):
            self.posy = self.posy + self.speed*yFac

            # Restricting the striker to be below the top surface of the screen
            if self.posy <= 0:
                self.posy = 0
            # Restricting the striker to be above the bottom surface of the screen
            elif self.posy + self.height >= HEIGHT:
                self.posy = HEIGHT-self.height

            # Updating the rect with the new values
            self.geekRect = (self.posx, self.posy, self.width, self.height)

        def displayScore(self, text, score, x, y, color):
            text = font20.render(text+str(score), True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)

            screen.blit(text, textRect)

        def getRect(self):
            return self.geekRect

    # Ball class


    class Ball:
        def __init__(self, posx, posy, radius, speed, color):
            self.posx = posx
            self.posy = posy
            self.radius = radius
            self.speed = speed
            self.color = color
            self.xFac = 1
            self.yFac = -1
            self.ball = pygame.draw.circle(
                screen, self.color, (self.posx, self.posy), self.radius)
            self.firstTime = 1

        def display(self):
            self.ball = pygame.draw.circle(
                screen, self.color, (self.posx, self.posy), self.radius)

        def update(self):
            self.posx += self.speed*self.xFac
            self.posy += self.speed*self.yFac

            # If the ball hits the top or bottom surfaces,
            # then the sign of yFac is changed and
            # it results in a reflection
            if self.posy <= 0 or self.posy >= HEIGHT:
                self.yFac *= -1

            if self.posx <= 0 and self.firstTime:
                self.firstTime = 0
                return 1
            elif self.posx >= WIDTH and self.firstTime:
                self.firstTime = 0
                return -1
            else:
                return 0

        def reset(self):
            self.posx = WIDTH//2
            self.posy = HEIGHT//2
            self.xFac *= -1
            self.firstTime = 1

        # Used to reflect the ball along the X-axis
        def hit(self):
            self.xFac *= -1

        def getRect(self):
            return self.ball

    # Game Manager


    def main():
        running = True

        # Defining the objects
        geek1 = Striker(20, 0, 10, 100, 10, GREEN)
        geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN)
        ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

        listOfGeeks = [geek1, geek2]

        # Initial parameters of the players
        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0

        while running:
            screen.fill(BLACK)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0

            # Collision detection
            for geek in listOfGeeks:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                    ball.hit()

            # Updating the objects
            geek1.update(geek1YFac)
            geek2.update(geek2YFac)
            point = ball.update()

            # -1 -> Geek_1 has scored
            # +1 -> Geek_2 has scored
            # 0 -> None of them scored
            if point == -1:
                geek1Score += 1
            elif point == 1:
                geek2Score += 1

            # Someone has scored
            # a point and the ball is out of bounds.
            # So, we reset it's position
            if point:
                ball.reset()

            # Displaying the objects on the screen
            geek1.display()
            geek2.display()
            ball.display()

            # Displaying the scores of the players
            geek1.displayScore("Geek_1 : ",
                            geek1Score, 100, 20, WHITE)
            geek2.displayScore("Geek_2 : ",
                            geek2Score, WIDTH-100, 20, WHITE)

            pygame.display.update()
            clock.tick(FPS)	


    if __name__ == "__main__":
        main()
        pygame.quit()

