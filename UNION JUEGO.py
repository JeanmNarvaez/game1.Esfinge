import turtle
import time
import math
from playsound import playsound
import random

def create_text(pos, txt):
	pen = turtle.Turtle()
	pen.speed(0)
	pen.color("white")
	pen.penup()
	pen.setposition(pos)
	pen.write(txt, False, align="center", font=("Arial", 20, "bold"))
	pen.hideturtle()
	return pen

def start_game():
	global game_state
	game_state = "game"

wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("pppp.png")
wn.title("Esfinge")
wn.setup(700, 700)
wn.tracer(0)
create_text((-150, -330), "aplasta \"q\", para jugar")

#Imagenes
turtle.register_shape("chihumano.gif")
turtle.register_shape("oro.gif")
turtle.register_shape("b.gif")
turtle.register_shape("bb.gif")
turtle.register_shape("bird.gif")
turtle.register_shape("birdr.gif")
turtle.register_shape("puerta.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.shape("circle")
pen.penup()
pen.hideturtle()

wn.listen()
wn.onkeypress(start_game, "q")

game_state = "inicio"


while True:
	pen.clear()
	if game_state == "inicio":
		wn.bgcolor("black")


	elif game_state == "game":
		wn.bgcolor("black")

		import turtle
		import math
		import random
		from playsound import playsound

		nivel = 1

		wn = turtle.Screen()
		wn.bgcolor("black")
		wn.bgpic("pppp.png")
		wn.title("Esfinge")
		wn.setup(700, 700)
		wn.tracer(0)

#texto
		def create_text(pos, txt):
			pen = turtle.Turtle()
			pen.speed(0)
			pen.color("red")
			pen.penup()
			pen.setposition(pos)
			pen.write(txt, False, align="center", font= ("Arial", 60, "bold"))
			pen.hideturtle()
			return pen

		#comienzo
		class Pen(turtle.Turtle):
			def __init__(self):
				turtle.Turtle.__init__(self)
				self.shape("b.gif")
				self.color("red")
				self.penup()
				self.speed(0)

		class Player(turtle.Turtle):
			def __init__(self):
				turtle.Turtle.__init__(self)
				self.shape("chihumano.gif")
				self.color("red")
				self.penup()
				self.speed(0)
				self.gold = 0

			def go_up(self):
				move_to_x = self.xcor()
				move_to_y = self.ycor() + 24
				if (move_to_x, move_to_y) not in walls:
					self.goto(move_to_x, move_to_y)

			def go_down(self):

				move_to_x = self.xcor()
				move_to_y = self.ycor() - 24
				if (move_to_x, move_to_y) not in walls:
					self.goto(move_to_x, move_to_y)

			def go_left(self):
				move_to_x = self.xcor() - 24
				move_to_y = self.ycor()
				if (move_to_x, move_to_y) not in walls:
					self.goto(move_to_x, move_to_y)

			def go_right (self):

				move_to_x = self.xcor() + 24
				move_to_y = self.ycor()

				if (move_to_x, move_to_y) not in walls:
					self.goto(move_to_x, move_to_y)


			def is_collision(self, other):
				a = self.xcor() - other.xcor()
				b = self.ycor() - other.ycor()
				distance = math.sqrt(a ** 2 + b ** 2)

				if distance < 5:
					return True
				else:
					return False
		#Enemigo
		class Enemy(turtle.Turtle):
			def __init__(self, x, y):
				turtle.Turtle.__init__(self)
				self.shape("bird.gif")
				self.color("red")
				self.penup()
				self.speed(0)
				self.gold = 25
				self.goto(x, y)
				self.direction = random.choice(["up", "down", "left", "right"])

			def move(self):
				if self.direction == "up":
					dx = 0
					dy = 24
				elif self.direction == "down":
					dx = 0
					dy = -24
				elif self.direction == "left":
					dx = -24
					dy = 0
					self.shape("bird.gif")
				elif self.direction == "right":
					dx = 24
					dy = 0
					self.shape("birdr.gif")
				else:
					dx = 0
					dy = 0

				move_to_x = self.xcor() + dx
				move_to_y = self.ycor() + dy

				if (move_to_x, move_to_y) not in walls:
					self.goto(move_to_x, move_to_y)
				else:
					self.direction = random.choice(["up", "down", "left", "right"])
				turtle.ontimer(self.move, t=random.randint(200, 400))

		class Treasure(turtle.Turtle):
			def __init__(self, x, y):
				turtle.Turtle.__init__(self)
				self.shape("oro.gif")
				self.color("gold")
				self.penup()
				self.speed(0)
				self.gold = 50
				self.goto(x, y)

			def destroy(self):
				self.goto(2000,2000)
				self.hideturtle()

		#door
		class Door(turtle.Turtle):
			def __init__(self, x, y):
				turtle.Turtle.__init__(self)
				self.shape("puerta.gif")
				self.color("gold")
				self.penup()
				self.speed(0)
				self.goto(x, y)

			def destroy(self):
				self.goto(2000,2000)
				self.hideturtle()


		levels = [""]

		level_1 = [
			"XXXXXXXXXXXXXXXXXXXXXXXXX",
			"XXXXP       XXXXXXXXXXXXX",
			"XXXXXXXX    XXXXXXXX XXXX",
			"XXX XXXXXX   XXXXXXXXXXXX",
			"XXXXXXXXXXXX    XXXXX XXX",
			"XXXXXX XXXXXXXX  XXXXXXXX",
			"XXXXXXXXXXXXXXX   XXXX XX",
			"XXXX XXXXXXXX    XXX XXXX",
			"XXXXXXXXXXX     XXXXXXXXX",
			"XXXXXXX       XXXXXXXXXXX",
			"XXXXX   XXX   XXXXXXX XXX",
			"XXX   XXXXXXX    XXXXXXXX",
			"XX  XXXXXXXXXXXT  XXXXXXX",
			"XXX  T  XXXXXXXXXXXXXXXXX",
			"XXXXXX  XXX XXXXX XXXXXXX",
			"XXXXXX   XXXXXXXXXXXXXXXX",
			"XXXXXX     XXXXXXXXX XXXX",
			"X  XX  XXX   XXXXXXXXXXXX",
			"X      EXXXX     XXXXXXXX",
			"XXX  XXXXXXXXX  XXXXXXXXX",
			"XX  XXXXXXXXXX  XXXXXXXXX",
			"XX XXX XXXXXXX  XXXXXXXXX",
			"XXXXXXXXXXXXXX  XXXXXXXXX",
			"XX XXXXXXX XXXX D XXXXXXX",
			"XXXXXXXXXXXXXXXXXXXXXXXXX"
		]

		treasures = []
		doors = []
		levels.append(level_1)


		def setup_maze(level):
			for y in range(len(level)):
				for x in range(len(level[y])):
					character = level[y][x]
					screen_x = -288 + (x * 24)
					screen_y = 288 - (y * 24)

					if character == "X":
						pen.goto(screen_x, screen_y)
						pen.stamp()
						walls.append((screen_x, screen_y))

					if character == "P":
						player.goto(screen_x, screen_y)

					if character == "T":
						treasures.append(Treasure(screen_x, screen_y))

					if character == "E":
						enemies.append(Enemy(screen_x, screen_y))

					if character == "D":
						doors.append(Door(screen_x, screen_y))





		pen = Pen()
		player = Player()


		walls = []
		enemies = []

		#puntaje
		score_pen = turtle.Turtle()
		score_pen.speed(0)
		score_pen.color("white")
		score_pen.penup()
		score_pen.setposition(0,310)
		scorestring = "Nivel 1 (Ra) Oro: {}".format(player.gold)
		score_pen.write(scorestring, False, align="center", font= ("Arial", 24, "normal"))
		score_pen.hideturtle()

		setup_maze(levels[1])

		turtle.listen()
		turtle.onkey(player.go_up, "Up")
		turtle.onkey(player.go_down, "Down")
		turtle.onkey(player.go_left, "Left")
		turtle.onkey(player.go_right, "Right")
		turtle.onkey(player.go_up, "w")
		turtle.onkey(player.go_down, "s")
		turtle.onkey(player.go_left, "a")
		turtle.onkey(player.go_right, "d")

		#wn.tracer(0)

		for enemy in enemies:
			turtle.ontimer(enemy.move, t=250)

		while True:
			wn.update()

			for treasure in treasures:
				if player.is_collision(treasure):
					player.gold += treasure.gold
					score_pen.clear()
					scorestring = "Nivel 1 (Ra) Oro: %s" % player.gold
					score_pen.write(scorestring, False, align="center", font=("Arial", 24, "normal"))
					treasure.destroy()
					treasures.remove(treasure)
					playsound('coins-1.wav')

				if player.is_collision(treasure):
					player.gold += treasure.gold

					score_pen.clear()
					scorestring = "Nivel 1 (Ra) Oro: {}".format(player.gold)
					score_pen.write(scorestring, False, align="center", font=("Arial", 24, "normal"))
					treasure.destroy()
					treasures.remove(treasure)


			for enemy in enemies:
				if player.is_collision(enemy):
					for enemy in enemies:
						enemy.hideturtle()
					for treasure in treasures:
						treasure.hideturtle()
					player.hideturtle()
					create_text((0, 60), "Humano muerto!")
					playsound('hit.wav')

			for door in doors:
				if player.is_collision(door):
					for door in doors:
						door.hideturtle()
					playsound('door.wav')

					wn.clear()


					def level_up():
						global game_state
						game_state ="game"


					def create_text(pos, txt):
						pen = turtle.Turtle()
						pen.speed(0)
						pen.color("white")
						pen.penup()
						pen.setposition(pos)
						pen.write(txt, False, align="center", font=("Arial", 20, "bold"))
						pen.hideturtle()
						return pen

					wn = turtle.Screen()

					wn.title("Esfinge")
					wn.bgcolor("black")

					wn = turtle.Screen()
					wn.bgcolor("black")
					wn.bgpic("set.png")
					wn.title("Esfinge")
					wn.setup(700, 700)
					wn.tracer(0)
					create_text((-150, -330), "aplasta \"q\", para jugar")

					pen = turtle.Turtle()
					pen.speed(0)
					pen.shape("circle")
					pen.color("blue")
					pen.penup()
					pen.hideturtle()

					wn.listen()
					wn.onkeypress(level_up, "q")

					game_state = "level_up"
					while True:
						pen.clear()
						if game_state == "level_up":
							wn.bgcolor("black")

						if game_state == "game":
							wn.bgpic("dc929e298f5b84335a8f8507d1aeb3bf.png")
							pen.clear()
							wn.clear()

							nivel +=1

							from playsound import playsound
							wn = turtle.Screen()
							wn.clear()
							wn.bgcolor("black")
							wn.bgpic("set.png")
							wn.title("Esfinge")
							wn.setup(700, 700)
							wn.tracer(0)



							# Imagenes
							turtle.register_shape("chihumano.gif")
							turtle.register_shape("oro.gif")
							turtle.register_shape("b.gif")
							turtle.register_shape("bb.gif")
							turtle.register_shape("bird.gif")
							turtle.register_shape("birdr.gif")
							turtle.register_shape("puerta.gif")

							# texto
							def create_text(pos, txt):
								pen = turtle.Turtle()
								pen.speed(0)
								pen.color("red")
								pen.penup()
								pen.setposition(pos)
								pen.write(txt, False, align="center", font=("Arial", 60, "bold"))
								pen.hideturtle()
								return pen

							# comienzo
							class Pen(turtle.Turtle):
								def __init__(self):
									turtle.Turtle.__init__(self)
									self.shape("b.gif")
									self.color("red")
									self.penup()
									self.speed(0)

							class Player(turtle.Turtle):
								def __init__(self):
									turtle.Turtle.__init__(self)
									self.shape("chihumano.gif")
									self.color("red")
									self.penup()
									self.speed(0)
									self.gold = 0

								def go_up(self):
									move_to_x = self.xcor()
									move_to_y = self.ycor() + 24
									if (move_to_x, move_to_y) not in walls:
										self.goto(move_to_x, move_to_y)

								def go_down(self):

									move_to_x = self.xcor()
									move_to_y = self.ycor() - 24
									if (move_to_x, move_to_y) not in walls:
										self.goto(move_to_x, move_to_y)

								def go_left(self):
									move_to_x = self.xcor() - 24
									move_to_y = self.ycor()
									if (move_to_x, move_to_y) not in walls:
										self.goto(move_to_x, move_to_y)

								def go_right(self):

									move_to_x = self.xcor() + 24
									move_to_y = self.ycor()

									if (move_to_x, move_to_y) not in walls:
										self.goto(move_to_x, move_to_y)

								def is_collision(self, other):
									a = self.xcor() - other.xcor()
									b = self.ycor() - other.ycor()
									distance = math.sqrt(a ** 2 + b ** 2)

									if distance < 5:
										return True
									else:
										return False

							# Enemigo
							class Enemy(turtle.Turtle):
								def __init__(self, x, y):
									turtle.Turtle.__init__(self)
									self.shape("bird.gif")
									self.color("red")
									self.penup()
									self.speed(0)
									self.gold = 25
									self.goto(x, y)
									self.direction = random.choice(["up", "down", "left", "right"])

								def move(self):
									if self.direction == "up":
										dx = 0
										dy = 24
									elif self.direction == "down":
										dx = 0
										dy = -24
									elif self.direction == "left":
										dx = -24
										dy = 0
										self.shape("bird.gif")
									elif self.direction == "right":
										dx = 24
										dy = 0
										self.shape("birdr.gif")
									else:
										dx = 0
										dy = 0

									move_to_x = self.xcor() + dx
									move_to_y = self.ycor() + dy

									if (move_to_x, move_to_y) not in walls:
										self.goto(move_to_x, move_to_y)
									else:
										self.direction = random.choice(["up", "down", "left", "right"])
									turtle.ontimer(self.move, t=random.randint(200, 400))

							class Treasure(turtle.Turtle):
								def __init__(self, x, y):
									turtle.Turtle.__init__(self)
									self.shape("oro.gif")
									self.color("gold")
									self.penup()
									self.speed(0)
									self.gold = 50
									self.goto(x, y)

								def destroy(self):
									self.goto(2000, 2000)
									self.hideturtle()

							# door
							class Door(turtle.Turtle):
								def __init__(self, x, y):
									turtle.Turtle.__init__(self)
									self.shape("puerta.gif")
									self.color("gold")
									self.penup()
									self.speed(0)
									self.goto(x, y)

							levels = [""]

							level_2 = [
								"XXXXXXXXXXXXXXXXXXXXXXXXX",
								"XP     X    X      XTXXXX",
								"X XXXXX XXXX XXX XXX XXXX",
								"X       X      X X X X XX",
								"X X  XX XXXXXX X X X X XX",
								"X X T X    E   X X     XX",
								"X XXX XXXXXX XXXXX XXXXXX",
								"X XXX    X X X       XXXX",
								"X    XXX       XXXXX XXXX",
								"XXXX    XXXXXX   E X    X",
								"X   XXX X X    X X X X XX",
								"XXX XXX X X      X X X XX",
								"X T   X X   XX X X X X XX",
								"XXXXX     XXXX X XXX  XXX",
								"X   E  X  XX   X      XXX",
								"X XXXXX X XXXX XXX XXXXXX",
								"X X        X X       XXXX",
								"X X XXXXXX X XXXXX X XXXX",
								"X X T       E      X DXXX",
								"XXXXXXXXXXXXXXXXXXXXXXXXX"
							]

							treasures = []
							doors = []
							levels.append(level_2)

							def setup_maze(level):
								for y in range(len(level)):
									for x in range(len(level[y])):
										character = level[y][x]
										screen_x = -288 + (x * 24)
										screen_y = 288 - (y * 24)

										if character == "X":
											pen.goto(screen_x, screen_y)
											pen.stamp()
											walls.append((screen_x, screen_y))

										if character == "P":
											player.goto(screen_x, screen_y)

										if character == "T":
											treasures.append(Treasure(screen_x, screen_y))

										if character == "E":
											enemies.append(Enemy(screen_x, screen_y))

										if character == "D":
											doors.append(Door(screen_x, screen_y))

							pen = Pen()
							player = Player()

							walls = []
							enemies = []

							# puntaje
							score_pen = turtle.Turtle()
							score_pen.speed(0)
							score_pen.color("white")
							score_pen.penup()
							score_pen.setposition(0, 310)
							scorestring = "Nivel 2 (Ra) Oro".format(player.gold)
							score_pen.write(scorestring, False, align="center", font=("Arial", 24, "normal"))
							score_pen.hideturtle()

							setup_maze(levels[1])

							turtle.listen()
							turtle.onkey(player.go_up, "Up")
							turtle.onkey(player.go_down, "Down")
							turtle.onkey(player.go_left, "Left")
							turtle.onkey(player.go_right, "Right")
							turtle.onkey(player.go_up, "w")
							turtle.onkey(player.go_down, "s")
							turtle.onkey(player.go_left, "a")
							turtle.onkey(player.go_right, "d")

							wn.tracer(0)

							for enemy in enemies:
								turtle.ontimer(enemy.move, t=250)

							while True:
								wn.update()

								for treasure in treasures:
									if player.is_collision(treasure):
										player.gold += treasure.gold
										score_pen.clear()
										scorestring = "Nivel 2 (Ra) Oro: %s" % player.gold
										score_pen.write(scorestring, False, align="center", font=("Arial", 24, "normal"))
										treasure.destroy()
										treasures.remove(treasure)
										playsound('coins-1.wav')

									if player.is_collision(treasure):
										player.gold += treasure.gold

										score_pen.clear()
										scorestring = "Nivel 2 (Ra) Oro: {}".format(player.gold)
										score_pen.write(scorestring, False, align="center", font=("Arial", 24, "normal"))
										treasure.destroy()
										treasures.remove(treasure)

								for enemy in enemies:
									if player.is_collision(enemy):
										for enemy in enemies:
											enemy.hideturtle()
										for treasure in treasures:
											treasure.hideturtle()
										player.hideturtle()
										create_text((0, 60), "Humano muerto!")
										#playsound('hit.wav')
										print("Huamano muerto!")

								from playsound import playsound
								for door in doors:
									if player.is_collision(door):
										for door in doors:
											door.hideturtle()
										#playsound('door.wav')
										wn.clear()


										def level_up():
											global game_state
											game_state = "game"


										def create_text(pos, txt):
											pen = turtle.Turtle()
											pen.speed(0)
											pen.color("white")
											pen.penup()
											pen.setposition(pos)
											pen.write(txt, False, align="center", font=("Arial", 20, "bold"))
											pen.hideturtle()
											return pen


										wn = turtle.Screen()

										wn.title("Esfinge")
										wn.bgcolor("black")

										wn = turtle.Screen()
										wn.bgcolor("black")
										wn.bgpic("HHH.png")
										wn.title("Esfinge")
										wn.setup(700, 700)
										wn.tracer(0)
										create_text((-150, -330), "aplasta \"q\", para jugar")

										pen = turtle.Turtle()
										pen.speed(0)
										pen.shape("circle")
										pen.color("blue")
										pen.penup()
										pen.hideturtle()

										wn.listen()
										wn.onkeypress(level_up, "q")

										game_state = "level_up"
										while True:
											pen.clear()
											if game_state == "level_up":
												wn.bgcolor("black")

											if game_state == "game":
												wn.bgpic("HHH.png")
												pen.clear()
												wn.clear()

												nivel += 1

												from playsound import playsound
												wn = turtle.Screen()
												wn.bgcolor("black")
												wn.bgpic("HHH.png")
												wn.title("Esfinge")
												wn.setup(700, 700)
												wn.tracer(0)

												# Imagenes
												turtle.register_shape("chihumano.gif")
												turtle.register_shape("oro.gif")
												turtle.register_shape("b.gif")
												turtle.register_shape("bb.gif")
												turtle.register_shape("kill.gif")
												turtle.register_shape("killr.gif")
												turtle.register_shape("puerta.gif")


												# texto
												def create_text(pos, txt):
													pen = turtle.Turtle()
													pen.speed(0)
													pen.color("red")
													pen.penup()
													pen.setposition(pos)
													pen.write(txt, False, align="center", font=("Arial", 60, "bold"))
													pen.hideturtle()
													return pen


												# comienzo
												class Pen(turtle.Turtle):
													def __init__(self):
														turtle.Turtle.__init__(self)
														self.shape("b.gif")
														self.color("red")
														self.penup()
														self.speed(0)


												class Player(turtle.Turtle):
													def __init__(self):
														turtle.Turtle.__init__(self)
														self.shape("chihumano.gif")
														self.color("red")
														self.penup()
														self.speed(0)
														self.gold = 0

													def go_up(self):
														move_to_x = self.xcor()
														move_to_y = self.ycor() + 24
														if (move_to_x, move_to_y) not in walls:
															self.goto(move_to_x, move_to_y)

													def go_down(self):

														move_to_x = self.xcor()
														move_to_y = self.ycor() - 24
														if (move_to_x, move_to_y) not in walls:
															self.goto(move_to_x, move_to_y)

													def go_left(self):
														move_to_x = self.xcor() - 24
														move_to_y = self.ycor()
														if (move_to_x, move_to_y) not in walls:
															self.goto(move_to_x, move_to_y)

													def go_right(self):

														move_to_x = self.xcor() + 24
														move_to_y = self.ycor()

														if (move_to_x, move_to_y) not in walls:
															self.goto(move_to_x, move_to_y)

													def is_collision(self, other):
														a = self.xcor() - other.xcor()
														b = self.ycor() - other.ycor()
														distance = math.sqrt(a ** 2 + b ** 2)

														if distance < 5:
															return True
														else:
															return False


												# Enemigo
												class Enemy(turtle.Turtle):
													def __init__(self, x, y):
														turtle.Turtle.__init__(self)
														self.shape("kill.gif")
														self.color("red")
														self.penup()
														self.speed(0)
														self.gold = 25
														self.goto(x, y)
														self.direction = random.choice(["up", "down", "left", "right"])

													def move(self):
														if self.direction == "up":
															dx = 0
															dy = 24
														elif self.direction == "down":
															dx = 0
															dy = -24
														elif self.direction == "left":
															dx = -24
															dy = 0
															self.shape("kill.gif")
														elif self.direction == "right":
															dx = 24
															dy = 0
															self.shape("killr.gif")
														else:
															dx = 0
															dy = 0

														move_to_x = self.xcor() + dx
														move_to_y = self.ycor() + dy

														if (move_to_x, move_to_y) not in walls:
															self.goto(move_to_x, move_to_y)
														else:
															self.direction = random.choice(
																["up", "down", "left", "right"])
														turtle.ontimer(self.move, t=random.randint(200, 400))


												class Treasure(turtle.Turtle):
													def __init__(self, x, y):
														turtle.Turtle.__init__(self)
														self.shape("oro.gif")
														self.color("gold")
														self.penup()
														self.speed(0)
														self.gold = 50
														self.goto(x, y)

													def destroy(self):
														self.goto(2000, 2000)
														self.hideturtle()


												# door
												class Door(turtle.Turtle):
													def __init__(self, x, y):
														turtle.Turtle.__init__(self)
														self.shape("puerta.gif")
														self.color("gold")
														self.penup()
														self.speed(0)
														self.goto(x, y)


												levels = [""]

												level_3 = [
													"XXXXXXXXXXXXXXXXXXXXXXXXX",
													"XXP  T          XXXD  XXX",
													"XXXX   XXXXX  E XXX   XXX",
													"XXXX    XXXXX XXXXX   XXX",
													"XXXXX             X    XX",
													"XXXXXXXXXXXXXX   XXX  XXX",
													"XXX E          XXXXXX  XX",
													"XT XX   XXXX    XX  XX  X",
													"X  XXX  XXXXX  XXX  XX XX",
													"X  XXX   XXXX       X  XX",
													"X       XX     XXXXXX  XX",
													"X   XX   XXXX    X     XX",
													"X    XXXXXXX   XXXXXXE XX",
													"XXX  X  XX     X  XXXX XX",
													"XXX  XXXXX  XXX   X    XX",
													"XXX   XXXX      XXXXX  XX",
													"XXX            XXXX    XX",
													"XXXE X XXXXXXXXXT    XXXX",
													"XXX XX  XXX   XXXX   XXXX",
													"XXXXX  XX XXX   X    XXXX",
													"XXXT    XX     XXX    XXX",
													"XXX XXX      XX    XXXXXX",
													"XX    XX   XXXX  XXXXXXXX",
													"XXX T             XXXXXXX",
													"XXXXXXXXXXXXXXXXXXXXXXXXX"
												]

												treasures = []
												doors = []
												levels.append(level_3)


												def setup_maze(level):
													for y in range(len(level)):
														for x in range(len(level[y])):
															character = level[y][x]
															screen_x = -288 + (x * 24)
															screen_y = 288 - (y * 24)

															if character == "X":
																pen.goto(screen_x, screen_y)
																pen.stamp()
																walls.append((screen_x, screen_y))

															if character == "P":
																player.goto(screen_x, screen_y)

															if character == "T":
																treasures.append(Treasure(screen_x, screen_y))

															if character == "E":
																enemies.append(Enemy(screen_x, screen_y))

															if character == "D":
																doors.append(Door(screen_x, screen_y))


												pen = Pen()
												player = Player()

												walls = []
												enemies = []

												# puntaje
												score_pen = turtle.Turtle()
												score_pen.speed(0)
												score_pen.color("white")
												score_pen.penup()
												score_pen.setposition(0, 310)
												scorestring = "Nivel 3 (Sobek) Oro: {}".format(player.gold)
												score_pen.write(scorestring, False, align="center",
																font=("Arial", 24, "normal"))
												score_pen.hideturtle()

												setup_maze(levels[1])
												print(walls)
												print(enemies)

												turtle.listen()
												turtle.onkey(player.go_up, "Up")
												turtle.onkey(player.go_down, "Down")
												turtle.onkey(player.go_left, "Left")
												turtle.onkey(player.go_right, "Right")
												turtle.onkey(player.go_up, "w")
												turtle.onkey(player.go_down, "s")
												turtle.onkey(player.go_left, "a")
												turtle.onkey(player.go_right, "d")

												wn.tracer(0)

												for enemy in enemies:
													turtle.ontimer(enemy.move, t=250)

												while True:
													for treasure in treasures:
														if player.is_collision(treasure):
															player.gold += treasure.gold
															score_pen.clear()
															scorestring = "Nivel 3 (Sobek) Oro: %s" % player.gold
															score_pen.write(scorestring, False, align="center",
																			font=("Arial", 24, "normal"))
															treasure.destroy()
															treasures.remove(treasure)
															playsound('coins-1.wav')

														if player.is_collision(treasure):
															player.gold += treasure.gold

															score_pen.clear()
															scorestring = "Nivel 3 (Sobek) Oro: {}".format(player.gold)
															score_pen.write(scorestring, False, align="center",
																			font=("Arial", 24, "normal"))
															treasure.destroy()
															treasures.remove(treasure)

													for enemy in enemies:
														if player.is_collision(enemy):
															for enemy in enemies:
																enemy.hideturtle()
															for treasure in treasures:
																treasure.hideturtle()
															player.hideturtle()
															create_text((0, 60), "Humano muerto!")
															#playsound('hit.wav')
															print("Huamano muerto!")

													from playsound import playsound
													for door in doors:
														if player.is_collision(door):
															for door in doors:
																door.hideturtle()
															#playsound('door.wav')
															wn.clear()


															def level_up():
																global game_state
																game_state = "game"


															def create_text(pos, txt):
																pen = turtle.Turtle()
																pen.speed(0)
																pen.color("white")
																pen.penup()
																pen.setposition(pos)
																pen.write(txt, False, align="center",
																		  font=("Arial", 20, "bold"))
																pen.hideturtle()
																return pen


															wn = turtle.Screen()

															wn.title("Esfinge")
															wn.bgcolor("white")

															wn = turtle.Screen()
															wn.bgcolor("black")
															wn.bgpic("hell_background.png")
															wn.title("Esfinge")
															wn.setup(700, 700)
															wn.tracer(0)
															create_text((-150, -330), "aplasta \"q\", para jugar")

															from playsound import playsound
															wn = turtle.Screen()
															wn.bgcolor("black")
															wn.bgpic("hell_background.png")
															wn.title("Esfinge")
															wn.setup(700, 700)
															wn.tracer(0)

															# Imagenes
															turtle.register_shape("chihumano.gif")
															turtle.register_shape("oro.gif")
															turtle.register_shape("b.gif")
															turtle.register_shape("bb.gif")
															turtle.register_shape("anubisright.gif")
															turtle.register_shape("anubisleft.gif")
															turtle.register_shape("puerta.gif")


															# texto
															def create_text(pos, txt):
																pen = turtle.Turtle()
																pen.speed(0)
																pen.color("red")
																pen.penup()
																pen.setposition(pos)
																pen.write(txt, False, align="center",
																		  font=("Arial", 60, "bold"))
																pen.hideturtle()
																return pen


															# comienzo
															class Pen(turtle.Turtle):
																def __init__(self):
																	turtle.Turtle.__init__(self)
																	self.shape("b.gif")
																	self.color("red")
																	self.penup()
																	self.speed(0)


															class Player(turtle.Turtle):
																def __init__(self):
																	turtle.Turtle.__init__(self)
																	self.shape("chihumano.gif")
																	self.color("red")
																	self.penup()
																	self.speed(0)
																	self.gold = 0

																def go_up(self):
																	move_to_x = self.xcor()
																	move_to_y = self.ycor() + 24
																	if (move_to_x, move_to_y) not in walls:
																		self.goto(move_to_x, move_to_y)

																def go_down(self):

																	move_to_x = self.xcor()
																	move_to_y = self.ycor() - 24
																	if (move_to_x, move_to_y) not in walls:
																		self.goto(move_to_x, move_to_y)

																def go_left(self):
																	move_to_x = self.xcor() - 24
																	move_to_y = self.ycor()
																	if (move_to_x, move_to_y) not in walls:
																		self.goto(move_to_x, move_to_y)

																def go_right(self):

																	move_to_x = self.xcor() + 24
																	move_to_y = self.ycor()

																	if (move_to_x, move_to_y) not in walls:
																		self.goto(move_to_x, move_to_y)

																def is_collision(self, other):
																	a = self.xcor() - other.xcor()
																	b = self.ycor() - other.ycor()
																	distance = math.sqrt(a ** 2 + b ** 2)

																	if distance < 5:
																		return True
																	else:
																		return False


															# Enemigo
															class Enemy(turtle.Turtle):
																def __init__(self, x, y):
																	turtle.Turtle.__init__(self)
																	self.shape("anubisleft.gif")
																	self.color("red")
																	self.penup()
																	self.speed(0)
																	self.gold = 25
																	self.goto(x, y)
																	self.direction = random.choice(
																		["up", "down", "left", "right"])

																def move(self):
																	if self.direction == "up":
																		dx = 0
																		dy = 24
																	elif self.direction == "down":
																		dx = 0
																		dy = -24
																	elif self.direction == "left":
																		dx = -24
																		dy = 0
																		self.shape("anubisleft.gif")
																	elif self.direction == "right":
																		dx = 24
																		dy = 0
																		self.shape("anubisright.gif")
																	else:
																		dx = 0
																		dy = 0

																	move_to_x = self.xcor() + dx
																	move_to_y = self.ycor() + dy

																	if (move_to_x, move_to_y) not in walls:
																		self.goto(move_to_x, move_to_y)
																	else:
																		self.direction = random.choice(
																			["up", "down", "left", "right"])
																	turtle.ontimer(self.move,
																				   t=random.randint(200, 400))


															class Treasure(turtle.Turtle):
																def __init__(self, x, y):
																	turtle.Turtle.__init__(self)
																	self.shape("oro.gif")
																	self.color("gold")
																	self.penup()
																	self.speed(0)
																	self.gold = 50
																	self.goto(x, y)

																def destroy(self):
																	self.goto(2000, 2000)
																	self.hideturtle()


															# door
															class Door(turtle.Turtle):
																def __init__(self, x, y):
																	turtle.Turtle.__init__(self)
																	self.shape("puerta.gif")
																	self.color("gold")
																	self.penup()
																	self.speed(0)
																	self.goto(x, y)


															levels = [""]

															level_4 = [
																"XXXXXXXXXXXXXXXXXXXXXXXXX",
																"XXP                   XXX",
																"XX    XXXXX  XXXXX  XXXXX",
																"XXXXX    XXXXXXXXX   XXXX",
																"XXXXXX         EX E   XXX",
																"XXXXXXXXXXX  X  XXX  XXXX",
																"XXXX X        XXXXXXT XXX",
																"XXXTXX   XX    XX  XX TXX",
																"XX  XXX XXXX  XXX  XXXXXX",
																"XX  XX  XXXX       X  XXX",
																"XX     XX     XXXXXX  XXX",
																"XX XX   XXXX       E  XXX",
																"X  E XXXXXXX   XXXXXX XXX",
																"XXXX  X  XX   T X  XXXXXX",
																"XXXX  XXXXX  XXX      XXX",
																"XXXX   XXXX      XXX  XXX",
																"XXXX      E      X  X XXX",
																"XXXXX XXXXXXXXXX    XXXXX",
																"XXXX XXX  XXX XXXX  XXXXX",
																"XXXXXX  XX X        XXXXX",
																"XXXXXE        XXX    XXXX",
																"XXXXXXX T   XX    XXXXXXX",
																"XXXD XXXXXXXXX  XXXXXXXXX",
																"XXX      E       XXXXXXXX",
																"XXXXXXXXXXXXXXXXXXXXXXXXX"
															]

															treasures = []
															doors = []
															levels.append(level_4)


															def setup_maze(level):
																for y in range(len(level)):
																	for x in range(len(level[y])):
																		character = level[y][x]
																		screen_x = -288 + (x * 24)
																		screen_y = 288 - (y * 24)

																		if character == "X":
																			pen.goto(screen_x, screen_y)
																			pen.stamp()
																			walls.append((screen_x, screen_y))

																		if character == "P":
																			player.goto(screen_x, screen_y)

																		if character == "T":
																			treasures.append(
																				Treasure(screen_x, screen_y))

																		if character == "E":
																			enemies.append(Enemy(screen_x, screen_y))

																		if character == "D":
																			doors.append(Door(screen_x, screen_y))


															pen = Pen()
															player = Player()

															walls = []
															enemies = []

															# puntaje
															score_pen = turtle.Turtle()
															score_pen.speed(0)
															score_pen.color("white")
															score_pen.penup()
															score_pen.setposition(0, 310)
															scorestring = "Nivel 4 (Anubis) Oro: {}".format(player.gold)
															score_pen.write(scorestring, False, align="center",
																			font=("Arial", 24, "normal"))
															score_pen.hideturtle()

															setup_maze(levels[1])
															print(walls)
															print(enemies)

															turtle.listen()
															turtle.onkey(player.go_up, "Up")
															turtle.onkey(player.go_down, "Down")
															turtle.onkey(player.go_left, "Left")
															turtle.onkey(player.go_right, "Right")
															turtle.onkey(player.go_up, "w")
															turtle.onkey(player.go_down, "s")
															turtle.onkey(player.go_left, "a")
															turtle.onkey(player.go_right, "d")

															wn.tracer(0)

															for enemy in enemies:
																turtle.ontimer(enemy.move, t=250)

															while True:
																for treasure in treasures:
																	if player.is_collision(treasure):
																		player.gold += treasure.gold
																		score_pen.clear()
																		scorestring = "Nivel 4 (Anubis) Oro: %s" % player.gold
																		score_pen.write(scorestring, False,
																						align="center",
																						font=("Arial", 24, "normal"))
																		treasure.destroy()
																		treasures.remove(treasure)
																		playsound('coins-1.wav')

																	if player.is_collision(treasure):
																		player.gold += treasure.gold

																		score_pen.clear()
																		scorestring = "Nivel 4 (Anubis) Oro: {}".format(
																			player.gold)
																		score_pen.write(scorestring, False,
																						align="center",
																						font=("Arial", 24, "normal"))
																		treasure.destroy()
																		treasures.remove(treasure)

																for enemy in enemies:
																	if player.is_collision(enemy):
																		for enemy in enemies:
																			enemy.hideturtle()
																		for treasure in treasures:
																			treasure.hideturtle()
																		player.hideturtle()
																		create_text((0, 60), "Humano muerto!")
																		#playsound('hit.wav')
																		print("Huamano muerto!")

																from playsound import playsound
																for door in doors:
																	if player.is_collision(door):
																		for door in doors:
																			door.hideturtle()
																		#playsound('door.wav')
																		wn.clear()


																		def level_up():
																			global game_state
																			game_state = "game"


																		def create_text(pos, txt):
																			pen = turtle.Turtle()
																			pen.speed(0)
																			pen.color("white")
																			pen.penup()
																			pen.setposition(pos)
																			pen.write(txt, False, align="center",
																					  font=("Arial", 20, "bold"))
																			pen.hideturtle()
																			return pen


																		wn = turtle.Screen()

																		wn.title("Esfinge")
																		wn.bgcolor("black")

																		wn = turtle.Screen()
																		wn.bgcolor("black")
																		wn.bgpic("sfin.gif")
																		wn.title("Esfinge")
																		wn.setup(700, 700)
																		wn.tracer(0)
																		create_text((-150, -330),
																					"aplasta \"q\", para jugar")

																		pen = turtle.Turtle()
																		pen.speed(0)
																		pen.shape("circle")
																		pen.color("blue")
																		pen.penup()
																		pen.hideturtle()

																		wn.listen()
																		wn.onkeypress(level_up, "q")

																		game_state = "level_up"
																		while True:
																			pen.clear()
																			if game_state == "level_up":
																				wn.bgcolor("black")

																			if game_state == "game":
																				wn.bgpic(
																					"sfin.gif")
																				pen.clear()
																				wn.clear()

																				nivel += 1

																				import time
																				import turtle

																				def create_text(pos, txt):
																					pen = turtle.Turtle()
																					pen.speed(0)
																					pen.color("red")
																					pen.penup()
																					pen.setposition(pos)
																					pen.write(txt, False,
																							  align="center", font=(
																						"Arial", 60, "bold"))
																					pen.hideturtle()
																					return pen


																				# Set up the screen
																				wn = turtle.Screen()
																				wn.setup(1000, 600)
																				wn.colormode(255)
																				wn.bgcolor(0, 0, 70)
																				wn.title("Esfinge Acertijos")
																				wn.tracer(0)
																				# Make boxes
																				# box C
																				turtle.speed(0)
																				turtle.hideturtle()
																				turtle.penup()
																				turtle.goto(-450, -250)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				turtle.color("goldenrod")
																				for sides in range(2):
																					turtle.fd(425)
																					turtle.left(90)
																					turtle.fd(125)
																					turtle.left(90)
																				turtle.end_fill()

																				# box D
																				turtle.penup()
																				turtle.goto(25, -250)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				for sides in range(2):
																					turtle.fd(425)
																					turtle.left(90)
																					turtle.fd(125)
																					turtle.left(90)
																				turtle.end_fill()

																				# box A
																				turtle.penup()
																				turtle.goto(-450, -75)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				for sides in range(2):
																					turtle.fd(425)
																					turtle.left(90)
																					turtle.fd(125)
																					turtle.left(90)
																				turtle.end_fill()

																				# box B
																				turtle.penup()
																				turtle.goto(25, -75)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				for sides in range(2):
																					turtle.fd(425)
																					turtle.left(90)
																					turtle.fd(125)
																					turtle.left(90)
																				turtle.end_fill()

																				# question box
																				turtle.penup()
																				turtle.goto(-450, 100)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				for sides in range(2):
																					turtle.fd(625)
																					turtle.left(90)
																					turtle.fd(150)
																					turtle.left(90)
																				turtle.end_fill()

																				# Score box
																				turtle.penup()
																				turtle.goto(225, 100)
																				turtle.pendown()
																				turtle.begin_fill()
																				turtle.setheading(0)
																				for sides in range(2):
																					turtle.fd(225)
																					turtle.left(90)
																					turtle.fd(150)
																					turtle.left(90)
																				turtle.end_fill()

																				# Create Question turtle
																				quest = turtle.Turtle()
																				quest.speed(0)
																				quest.hideturtle()
																				quest.penup()
																				quest.goto(-425, 150)

																				# Create Score turtle
																				score1 = turtle.Turtle()
																				score1.speed(0)
																				score1.hideturtle()
																				score1.penup()
																				score1.goto(250, 145)

																				# Create Answer turtles
																				# A
																				A = turtle.Turtle()
																				A.speed(0)
																				A.hideturtle()
																				A.penup()
																				A.goto(-425, -50)

																				# B
																				B = turtle.Turtle()
																				B.speed(0)
																				B.hideturtle()
																				B.penup()
																				B.goto(50, -50)

																				# C
																				C = turtle.Turtle()
																				C.speed(0)
																				C.hideturtle()
																				C.penup()
																				C.goto(-425, -225)

																				# D
																				D = turtle.Turtle()
																				D.speed(0)
																				D.hideturtle()
																				D.penup()
																				D.goto(50, -225)

																				# Opening Credits
																				quest.write(
																					"Bienvenido a los Acertijos!",
																					font=("Verdana", 23, "bold"))
																				time.sleep(3)
																				quest.clear()

																				quest.write(
																					"lograste esquivarte de los Dioses!",
																					font=("Verdana", 23, "bold"))
																				time.sleep(3)
																				quest.clear()

																				quest.write(
																					"Hay 6 preguntas...",
																					font=("Verdana", 23, "bold"))
																				time.sleep(3)
																				quest.clear()

																				quest.write(
																					"Aplasta a, b, c, d para contestar!",
																					font=("Verdana", 23, "bold"))
																				time.sleep(3)
																				quest.clear()

																				quest.write(
																					"Que los dioses le acompañe...",
																					font=("Verdana", 23, "bold"))
																				time.sleep(3)
																				quest.clear()

																				# NUMBER OF CORRECT ANSWERS HERE
																				correctNow = 0

																				score1.write("{}".format(correctNow),font=("Verdana", 45, "bold"))

																				# Variables
																				CurrentQ = 1

																				# Key Functions
																				def chooseAnswerA():
																					global select
																					select = 'A'
																					evaluate()


																				def chooseAnswerB():
																					global select
																					select = 'B'
																					evaluate()


																				def chooseAnswerC():
																					global select
																					select = 'C'
																					evaluate()


																				def chooseAnswerD():
																					global select
																					select = 'D'
																					evaluate()


																				def evaluate():
																					global correctNow
																					global CurrentQ
																					if correct == select:
																						quest.clear()
																						quest.write("BIEN!!!", font=(
																						"Verdana", 23, "bold"))
																						time.sleep(1.2)
																						score1.clear()
																						correctNow += 1
																						score1.write(
																							"{}".format(correctNow),
																							font=(
																							"Verdana", 45, "bold"))
																					else:
																						quest.clear()
																						quest.write(
																							"MALL!!! la respuesta era {}".format(
																								correct), font=(
																							"Verdana", 23, "bold"))
																						time.sleep(1.2)
																						quest.clear()
																					CurrentQ += 1
																					clearBoard()
																					GetQuestionNum()


																				def GetQuestionNum():
																					if CurrentQ == 2:
																						question2()

																					if CurrentQ == 3:
																						question3()

																					if CurrentQ == 4:
																						question4()

																					if CurrentQ == 5:
																						question5()

																					if CurrentQ == 6:
																						question6()

																					if CurrentQ == 7:
																						question7()


																				def clearBoard():
																					quest.clear()
																					A.clear()
																					B.clear()
																					C.clear()
																					D.clear()


																				def question1():
																					quest.write(
																						"¿Qué puede devolver la vida a los muertos; "
																						"\nhacerte llorar, reír y sentirte joven; y "
																						"\naguantar toda la vida a pesar de haber sido "
																						"\ncreado en un instante?",
																						font=("Verdana", 15, "bold"))

																					A.write("A. muerte", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. cruz", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. memoria", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. religion", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'C'


																				def question2():
																					quest.write(
																						"¿Qué es grande pero nunca crece, tiene raíces "
																						"\n invisibles y es más alto que los árboles?",
																						font=("Verdana", 15, "bold"))
																					A.write("A. montañas", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. pyramides", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. humanos", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. arboles", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'A'


																				def question3():
																					quest.write(
																						"Todas las criaturas son devoradas por esta cosa:"
																						"\npájaros, bestias, árboles y flores; muerde hierro,"
																						"\nmasca acero, muele piedras duras para hacer harina,"
																						"\nmata monarcas y destruye pueblos.",
																						font=("Verdana", 15, "bold"))
																					A.write("A. agua", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. oxygeno", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. tiempo", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. gigantes", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'C'


																				def question4():
																					quest.write(
																						"Estando roto es más útil que sin romperse."
																						"\n¿Que es ?",
																						font=("Verdana", 15, "bold"))
																					A.write("A. camiseta", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. huevo", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. coco", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. casa", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'B'


																				def question5():
																					quest.write(
																						"Parte del humano que tiene la capacidad de"
																						"\naumentar por 9 su tamaño¿qué es?",
																						font=("Verdana", 15, "bold"))
																					A.write("A. dientes", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. nariz", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. pupila", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. fetos", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'C'


																				def question6():
																					quest.write(
																						"Hay algo que aunque te pertenezca la gente"
																						"\nsiempre lo utiliza mas que tu ¿que es?",
																						font=("Verdana", 15, "bold"))
																					A.write("A. numeros", font=(
																					"Verdana", 23, "bold"))
																					B.write("B. oxygeno", font=(
																					"Verdana", 23, "bold"))
																					C.write("C. cerebro", font=(
																					"Verdana", 23, "bold"))
																					D.write("D. nombre", font=(
																					"Verdana", 23, "bold"))
																					global correct
																					correct = 'D'


																				def question7():
																					quest.write("Tu resultado fue:",
																								font=(
																								"Verdana", 15, "bold"))
																					A.write("gracias ", font=(
																					"Verdana", 23, "bold"))
																					B.write("por", font=(
																					"Verdana", 23, "bold"))
																					C.write("jugar", font=(
																					"Verdana", 23, "bold"))
																					D.write("intenta romper tu "
																							"\nrecord", font=(
																					"Verdana", 23, "bold"))
																					time.sleep(100)
																					quest.clear()


																				# Key bindings
																				wn.listen()
																				wn.onkeypress(chooseAnswerA, "a")
																				wn.onkeypress(chooseAnswerA, "A")
																				wn.onkeypress(chooseAnswerB, "b")
																				wn.onkeypress(chooseAnswerB, "B")
																				wn.onkeypress(chooseAnswerC, "c")
																				wn.onkeypress(chooseAnswerC, "C")
																				wn.onkeypress(chooseAnswerD, "d")
																				wn.onkeypress(chooseAnswerD, "D")

																				# Start Game
																				question1()

																				turtle.exitonclick()
																				wn.update()

																wn.update()

													wn.update()
								wn.update()
	wn.update()