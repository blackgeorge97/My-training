from random import choice

I = [[1, 1, 1, 1], [0, 0, 0, 0]]
O = [[0, 1, 1, 0], [0, 1, 1, 0]]
T = [[1, 1, 1, 0], [0, 1, 0, 0]]
S = [[0, 1, 1, 0], [1, 1, 0, 0]]
Z = [[1, 1, 0, 0], [0, 1, 1, 0]]
J = [[1, 1, 1, 0], [0, 0, 1, 0]]
L = [[1 ,1, 1, 0], [1, 0, 0, 0]]
TETRIMINOES = {'I': I, 'O': O,'T': T, 'S': S, 'Z': Z, 'J': J, 'L': L}
MOVES = {'up' : [0, -1], 'down' : [0, 1], 'right' : [1, 0], 'left' : [-1, 0]}

def create_board(HOR_BOXES, VER_BOXES):
    board = [[0] * HOR_BOXES for _ in range(VER_BOXES)]
    return board

def create_tetrimino(board, HOR_BOXES, VER_BOXES):
    tetrimino = choice(list(TETRIMINOES.keys()))
    place = []
    for i in range(2):
        for j in range(int(HOR_BOXES / 2) - 2, int(HOR_BOXES / 2) + 2):
            if TETRIMINOES[tetrimino][i][j - int(HOR_BOXES / 2) + 2] == 1:
                place.append([i, j])
                board[i][j] = TETRIMINOES[tetrimino][i][j - int(HOR_BOXES / 2) + 2]
    return board, tetrimino, place

def move_tetrimino(board, move_dir, HOR_BOXES, VER_BOXES, place):
    if move_dir == 'none':
        return board ,place
    new_board = create_board(HOR_BOXES, VER_BOXES)
    new_place = []
    for box in place:
        x = box[1] + MOVES[move_dir][0]
        y = box[0] + MOVES[move_dir][1]
        if x not in range(HOR_BOXES) or y not in range(VER_BOXES):
            new_board.clear()
            new_place.clear()
            new_board = board
            new_place = place
            break
        new_place.append([y,x])
        new_board[y][x] = 1    
    return new_board, new_place

def new_game(HOR_BOXES, VER_BOXES):
    board = create_board(HOR_BOXES, VER_BOXES)
    board, tetrimino, place = create_tetrimino(board, HOR_BOXES, VER_BOXES)
    return board, tetrimino, place

def tetris(board, HOR_BOXES, VER_BOXES, move_dir, place):
    board, place = move_tetrimino(board, move_dir, HOR_BOXES, VER_BOXES, place)
    return board, place
