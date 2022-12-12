class Room:
    contacts = []
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

maze = []

for columnI in range(0, 5):
    maze.append([])
    for rowI in range(0, 5):
        room = Room(columnI, rowI)
        maze[columnI].append(room)
    
for x, column in enumerate(maze):
    for y, room in enumerate(column):
        room.contacts.append('' if x >= len(maze) - 1 else maze[x + 1])
        room.contacts.append('' if y <= 0 else maze[y - 1])
        room.contacts.append('' if x <= 0 else maze[x - 1])
        room.contacts.append('' if y >= len(column) - 1 else maze[y + 1])