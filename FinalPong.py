import pygame, random, time

#Pygame basics
pygame.init()
screen_width = 1280
screen_height = 720
pygame.display.set_caption("Pong")

#Main Variables
WHITE = (255,255,255)
clock = pygame.time.Clock()
window = pygame.display.set_mode((screen_width, screen_height))


#MUSIC
start_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\pongStart.mp3')
start_sound.set_volume(0.2)

megalovania = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\Megalovania.mp3')
megalovania.set_volume(0.2)

nyeh_heh = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\Anyeh.mp3')
nyeh_heh.set_volume(0.2)

theme_song = [megalovania, nyeh_heh]

#SOUND
hit_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\stephenHitSound.mp3')
hit_sound.set_volume(0.1)

wasted_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\wasted.mp3')
wasted_sound.set_volume(0.2)

menu_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\shopSoundtrack.mp3')
menu_sound.set_volume(0.05)

missed_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\stephenVoice.mp3')
missed_sound.set_volume(0.3)

wasted_img = pygame.image.load('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\wasted.png')
wasted_img = pygame.transform.scale(wasted_img, (300,300))

win_sound = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\playerWinSound.mp3')
win_sound.set_volume(0.2)

button_press = pygame.mixer.Sound('d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\ButtonPress.mp3')
button_press.set_volume(0.3)

#Paddle Variables
paddle_velocity = 8
paddle_width = 20
paddle_height = 0
#original 180

#PongBall Varables
ball_size = 12

#MAKE SURE TO ALWAYS CHANGE THIS DEPENDING ON THE SYSTEM
pong_ball = pygame.image.load("d:\Desktop\pythontrash\Pygame\PONG\Pong4.0\Pong_model\PongBall.png")
pong_ball = pygame.transform.scale(pong_ball, (ball_size, ball_size))

#Pong ball speeds
ball_vel = 5
ball_vel = [-ball_vel, ball_vel]
ball_x_vel = random.choice(ball_vel)
ball_y_vel = random.choice(ball_vel)
#put in decimals of (1 + percentage)
speed_multiplier = 1.07

#Sprites
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([paddle_width, paddle_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def moveUp(self):
        if self.rect.y >= 0:
            self.rect.y -= paddle_velocity

    def moveDown(self):
        if self.rect.y <= (screen_height - paddle_height):
            self.rect.y += paddle_velocity

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pong_ball
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def ballMove(self):
        self.rect.y += ball_y_vel
        self.rect.x += ball_x_vel
    
    def Reset(self, x, y):
        self.rect.center = [x,y]

#Ball added to sprite group
ball = Ball(screen_width/2, screen_height/2)
paddle_group = pygame.sprite.Group(ball)
#Paddle added to sprite group
player_1 = ()
player_2 = ()
paddle_group.add(player_1,player_2)


#Player Controls
def playerPaddle():
    #Player1(left)
    if key[pygame.K_w]:
        player_1.moveUp()
    if key[pygame.K_s]:
        player_1.moveDown()


    #Player2(right)
    if key[pygame.K_i]:
        player_2.moveUp()
    if key[pygame.K_k]:
        player_2.moveDown()

    paddle_group.draw(window)

#Buttons
click = pygame.MOUSEBUTTONDOWN
class Button():
    def __init__(self, y, text = ''):
        self.color = (0)
        self.width = 400
        self.height = 80
        self.x = screen_width/2
        self.y = y
        self.text = text
    
    def draw(self, centertext):
        #outline
        pygame.draw.rect(window, WHITE, (self.x - self.width/2 - 4, self.y - self.height/2 - 4, self.width + 8, self.height + 8), 0)

        #button
        pygame.draw.rect(window, self.color, (self.x - self.width/2, self.y - self.height/2, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('Corbel',70)
            word = font.render(self.text, 0 , WHITE)
            window.blit(word, (self.x - centertext, self.y - self.height/2 + 5))

    #mouse interaction with button
    def isOver(self, mouse_position):
        if ((mouse_position[0] >= (self.x - self.width/2)) and (mouse_position[0] <= (self.x + self.width/2))) and ((mouse_position[1] >= (self.y - self.height/2)) and (mouse_position[1] <= (self.y + self.height/2))):
                self.color = (100,100,100)         
                return True
        else: 
            self.color = (0)

#Font Types
font = pygame.font.SysFont('Corbel',180)
font_small = pygame.font.SysFont('Corbel',100)
font_big = pygame.font.SysFont('Corbel',250)

#Menu Screen
start_button = Button(screen_height - 250, 'Start')
option_button = Button(screen_height - 150, 'Options')
exit_button = Button(screen_height - 50, 'Exit')

def menuScreen():    
    title = font.render("Pong.", 0 , WHITE)

    
    window.blit(title, (screen_width/2 - 200, 100))
    start_button.draw(70)
    option_button.draw(105)
    exit_button.draw(55)

#Option screen
easy_diff = Button(screen_height - 350, 'Easy')
normal_diff = Button(screen_height - 250, 'Normal')
hard_diff = Button(screen_height - 150, 'Hard')
back_button = Button(screen_height - 50, 'Back')

def optionScreen():
    title = font.render("Options.", 0 , WHITE)


    window.blit(title, (screen_width/2 - 300, 50))
    window.blit(font_small.render("Difficulty.", 0 , WHITE), (screen_width/2 - 175, 230))
    easy_diff.draw(70)
    normal_diff.draw(100)
    hard_diff.draw(70)
    back_button.draw(70)
    
#Pause Screen
resume_button = Button(screen_height - 350, 'Resume')
menu_button = Button(screen_height - 250, 'Main Menu')
def pauseScreen():
    title = font.render("Pause.", 0 , WHITE)

    window.blit(font_small.render("Oi, why'd ya stop?", 0 , WHITE), (screen_width/2 - 350, 100))
    resume_button.draw(110)
    menu_button.draw(150)
    exit_button.draw(55)


left_point = 0
right_point = 0

def drawScore(x, point):
        player_score = font_big.render(str(point), 0 , (100, 100, 100))
        window.blit(player_score, (x,screen_height/3))

def checkWinner(totalScore, LeftOrRight = ''):
    LeftOrRight = font_big.render(LeftOrRight ,'wins!', 0 , WHITE)
    if totalScore == 3:
        ball.Reset(screen_width/2, screen_height/2)
        game_song.stop()    #stops song
        win_sound.play()    #winning sound effect
    else:
        ball.Reset(screen_width/2, screen_height/2)
        game_song.stop()    #stops song
        wasted_sound.play() #winning sound effect

#Main running loop
main_menu = True
option_menu = False
game_start = False
pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    window.fill(0)
    #Menu screen
    if main_menu == True:
        menuScreen()
        menu_sound.play()
        if exit_button.isOver(mouse_pos):   #exit button
                exit_button.draw(55)
                if event.type == click:
                    button_press.play()
                    pygame.time.delay(150)
                    pygame.quit()

        if start_button.isOver(mouse_pos): #start game button
            start_button.draw(70)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                if paddle_height != 0:  #if paddle height has been determined by selected difficulty
                    menu_sound.stop()
                    main_menu = False
                else:
                    paddle_height = 180 #if paddle heigh has not been determinded by selected difficulty (Player pressed start w/o pressing options)
                    player_1 = Paddle(20, screen_height/2)
                    player_2 = Paddle(screen_width - 20, screen_height/2)
                    paddle_group.add(player_1,player_2)

                
    
        if option_button.isOver(mouse_pos): #option button 
            option_button.draw(105)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                main_menu = False
                option_menu = True

    #Option Screen                        
    elif option_menu == True:
        optionScreen()
        if easy_diff.isOver(mouse_pos):
            easy_diff.draw(70)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                paddle_group.remove(player_1, player_2)
                paddle_height = 270                
                player_1 = Paddle(20, screen_height/2)
                player_2 = Paddle(screen_width - 20, screen_height/2)
                paddle_group.add(player_1,player_2)


        if normal_diff.isOver(mouse_pos):
            normal_diff.draw(100)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                paddle_group.remove(player_1,player_2)
                paddle_height = 200
                player_1 = Paddle(20, screen_height/2)
                player_2 = Paddle(screen_width - 20, screen_height/2)
                paddle_group.add(player_1,player_2)



        
        if hard_diff.isOver(mouse_pos):
            hard_diff.draw(70)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                paddle_group.remove(player_1,player_2)
                paddle_height = 80
                player_1 = Paddle(20, screen_height/2)
                player_2 = Paddle(screen_width - 20, screen_height/2)
                paddle_group.add(player_1,player_2)

        


        if back_button.isOver(mouse_pos):
            back_button.draw(70)
            if event.type == click:
                button_press.play()
                pygame.time.delay(150)
                option_menu = False
                pygame.time.delay(150)
                main_menu = True

        #THE ACTUAL GAME
    else:
        drawScore(100, left_point)
        drawScore(screen_width-200, right_point)
         #Update player paddle position
        playerPaddle()
        #Game Starts
        if key[pygame.K_SPACE]:
            game_song = random.choice(theme_song)
            start_sound.play()
            pygame.time.delay(3500)
            game_song.play()
            game_start = True

        if game_start == True: 
            ball.ballMove()
            #Ball hits a paddle
            if pygame.sprite.collide_rect(player_1, ball) or pygame.sprite.collide_rect(player_2, ball):
                hit_sound.play()
                ball_x_vel *= -speed_multiplier
            
            #Ball hits top/bottom wall
            if (ball.rect.y >= screen_height) or (ball.rect.y <= 0):
                ball_y_vel *= -1

            #Player loses
            if (ball.rect.x > screen_width + 20):
                left_point += 1
                missed_sound.play()
                ball_x_vel = random.choice(ball_vel)    #Reset velocities
                game_start = False
                checkWinner(left_point, 'Left')
            if (ball.rect.x < -20):   #Right gets a score
                right_point += 1
                missed_sound.play()
                ball_x_vel = random.choice(ball_vel)    #Reset velocities
                game_start = False
                checkWinner(right_point, 'Right')
            if (left_point == 3) or (right_point == 3):
                left_point = 0
                right_point = 0

        #PAUSING :)
        if key[pygame.K_ESCAPE]:
            game_start = False
            pause = True
        if pause == True:
            pygame.mixer.pause()
            pauseScreen()
            if resume_button.isOver(mouse_pos):
                resume_button.draw(110)
                if event.type == click:
                    button_press.play()
                    pygame.time.delay(150)
                    start_sound.play()
                    pygame.time.delay(3500)
                    pygame.mixer.unpause()
                    pause = False
                    game_start = True

            if menu_button.isOver(mouse_pos): #goes back to main menu
                menu_button.draw(150)
                if event.type == click:
                    button_press.play()
                    pygame.time.delay(150)
                    left_point = 0
                    right_point = 0
                    pause = False
                    main_menu = True
            
            if exit_button.isOver(mouse_pos):
                exit_button.draw(55)
                if event.type == click:
                    pygame.time.delay(150)
                    button_press.play()
                    pygame.quit()

    pygame.display.flip()
    clock.tick(120)
    

pygame.quit()