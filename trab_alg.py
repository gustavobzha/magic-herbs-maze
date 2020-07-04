from numpy import array

def makematrix(matrix_lines,matrix_columns):
    matrix_local = [] 
    for lines in range(matrix_lines): 
        line = [None] * matrix_columns 
        matrix_local.append(line) 
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
    return position[0] == len(matrix) - 1

def check_magic_herb(matrix, position, age, age_catch, save):
    if matrix[position[0]][position[1]] == 0:
        age_catch = age 
        if age <= age_limit:
            save += 'S' 
        else:
            save += 'N' 
    return age_catch, save 

def route(matrix, position, path_traveled, age, age_limit, age_catch,
          route_list,  entry_magic, entry_chosen, save):
    if not entry_magic == entry_chosen: 
        age += matrix[position[0]][position[1]] 
    
    if position[0] == len(matrix) - 1:
        age_catch, save = check_magic_herb(matrix, position,
                                           age, age_catch, save) 
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

    age_catch, save = check_magic_herb(matrix, position, age, age_catch, save)
    return age, age_catch, save

cases = int(input()) 

for case in range(cases):
    age, age_limit = map(int, input().split()) 
    entry_magic, entry_chosen = map(int, input().split()) 
    lines, columns = map(int, input().split()) 
    maze = makematrix(lines,columns) 
    maze_matrix(maze, lines, columns) 
    maze = array(maze, dtype = int) 
    position = [len(maze) - 1, entries(maze)[entry_chosen]]
    exit_maze = False 
    route_list = ['N'] 
    path_traveled = [] 
    save = '' 
    age_catch = 0 
    
    while not exit_maze: 
        age, age_catch, save = route(maze, position, path_traveled, age,
                                     age_limit, age_catch, route_list,
                                     entry_magic, entry_chosen, save)
        exit_maze = checkexit(maze) 
    
    if entry_magic != entry_chosen: 
        age += maze[position[0]][position[1]] 
    
    route_list.append('S') 
    print(*route_list) 
    print(age, save, age_catch) 