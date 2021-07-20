import sys, pygame
from colors import *

# Utils for path finder
def search_point(queue:list, point:tuple):
	for i in queue:
		if i[0] == point:
			return True

def findPath(maze:list, start:tuple, end:tuple):
	queue = [(start, [start])]

	dir_row = [-1, 1, 0, 0]
	dir_col = [0, 0, 1, -1]
	end_reach = False
	visited = []
	
	path = []

	while queue:
		q = queue.pop(0)
		r,c = q[0]
		if (r, c) == end:
			path = q[1]
			end_reach = True
			break
		
		visited.append((r,c))
		for i in range(len(dir_row)):
			curr_r = r + dir_row[i]
			curr_c = c + dir_col[i]
			if curr_r < 0 or curr_r >= len(maze): continue
			if curr_c < 0 or curr_c >= len(maze[curr_r]): continue
			if maze[curr_r][curr_c] == 1: continue
			if search_point(queue, (curr_r, curr_c)) or (curr_r, curr_c) in visited: continue
			queue.append(((curr_r, curr_c), [*q[1], (curr_r, curr_c)]))

	return path


# visualizing with pygame 
def run(maze: list, start: tuple, end: tuple):
	if not maze:
		return
	pygame.init()
	size = width, height = len(maze[0]) * 16 + 1, len(maze)  * 16 + 1
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('Breadth-First Search Pathfinding')
	path = findPath(maze, start, end)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
		
		for i, l in enumerate(maze):
			for y,c in enumerate(l):
				color = white
				if (i, y) == start:
					color = green
				elif (i, y) == end:
					color = blue
				elif c == 1:
					color = red
				elif (i,y) in path:
					color=  lightgreen
				pygame.draw.rect(screen, color, (16 * y + 1, 16 * i + 1, 15, 15))

		pygame.display.flip()
		screen.fill(darkgray)