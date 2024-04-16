import turtle
import random
import time
from playsound import playsound

score = 0
streak = 0
row = False
cooldown = False

def default(x, y):
		global score
		global streak
		global row
		global cooldown

		if not cooldown:  # Check if the target is clickable
			score += 1
			streak += 1
			row = True
			if row == True and streak == 1:
				playsound("OneKill.mp3", block = False)
			elif row == True and streak == 2:
				playsound("TwoKills.mp3", block = False)
			elif row == True and streak == 3:
				playsound("ThreeKills.mp3", block = False)
			elif row == True and streak == 4:
				playsound("FourKills.mp3", block = False)
			elif row == True and streak >= 5:
				playsound("FiveKills.mp3")

			# Set cooldown after clicking
			cooldown = True
			turtle.ontimer(reset_cooldown, 500)  # 500 milliseconds cooldown

def reset_cooldown():
    global cooldown
    cooldown = False

def noclick():
    global row
    global streak
    row = False
    streak = 0

tile = turtle.Turtle()
tile.speed(9)
tile.shapesize(.75, .75)
tile.shape("circle")
time.sleep(1)
click = False
loop = 0
skinLoop = True
while score < 5 and not click:
		click = True
		y = random.randint(-150, 150)
		x = random.randint(-200, 200)
		loop += 1
		tile.up()
		tile.setposition(x, 10)
		time.sleep(.5)
		tile.onclick(lambda x, y, t=tile: default(x, y))

		print(score, "Streak:", streak)
		click = False

print("Number of tiles spawned:", loop, ". You hit 5.")
print("Your accuracy:" , 5/loop)

