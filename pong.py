import pygame, sys
from pygame.locals import *

fps = 150
screenheight = 450
screenwidth = 350
paddlewidth = 60
paddleoffset = 20
linewidth = 15

black = (0 ,0 ,0 )	
white = (255, 255 ,255 )

def drawarena():
	DISPLAY.fill((0,0,0))
	pygame.draw.rect(DISPLAY, white, ((0,0),(screenwidth,screenheight)), linewidth*2)
	
	
def drawpaddle(paddle):
		if paddle.bottom > screenheight - linewidth:
			paddle.bottom = screenheight - linewidth
		
		elif paddle.top < linewidth:
			paddle.top = linewidth
			
		pygame.draw.rect(DISPLAY, white, paddle)
		
def drawball(ball):
	pygame.draw.rect(DISPLAY, white, ball)
	
def ballmoving(ball, balldirectx, balldirecty):
		ball.x += balldirectx
		ball.y += balldirecty
		return ball

def wallcollision(ball,balldirectx,balldirecty):
			if ball.top == (linewidth) or ball.bottom == (screenheight - linewidth):
				balldirecty = balldirecty * -1
			if ball.left == (linewidth) or ball.right == (screenwidth - linewidth):
				balldirectx = balldirectx * -1
			return balldirectx,balldirecty
	
def ballcollision(ball,paddle1,paddle2,balldirectx):
			if balldirectx == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
				return -1
			elif balldirectx == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
				return -1
			else: return 1
	
def main():

	pygame.init()
	global DISPLAY
	
	fpsclock = pygame.time.Clock()
	DISPLAY = pygame.display.set_mode((screenwidth,screenheight))
	pygame.display.set_caption("Pong!")
	
	ball1 = screenwidth/2 - linewidth/2
	ball2 = screenheight/2 - linewidth/2
	player1spot = (screenheight - paddlewidth) /2
	player2spot = (screenheight - paddlewidth) /2
	
	balldirectx = -1
	balldirecty = -1
	
	paddle1 = pygame.Rect(paddleoffset, player1spot, linewidth, paddlewidth)
	paddle2 = pygame.Rect(screenwidth - paddleoffset - linewidth, player2spot, linewidth, paddlewidth)
	ball = pygame.Rect(ball1, ball2, linewidth, linewidth)
	
	drawarena()
	drawpaddle(paddle1)
	drawpaddle(paddle2)
	drawball(ball)
	
	while True:
		keypressed = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == quit:
				pygame.quit()
				sys.exit()
			
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_UP:
				paddle1.y = paddle1.y - 5
			if event.key == pygame.K_DOWN:
				paddle1.y = paddle1.y + 5		
		if event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			paddle2.y = mousey - 10
				
		
		
		
		drawarena()
		drawpaddle(paddle1)
		drawpaddle(paddle2)
		drawball(ball)		
		
		ball = ballmoving(ball, balldirectx, balldirecty)
		balldirectx, balldirecty = wallcollision(ball, balldirectx, balldirecty)
		balldirectx = balldirectx * ballcollision(ball, paddle1, paddle2, balldirectx)
		fpsclock.tick(fps)
		pygame.display.update()

		
if __name__=='__main__':
	main()
