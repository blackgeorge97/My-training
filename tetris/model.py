from random import choice

I = [[1, 1, 1, 1], 
     [0, 0, 0, 0]]
O = [[0, 1, 1, 0], 
     [0, 1, 1, 0]]
T = [[1, 1, 1, 0], 
     [0, 1, 0, 0]]
S = [[0, 1, 1, 0], 
     [1, 1, 0, 0]]
Z = [[1, 1, 0, 0],  
     [0, 1, 1, 0]]
J = [[1, 1, 1, 0], 
     [0, 0, 1, 0]]
L = [[1 ,1, 1, 0],  
     [1, 0, 0, 0]]
TETROMINOES = {'I': I, 'O': O,'T': T, 'S': S, 'Z': Z, 'J': J, 'L': L}
MOVES = {'down': [0, 1], 'right': [1, 0], 'left': [-1, 0]}

class Game:
    
    HOR_BOXES = 10
    VER_BOXES = 20
    
    def __init__(self):
        self.board = [[0] * self.HOR_BOXES for _ in range(self.VER_BOXES)]
        self.place = []

    def create_tetromino(self):
        self.tetromino = choice(list(TETROMINOES.keys()))
        self.place = []
        for i in range(2):
            for j in range(int(self.HOR_BOXES / 2) - 2, int(self.HOR_BOXES / 2) + 2):
                if TETROMINOES[self.tetromino][i][j - int(self.HOR_BOXES / 2) + 2] == 1:
                    self.place.append([i, j])
                    self.board[i][j] = TETROMINOES[self.tetromino][i][j - int(self.HOR_BOXES / 2) + 2]
    
    def stop(self): 
        for box in self.place:
            self.board[box[0]][box[1]] = self.tetromino
        self.place.clear()
        self.create_tetromino()
 
    def rotate(self):
        pass
     
    def move(self, direction):
        if direction != 'none':
            if direction == 'up':
                self.rotate() 
            else:
                new_place = []
                for box in self.place:
                    x = box[1] + MOVES[direction][0]
                    y = box[0] + MOVES[direction][1]
                    if x not in range(self.HOR_BOXES) or y not in range(self.VER_BOXES) or self.board[y][x] != 0 and self.board[y][x] != 1:
                        break      
                    new_place.append([y, x])
                if len(new_place) == len(self.place):
                    for box in self.place:
                        self.board[box[0]][box[1]] = 0
                    for box in new_place:  
                        self.board[box[0]][box[1]] = 1 
                    self.place = new_place           
 
    def integrate(self):
        if len(self.place) == 0:
            self.create_tetromino()
        else:
            for box in self.place:
                if box[0] + 1 > self.VER_BOXES - 1 or self.board[box[0] + 1][box[1]] != 0 and self.board[box[0] + 1][box[1]] != 1:
                    self.stop()     
                    break 
            else:
                self.move('down')
