from numpy import array

def makematrix(matrix_lines,matrix_columns):
    matrix_local = []
    for lines in range(matrix_lines):
        line = [None] * matrix_columns
        matrix_local += [line]
    
    return matrix_local

def maze_matrix(matrix, matrix_lines, matrix_columns):
    for line in range(matrix_lines):
        line_local = input().split()
        for column in range(matrix_columns):
            matrix[line][column] = line_local[column]

def entries(matrix):
    entry = 1
    maze_entries = {}
    for index, value in enumerate(matrix[len(matrix) - 1]):
        if value != -1:
            maze_entries[entry] = index
            entry += 1
    
    return maze_entries

def checkexit(matrix):
    if position[0] == len(matrix) - 1:
        return True
    else:
        return False

def check_magic_herb(matrix, postion):
    global age, age_catch, save

    if matrix[position[0]][position[1]] == 0:
        age_catch = age
        if age <= age_limit:
            save += 'S'
        else:
            save += 'N'
            
def route(matrix, position, path_traveled, age_limit, route_list):
    global age, entry_magic, entry_chosen

    if entry_magic == entry_chosen:
        pass
    else:
        age += matrix[position[0]][position[1]]

    if position[0] == len(matrix) - 1 and exit_maze == False:
        check_magic_herb(matrix, position)
        route_list.append('N')
        path_traveled.extend([[position[0], position[1]]])
        position.extend([position[0]-1, position[1]])
        del position[0:2]
    
    else:
        up = matrix[position[0]-1][position[1]] 
        down = matrix[position[0]+1][position[1]] 
        left = matrix[position[0]][position[1]-1] 
        right = matrix[position[0]][position[1]+1] 

        if up != -1 and [position[0]-1, position[1]] not in path_traveled:
            route_list.append('N')
            path_traveled.extend([[position[0], position[1]]])
            position.extend([position[0]-1, position[1]])
            del position[0:2]
        
        elif left != -1 and [position[0], position[1]-1] not in path_traveled:
            route_list.append('O')
            path_traveled.extend([[position[0], position[1]]])
            position.extend([position[0], position[1]-1])
            del position[0:2]
        
        elif right != -1 and [position[0], position[1]+1] not in path_traveled:
            route_list.append('L')
            path_traveled.extend([[position[0], position[1]]])
            position.extend([position[0], position[1]+1])
            del position[0:2]
        
        elif down != -1 and [position[0]+1, position[1]] not in path_traveled:
            route_list.append('S')
            path_traveled.extend([[position[0], position[1]]])
            position.extend([position[0]+1 , position[1]])
            del position[0:2]

    check_magic_herb(matrix, position)

cases = int(input())

for case in range(cases):
    age, age_limit = map(int, input().split())
    entry_magic, entry_chosen = map(int, input().split())
    lines, columns = map(int, input().split())
    maze = makematrix(lines,columns)
    maze_matrix(maze, lines, columns)
    maze = array(maze, dtype = int) #Converte a matriz para uma array 2D que pode ser manipulada pelo numpy e o dtype convert tudo que está dentro da matriz para inteiro
    position = [len(maze) - 1, entries(maze)[entry_chosen]]
    exit_maze = False
    route_list = ['N']
    path_traveled = []
    save = ''
    age_catch = 0
    
    while not exit_maze:
        route(maze, position, path_traveled, age_limit, route_list)
        exit_maze = checkexit(maze)

    if entry_magic != entry_chosen:
        age += maze[position[0]][position[1]] 
    
    route_list.append('S')
    print(*route_list)
    print(age, save, age_catch)