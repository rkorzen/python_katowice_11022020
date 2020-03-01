# pip install pyatuogui
import pyautogui, time
time.sleep(2)
pyautogui.click()    # click to put drawing program in focus
# distance = 200
# while distance > 0:
# 	pyautogui.dragRel(distance, 0, duration=0.001)   # move right
# 	distance = distance - 2
# 	pyautogui.dragRel(0, distance, duration=0.001)   # move down
# 	pyautogui.dragRel(-distance, 0, duration=0.001)  # move left
# 	distance = distance - 8
# 	pyautogui.dragRel(0, -distance, duration=0.001)  # move up

# dist = 30
# for j in range(5):

# 	for i in range(5):
# 		pyautogui.dragRel(0, -dist, duration=0.001)   # move right
# 		pyautogui.dragRel(dist, 0, duration=0.001)   # move right
# 		pyautogui.dragRel(0, dist, duration=0.001)   # move right
# 	pyautogui.dragRel(-5*dist, 0, duration=0.005)	
# 	if i < 4:
# 		pyautogui.dragRel(0, dist, duration=0.001)   # move right
# 	else:
# 		pyautogui.move(0, 0)

# dist = 30
# for j in range(10):

# 	for i in range(10):
# 		pyautogui.dragRel(0, -dist, duration=0.001)   # move right
# 		pyautogui.dragRel(dist, 0, duration=0.001)   # move right
# 		pyautogui.dragRel(0, dist, duration=0.001)   # move right
# 	pyautogui.dragRel(-10*dist, 0, duration=0.05)	
# 	pyautogui.dragRel(0, dist, duration=0.001)   # move right

def up(dist):
	pyautogui.dragRel(0, -dist, duration=0.001)

def down(dist):
	pyautogui.dragRel(0, dist, duration=0.001)

def left(dist):
	pyautogui.dragRel(-dist, 0, duration=0.001)

def right(dist):
	pyautogui.dragRel(dist, 0, duration=0.001)


def fill(dist, stopDown=False):
	for i in range(dist):
		down(dist)
		right(1)
		if not stopDown:
			up(dist)

# 0.001 = 0.001

dist = 30


def draw_even():
	for i in range(3):
		if i % 2 == 1:
			fill(dist)
		else:		
			down(dist)
			right(dist)
			if i == 4:
				pass
				#down(dist)
			else:
				up(dist)

	pyautogui.dragRel(-3*dist, 0, duration=0.005)	

def draw_odd():

	for i in range(3):
		if i % 2 == 0:
			fill(dist)
		else:		
			down(dist)
			right(dist)
			if i == 4:
				pass
				#down(dist)
			else:
				up(dist)

	pyautogui.dragRel(-3*dist, 0, duration=0.005)	


for i in range(3):
	if i % 2 == 0:
		draw_even()
	else:
		draw_odd()

	if i < 2:
		pyautogui.dragRel(0, dist, duration=0.001)   # move right
	else:
		pyautogui.move(0, 0)