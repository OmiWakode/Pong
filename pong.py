# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

score1 = 0
score2 = 0
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

hit_times = 0

ball_pos=[WIDTH//2,HEIGHT//2]
ball_vel = [0,0]

paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle_vel= 5

left_up = False
left_down = False
right_up = False
right_down = False

LEFT = False
RIGHT = True
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

# define event handlers 

    
    
def spawn_ball(direction):
    global ball_pos, ball_vel, time # these are vectors stored as lists
    ball_pos = [WIDTH//2, HEIGHT//2]
    x = random.randrange(120, 240)/60
    if direction==RIGHT:
        ball_vel[0] = x
    if direction==LEFT:
        ball_vel[0] = -1*x
    ball_vel[1] = -1* random.randrange(60, 180)/60



    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    score1 = 0
    score2 = 0
    
    ball_pos=[WIDTH//2,HEIGHT//2]
    ball_vel = [0,0]
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    
    left_up = False
    left_down = False
    right_up = False
    right_down = False
    hit_times = 0
    
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,hit_times
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    #for collision with horizontal walls
    if ball_pos[1]==BALL_RADIUS or ball_pos[1]==HEIGHT - BALL_RADIUS:
        ball_vel[1] = -1* ball_vel[1]
    
        
    #gutter collision
    if ball_pos[0]<=BALL_RADIUS + PAD_WIDTH:
       
        if abs(paddle1_pos - ball_pos[1]) < 48:
            if ball_vel[0]> 0:
                ball_vel[0] = -1 *(ball_vel[0] + 0.1*ball_vel[0])
            else:
                ball_vel[0] =  abs(ball_vel[0])+  0.1*abs(ball_vel[0])
            
        else:
            score2+=1
            spawn_ball(RIGHT)
            
    elif ball_pos[0]>=WIDTH-BALL_RADIUS - PAD_WIDTH:
        
        if abs(paddle2_pos - ball_pos[1]) <48:
            if ball_vel[0]> 0:
                ball_vel[0] = -1 *(ball_vel[0] + 0.1*ball_vel[0])
            else:
                ball_vel[0] =  abs(ball_vel[0]) +  0.1*abs(ball_vel[0])
        else:     
            score1+=1
            spawn_ball(LEFT)
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

        
    
       
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"white","white")
    
    
    # update paddle's vertical position, keep paddle on the screen
    
    if left_down:
        if paddle1_pos < HEIGHT - PAD_HEIGHT/2:
            paddle1_pos = paddle1_pos + paddle_vel
    if left_up:	
        if paddle1_pos > PAD_HEIGHT/2:
            paddle1_pos = paddle1_pos - paddle_vel
    
    if right_down:
        if paddle2_pos < HEIGHT - PAD_HEIGHT/2:
            paddle2_pos = paddle2_pos + paddle_vel
        
    if right_up:    	
        if paddle2_pos > PAD_HEIGHT/2:
            paddle2_pos = paddle2_pos - paddle_vel

            
        
    
    # draw paddles
    canvas.draw_line([0,paddle1_pos - PAD_HEIGHT/2],[0,paddle1_pos + PAD_HEIGHT/2],17,'red')
    canvas.draw_line([WIDTH,paddle2_pos - PAD_HEIGHT/2],[WIDTH,paddle2_pos + PAD_HEIGHT/2],17,'green')    
    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/3,HEIGHT/4],50,'red','monospace')
    canvas.draw_text(str(score2),[WIDTH - WIDTH/3,HEIGHT/4],50,'green','monospace')
        
def keydown(key):
    global left_up, left_down, right_up, right_down
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    
    if key == simplegui.KEY_MAP['w']:
        left_up = True
        left_down = False
    if key == simplegui.KEY_MAP['s']:
        left_down = True
        left_up = False
        
    if key == simplegui.KEY_MAP['up']:
        right_up = True
        right_down = False
    if key == simplegui.KEY_MAP['down']:
        right_down = True
        right_up = False
        
   
def keyup(key):
    global left_up,left_down, right_up, right_down
    if key == simplegui.KEY_MAP['w']:
        left_up = False
    if key == simplegui.KEY_MAP['s']:
        left_down = False
    
    if key == simplegui.KEY_MAP['up']:
        right_up = False
    if key == simplegui.KEY_MAP['down']:
        right_down = False


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

#register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game,100)

# start frame
new_game()
frame.start()

