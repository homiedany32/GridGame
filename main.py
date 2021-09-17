import pygame
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 255)
WHITE = (255, 255, 255) # 0
GREEN = (0, 255, 0) # 1
SAND = (214, 198, 148) # 2
WATER = (128, 207, 222) # 3
SEA = (108, 177, 202) # 4

max_color = 4
 
WIDTH = 25
HEIGHT = 25


grid = [
        [4, 4, 4, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 3, 4, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 3, 3, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 3, 3, 2, 2, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 4, 4, 4, 3, 3, 3, 4, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
] 

unit_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
] 



for row in range(32):
    grid.append([])
    for column in range(32):
        grid[row].append(0)  
 



current_units = []


def AddUnit(Team, Typ, X, Y):
    if Team == "Red":
        if Typ == 1:
            current_units.append([Team, 1, X, Y, 10])
        elif Typ == 2:
            current_units.append([Team, 3, X, Y, 20])
        elif Typ == 3:
            current_units.append([Team, 5, X, Y, 15])
        elif Typ == 4:
            current_units.append([Team, 7, X, Y, 10])
    elif Team == "Purple":
        if Typ == 1:
            current_units.append([Team, 2, X, Y, 10])
        elif Typ == 2:
            current_units.append([Team, 4, X, Y, 20])
        elif Typ == 3:
            current_units.append([Team, 6, X, Y, 15])
        elif Typ == 4:
            current_units.append([Team, 8, X, Y, 10])



pygame.init()
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed Grid")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            column = pos[0] // (WIDTH)
            row = pos[1] // (HEIGHT)

            AddUnit("Red", 1, row, column)
            print(current_units)
 
    screen.fill(BLACK)
    
    # map
    for row in range(32):
        for column in range(32):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = SAND
            elif grid[row][column] == 3:
                color = WATER
            elif grid[row][column] == 4:
                color = SEA
            pygame.draw.rect(screen,
                             color,
                             [(WIDTH) * column,
                              (HEIGHT) * row,
                              WIDTH,
                              HEIGHT])
    
    # add units from 'current_units' list
    for i in current_units:

        unit_grid[5][5] = 1

        """
        temp_row = current_units[i][2]
        temp_column = current_units[i][3]
        if current_units[i][0] == "Red":
            if current_units[i][1] == 1:
                unit_grid[temp_row][temp_column] = 1
        """
    # unit drawing
    for row in range(32):
        for column in range(32):
            if unit_grid[row][column] == 1:
                color = RED
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row, 8, 8], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 7], [(WIDTH) * column + 12, (HEIGHT) * row + 14], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 7, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 17, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10], [(WIDTH) * column + 19, (HEIGHT) * row + 10], 2)
            elif unit_grid[row][column] == 2:
                color = PURPLE
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row, 8, 8], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 7], [(WIDTH) * column + 12, (HEIGHT) * row + 14], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 7, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 17, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10], [(WIDTH) * column + 19, (HEIGHT) * row + 10], 2)
            elif unit_grid[row][column] == 3:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 15, 14, 6])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10, 6, 6])
                pygame.draw.line(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 11], [(WIDTH) * column + 15, (HEIGHT) * row + 11], 2)
            elif unit_grid[row][column] == 4:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 15, 14, 6])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10, 6, 6])
                pygame.draw.line(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 11], [(WIDTH) * column + 15, (HEIGHT) * row + 11], 2)
            elif unit_grid[row][column] == 5:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 18, 14, 5])
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 19, (HEIGHT) * row + 18], [(WIDTH) * column + 19, (HEIGHT) * row + 22], [(WIDTH) * column + 24, (HEIGHT) * row + 18]], 0)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 6, (HEIGHT) * row + 18], [(WIDTH) * column + 6, (HEIGHT) * row + 22], [(WIDTH) * column + 1, (HEIGHT) * row + 18]], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 16, (HEIGHT) * row + 17], [(WIDTH) * column + 16, (HEIGHT) * row + 3], 1)
                pygame.draw.line(screen, color, [(WIDTH) * column + 11, (HEIGHT) * row + 17], [(WIDTH) * column + 11, (HEIGHT) * row + 11], 1)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 16, (HEIGHT) * row + 4], [(WIDTH) * column + 16, (HEIGHT) * row + 11], [(WIDTH) * column + 8, (HEIGHT) * row + 8]], 0)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 11, (HEIGHT) * row + 12], [(WIDTH) * column + 11, (HEIGHT) * row + 16], [(WIDTH) * column + 6, (HEIGHT) * row + 14]], 0)
            elif unit_grid[row][column] == 6:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 18, 14, 5])
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 19, (HEIGHT) * row + 18], [(WIDTH) * column + 19, (HEIGHT) * row + 22], [(WIDTH) * column + 24, (HEIGHT) * row + 18]], 0)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 6, (HEIGHT) * row + 18], [(WIDTH) * column + 6, (HEIGHT) * row + 22], [(WIDTH) * column + 1, (HEIGHT) * row + 18]], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 16, (HEIGHT) * row + 17], [(WIDTH) * column + 16, (HEIGHT) * row + 3], 1)
                pygame.draw.line(screen, color, [(WIDTH) * column + 11, (HEIGHT) * row + 17], [(WIDTH) * column + 11, (HEIGHT) * row + 11], 1)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 16, (HEIGHT) * row + 4], [(WIDTH) * column + 16, (HEIGHT) * row + 11], [(WIDTH) * column + 8, (HEIGHT) * row + 8]], 0)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 11, (HEIGHT) * row + 12], [(WIDTH) * column + 11, (HEIGHT) * row + 16], [(WIDTH) * column + 6, (HEIGHT) * row + 14]], 0)
            elif unit_grid[row][column] == 7:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 13, 12, 8])
                pygame.draw.line(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 13], [(WIDTH) * column + 15, (HEIGHT) * row + 3], 3)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 15, (HEIGHT) * row + 3], [(WIDTH) * column + 15, (HEIGHT) * row + 10], [(WIDTH) * column + 4, (HEIGHT) * row + 7]], 1)
            elif unit_grid[row][column] == 8:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 13, 12, 8])
                pygame.draw.line(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 13], [(WIDTH) * column + 15, (HEIGHT) * row + 3], 3)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 15, (HEIGHT) * row + 3], [(WIDTH) * column + 15, (HEIGHT) * row + 10], [(WIDTH) * column + 4, (HEIGHT) * row + 7]], 1)
            

    
    clock.tick(60)
 
    
    pygame.display.flip()
 


pygame.quit()