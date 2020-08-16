class Person:
    def __init__(self, age, age_limit, entry_chosen):
        self.age = age
        self.age_limit = age_limit
        self.entry_chosen = entry_chosen
        self.age_catch = 0
        self.position = []
        self.path = ['N']
        self.traveled = []
        self.mission = ''

    def path_traveled(self, maze, entry_magic):
        if not entry_magic == self.entry_chosen:
            self.age += maze[self.position[0]][self.position[1]]

        if self.position[0] == len(maze) - 1:
            self.check_magic_herb(maze[self.position[0]][self.position[1]])
            self.path.append('N')
            current_position = [self.position[0], self.position[1]]
            new_position = [self.position[0]-1, self.position[1]]
            self.update_path(current_position, new_position)
        
        else:
            maze_up = maze[self.position[0]-1][self.position[1]]
            maze_down = maze[self.position[0]+1][self.position[1]]
            maze_left = maze[self.position[0]][self.position[1]-1]
            maze_right = maze[self.position[0]][self.position[1]+1]
            position_up = [self.position[0]-1, self.position[1]]
            position_down = [self.position[0]+1, self.position[1]]
            position_left = [self.position[0], self.position[1]-1]
            position_right = [self.position[0], self.position[1]+1]
            current_position = [self.position[0], self.position[1]]

            if maze_up != -1 and position_up not in self.traveled:
                self.path.append('N')
                self.update_path(current_position, position_up)
                
            elif maze_down != -1 and position_down not in self.traveled:
                self.path.append('S')
                self.update_path(current_position, position_down)

            elif maze_left != -1 and position_left not in self.traveled:
                self.path.append('O')
                self.update_path(current_position, position_left)

            elif maze_right != -1 and position_right not in self.traveled:
                self.path.append('L')
                self.update_path(current_position, position_right)
                
        self.check_magic_herb(maze[self.position[0]][self.position[1]])

    def check_magic_herb(self, position):
        if position == 0:
            self.age_catch = self.age
            if self.age <= self.age_limit:
                self.mission = 'S'
            else:
                self.mission = 'N'

    def update_path(self, current_pos, new_pos):
        self.traveled.extend([current_pos])
        self.position.extend(new_pos)
        del self.position[0:2]

class Maze:
    def __init__(self, rows, columns, entry_magic):
        self.rows = rows
        self.columns = columns
        self.entry_magic = entry_magic
        self.map = []
        self.maze_entries = {}

    def build_maze(self):
        for row in range(self.rows):
            line = [None] * self.columns
            self.map.append(line)

        for row in range(self.rows):
            local_row = input().split()
            for column in range(self.columns):
                self.map[row][column] = int(local_row[column])

    def find_entries(self):
        entry = 1
        for index, value in enumerate(self.map[len(self.map) - 1]):
            if value != -1:
                self.maze_entries[entry] = index
                entry += 1
        return self.maze_entries

def checkexit(maze, position):
    return position[0] == len(maze) -1

for case in range(int(input())):
    age, age_limit = map(int, input().split())
    entry_magic, entry_chosen = map(int, input().split())
    rows, columns = map(int, input().split())

    person1 = Person(age, age_limit, entry_chosen)
    maze1 = Maze(rows, columns, entry_magic)

    maze1.build_maze()
    person1.position = [len(maze1.map) - 1, maze1.find_entries()[entry_chosen]]

    while True:
        person1.path_traveled(maze1.map, entry_magic)
        if checkexit(maze1.map, person1.position): break

    if entry_magic != entry_chosen:
        person1.age += maze1.map[person1.position[0]][person1.position[1]]

    person1.path.append('S')
    print(*person1.path)
    print(person1.age, person1.mission, person1.age_catch)