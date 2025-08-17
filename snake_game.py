
import pygame
import turtle
import random

# Welcome Screen

pygame.init()
screen_width =600
screen_height = 600
game_display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

white = (0,0,0)
black = (100,100,100)
font = pygame.font.SysFont("Times New Roman",50)
def message_to_screen(msg, color, y_displace=0):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2 + y_displace))
    game_display.blit(text, text_rect)

def welcome_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Press space to start
                    intro = False

        game_display.fill(white) # Fill the background
        message_to_screen("Welcome to Snake Game!",  black, -50)

        message_to_screen("Press SPACE to Play", black, 50)
        pygame.display.update()    

welcome_screen()
     




#main game code

delay = 100
Score=0
High_Score=0
game_over_flag = False  
# track game whether its over or not false means not over and true means over 



# window 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction ="stop"

#food
f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("red")
f.penup()
f.goto(0,100)

segments = []

# Pen for score
p = turtle.Turtle()
p.speed(0)
p.shape("circle")
p.color("grey")
p.penup()
p.hideturtle()
p.goto(0, 260)
p.write("Score: 0  High Score: 0", align="center", font=("san sarif", 24, "normal"))

# Pen for Game Over
go = turtle.Turtle()
go.speed(0)
go.color("red")
go.penup()
go.hideturtle()
go.goto(0, 0)


def go_up():
    if head.direction !="down":
        head.direction ="up"

def go_down():
    if head.direction !="up":
        head.direction ="down"        

def go_left():
    if head.direction !="right":
        head.direction ="left" 

def go_right():
    if head.direction!="left":
        head.direction ="right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)

# restart game        
def restart():
    global Score, High_Score, delay, game_over_flag

    go.clear() 
    head.goto(0,0)
    head.direction ="stop"
    f.goto(0,100)
    f.direction ="stop"
    Score=0
    delay=100

# removal of old segment from screen 
    for segment in segments:
        segment.hideturtle()
    segments.clear()
    
    game_over_flag = False

    p.clear()
    p.write("Score:{}  High Score: {}".format(Score, High_Score), align="center", font=("san serif",24," normal"))
    game_loop()


# keybord binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# navigation key control
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(restart, "space") # press Space to restart


# Game loop funstion (runs every delay ms)
def game_loop():
    global Score, High_Score, delay , game_over_flag
    if game_over_flag:
        return # when the game is over it will stop updating 
    wn.update()

    # border collision to Game over 
    if head.xcor() >300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        go.write("GAME OVER \n Press SPACE to restart", align="center", font=("san serif",28,"bold"))
        game_over_flag= True

    # collision with food    
    if head.distance(f)< 20:
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        f.goto(x,y) 

        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("yellow")
        new_seg.penup()
        segments.append(new_seg)

        delay = 100 

        Score += 10 
        if Score > High_Score:
            High_Score = Score

        p.clear()
        p.write("Score {}  High Score {}".format(Score,High_Score), align="center",  font=("san serif", 24 , "normal"))
        
    # to move the body 
    for index in range(len(segments) - 1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y) 

    if len(segments)> 0: 
        x=head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)
    move()
    
    # check collision with body 
    for segment in segments:
        if segment.distance(head)<20:
            go.write("GAME OVER \n Press SPACE to restart", align="center", font=("san serif",28,"bold"))
            game_over_flag= True
            return
    wn.ontimer(game_loop, delay)    
game_loop()
wn.mainloop()    








           
