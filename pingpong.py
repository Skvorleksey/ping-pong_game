import pygame
import sys

pygame.font.init()

#create a start button
class Button():
	def __init__(self, screen, x, y, write):
		self.screen = screen
		self.x = x
		self.y = y
		self.font = pygame.font.Font(None, 40)
		self.text = self.font.render(write, 1, (100, 100, 100))
		self.start = False

	def show_button(self):
		pygame.draw.rect(self.screen,(200,200,250),(self.x,self.y,100,60))
		self.screen.blit(self.text, (self.x + 10,self.y + 15))

	def check_button(self):
		if self.x < pygame.mouse.get_pos()[0] < self.x + 100:
				if self.y < pygame.mouse.get_pos()[1] < self.y + 60:
					if pygame.mouse.get_pressed()[0] == 1:
						self.start = True

class Platform():
	def __init__(self,screen,x,y):
		self.screen = screen
		self.x = x
		self.y = y
		self.move_y = 1
		self.move_up = False
		self.move_down = False

	def show_platform(self):
		pygame.draw.rect(self.screen,(200,200,250),(self.x,self.y,15,100))

	def move(self):
		if self.move_up == True:
			self.y -= self.move_y
		if self.move_down == True:
			self.y += self.move_y


		

#create a ball
class Ball():
	def __init__(self, screen):
		self.screen = screen
		self.x = 400
		self.y = 300
		self.r = 20
		self.move_x = 1
		self.move_y = 1
		self.move_down = True
		self.move_up = False
		self.move_left = False
		self.move_right = True
		self.ball_out = False

	#draws the ball
	def show_ball(self):
		pygame.draw.circle(self.screen,(200,200,250),(self.x,self.y),self.r)

	#defines the ball's direction
	def move(self):
		self.x += self.move_x
		self.y += self.move_y
		if self.move_down:
			self.move_y = 1
			self.move_up = False
		if self.move_up:
			self.move_y = -1
			self.move_down = False
		if self.move_right:
			self.move_x = 1
			self.move_left = False
		if self.move_left:
			self.move_x = -1
			self.move_right = False
		if self.x >= 850:
			self.ball_out = True
		if self.y == 580:
			self.move_up = True
			self.move_down = False
		if self.x <= -50:
			self.ball_out = True
		if self.y == 20:
			self.move_down = True
			self.move_up = False

	def check(self):
		if self.ball_out == True:
			self.x = 400
			self.y = 300
			self.ball_out = False

class Countbox:
	def __init__(self, screen, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		self.count = 0
		
	def upd_count(self):
		self.count += 1

	def show_count(self):
		self.font = pygame.font.Font(None, 40)
		self.text = self.font.render(str(self.count), 1, (100, 100, 100))
		self.screen.blit(self.text,(self.x, self.y))



#main class of the game
class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((800,600))
		self.screencaption = pygame.display.set_caption("Возможно это пинг-понг")
		self.run = True
		#objects
		self.ball = Ball(self.screen)
		self.player = Platform(self.screen,5,250)
		self.player2 = Platform(self.screen,780,250)
		#buttons
		self.start_button = Button(self.screen, 370, 280, "1 player")
		self.start_button2 = Button(self.screen,370,360, "2 players")
		self.pause_button = Button(self.screen, 370, 5, "Pause")
		self.resume_button = Button(self.screen, 370, 320, "Resume")
		#countboxes
		self.main_count = Countbox(self.screen, 300, 20)
		self.count1 = Countbox(self.screen, 300, 20)
		self.count2 = Countbox(self.screen, 500, 20)



	#main loop
	def rungame(self):
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						if self.start_button2.start:
							self.player.move_up = True
						if self.start_button.start:
							self.player.move_up = True
							self.player2.move_up = True
					if event.key == pygame.K_s:
						if self.start_button2.start:
							self.player.move_down = True
						if self.start_button.start:
							self.player2.move_down = True
							self.player.move_down = True
					if event.key == pygame.K_UP:
						if self.start_button2.start:
							self.player2.move_up = True
						if self.start_button.start:
							self.player2.move_up = True
							self.player.move_up = True
					if event.key == pygame.K_DOWN:
						if self.start_button2.start:
							self.player2.move_down = True
						if self.start_button.start:
							self.player2.move_down = True
							self.player.move_down = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						if self.start_button2.start:
							self.player.move_up = False
						if self.start_button.start:
							self.player2.move_up = False
							self.player.move_up = False
					if event.key == pygame.K_s:
						if self.start_button2.start:
							self.player.move_down = False
						if self.start_button.start:
							self.player2.move_down = False
							self.player.move_down = False
					if event.key == pygame.K_UP:
						if self.start_button2.start:
							self.player2.move_up = False
						if self.start_button.start:
							self.player2.move_up = False
							self.player.move_up = False
					if event.key == pygame.K_DOWN:
						if self.start_button2.start:
							self.player2.move_down = False
						if self.start_button.start:
							self.player2.move_down = False
							self.player.move_down = False

			self.screen.fill((200,120,120))
			if self.start_button.start == False and self.start_button2.start == False:
				self.start_button.show_button()
				self.start_button2.show_button()

			#checks is button pressed or not
			self.start_button.check_button()
			self.start_button2.check_button()
			self.pause_button.check_button()
			self.resume_button.check_button()


			#check ball and platform collision
			if self.player.x + 15 == self.ball.x - 20:
				if self.player.y - 20 < self.ball.y < self.player.y + 120:
					self.ball.move_right = True
					if self.start_button.start == True:
						self.main_count.upd_count()


			if self.player2.x  == self.ball.x + 20:
				if self.player2.y - 20 < self.ball.y < self.player2.y + 120:
					self.ball.move_right = False
					self.ball.move_left = True
					if self.start_button.start == True:
						self.main_count.upd_count()

			#checks the targets
			if self.ball.ball_out == True and self.ball.x > 800:
				self.count1.upd_count()
			if self.ball.ball_out == True and self.ball.x < 0:
				self.count2.upd_count()

			self.ball.check()

			# it will be working only after button is pressed
			if self.start_button.start or self.start_button2.start == True:
				if self.pause_button.start == False:
					self.resume_button.start = True
					self.ball.move()
					self.player.move()
					self.player2.move()
					self.pause_button.show_button()

				if self.pause_button.start == True:
					self.resume_button.start = False
					self.resume_button.show_button()
				if self.resume_button.start == True:
					self.pause_button.start = False


				if self.start_button.start == True:
					self.main_count.show_count()
				if self.start_button2.start == True:
					self.count1.show_count()
					self.count2.show_count()

				self.ball.show_ball()
				self.player.show_platform()
				self.player2.show_platform()



			pygame.time.delay(5)
			pygame.display.flip()
			
			

game = Game()
game.rungame()
