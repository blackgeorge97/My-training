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
CENTER_HEIGHT = {'I': 0, 'O': 0,'T': 0, 'S': 1, 'Z': 1, 'J': 0, 'L': 0}

class Game:
    
    HOR_BOXES = 10
    VER_BOXES = 20
    START = True  
    
    def __init__(self):
        self.clear_board()
        self.place = []
        self.center = []
        self.tetromino = ''
        self.game_over = True
        self.deleted_lines = 0
        try:
            with open('highscore.txt', 'r') as f:
                self.highscore = int(f.read())
        except:
            self.highscore = 0
        self.score = 0  
    
    def is_game_over(self):
        self.game_over = True
        if self.highscore < self.score:
                self.beat_highscore = True
                self.highscore = self.score
                with open('highscore.txt', 'w') as f:
                    f.write(str(self.highscore))        
 
    def clear_board(self):
        self.board = [[0] * self.HOR_BOXES for _ in range(self.VER_BOXES)]

    def create_tetromino(self):
        self.tetromino = choice(list(TETROMINOES.keys()))
        self.center = [CENTER_HEIGHT[self.tetromino], int(self.HOR_BOXES / 2 - 1)]
        self.place = []
        i = 0
        for row in TETROMINOES[self.tetromino]:
            for j in range(int(self.HOR_BOXES / 2) - 2, int(self.HOR_BOXES / 2) + 2):
                if row[j - int(self.HOR_BOXES / 2) + 2] == 1:
                    if self.place_taken(j, i):
                        self.is_game_over()
                        self.START = False
                        break
                    self.place.append([i, j])
                    self.board[i][j] = row[j - int(self.HOR_BOXES / 2) + 2]
            i += 1
 
    def in_bounds(self, x, y):
        if x not in range(self.HOR_BOXES) or y not in range(self.VER_BOXES):
            return False
        return True
   
    def place_taken(self, x, y):
        if self.board[y][x] != 0 and self.board[y][x] != 1:
            return True
        return False
    
    def delete_line(self, line):
        self.board.remove(line)
        self.board.insert(0, [0] * self.HOR_BOXES)
    
    def stop(self): 
        for box in self.place:
            self.board[box[0]][box[1]] = self.tetromino
        for line in self.board:
            if line.count(0) == 0:
                self.delete_line(line)
                self.deleted_lines += 1
        self.place.clear()
        self.create_tetromino()
 
    def rotate(self):
        if self.tetromino == 'O':
            return
        new_place = []
        for box in self.place:
            x = self.center[1] + self.center[0] - box[0]
            y = self.center[0] - self.center[1] + box[1]
            if not self.in_bounds(x, y)  or self.place_taken(x, y):
                return
            new_place.append([y, x])
        for box in self.place:
            self.board[box[0]][box[1]] = 0
        for box in new_place:
            self.board[box[0]][box[1]] = 1
        self.place = new_place
        

    def move(self, direction):
            new_place = []
            for box in self.place:
                x = box[1] + MOVES[direction][0]
                y = box[0] + MOVES[direction][1]
                if not self.in_bounds(x, y)  or self.place_taken(x, y):
                    return False 
                new_place.append([y, x])
            self.center[0] += MOVES[direction][1]
            self.center[1] += MOVES[direction][0]
            for box in self.place:
                self.board[box[0]][box[1]] = 0
            for box in new_place:  
                self.board[box[0]][box[1]] = 1 
            self.place = new_place           
            return True

    def integrate(self):
        if self.game_over:
            if self.highscore < self.score:
                self.beat_highscore = True
                self.highscore = self.score
                with open('highscore.txt', 'w') as f:
                    f.write(str(self.highscore))
            return
        if len(self.place) == 0:
            self.create_tetromino()
            return
        self.beat_highscore = False 
        if not self.move('down'):
            self.stop()
            if self.deleted_lines != 0:
                current_score = 100
                for _ in range(self.deleted_lines):
                    current_score *= 2
                self.deleted_lines = 0
            else:
                current_score = 0
            self.score += current_score
