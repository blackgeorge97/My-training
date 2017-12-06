MOVES = {'right': 1, 'left': -1, 'none': 0}

class Game:
    W = 600
    H = 600
    BALL_R = int(H / 100) 
    PADDLE_W = int(W / 5)
    PADDLE_H = int(H / 100)
    PADDLE_Y = H - PADDLE_H
    X_RECTS = 10
    Y_RECTS = 6 
    RECT_W = int(W / X_RECTS)
    RECT_H = int(H * 30 / 100 / Y_RECTS)
    BALL_SPEED = 6
    PADDLE_SPEED = 2 * BALL_SPEED

    def __init__(self):
        self.start = True
        self.game_over = True
    
    def create_peaces(self):
        self.peace_places = [[i, j] for i in range(self.X_RECTS) for j in range(self.Y_RECTS)]

    def start_game(self):
        self.win = False
        self.start = False
        self.paddle_x = int(self.W / 2 - self.PADDLE_W / 2)
        self.ball_x = int(self.W / 2)
        self.ball_y = self.PADDLE_Y - self.BALL_R
        self.ball_change_x = 0
        self.ball_change_y = 0
        self.paddle_change = 0
        self.create_peaces()
        self.game_over = False
 
    def touch_peace(self):
        move_change_y = False
        move_change_x = False
        for peace in self.peace_places:
            if self.ball_x in range(peace[0] * self.RECT_W, (peace[0] + 1) * self.RECT_W + 1):
                if self.ball_y in range(peace[1] * self.RECT_H - self.BALL_R, (peace[1] + 1) * self.RECT_H + self.BALL_R + 1):
                    if not move_change_y:
                        self.ball_change_y *= -1
                        move_change_y = True
                    self.peace_places.remove(peace)
            elif self.ball_y in range(peace[1] * self.RECT_H, (peace[1] + 1) * self.RECT_H + 1):
                if self.ball_x in range(peace[0] * self.RECT_W - self.BALL_R, (peace[0] + 1) * self.RECT_W + self.BALL_R + 1):
                    if not move_change_x:
                        self.ball_change_x *= -1
                        move_change_x = True
                    self.peace_places.remove(peace)
                    
    def read_input(self, input):
        if self.game_over:
            if input == 'space':
                self.start_game()
            return
        if input == 'up' and self.ball_change_y == 0:
            self.ball_change_y = self.BALL_SPEED * -1
        try:
            self.paddle_change = MOVES[input] * self.PADDLE_SPEED
        except: 
            pass
        if self.paddle_x + self.paddle_change in range(0, self.W - self.PADDLE_W + 1):
            self.paddle_x += self.paddle_change
 
    def integrate(self):
        if self.game_over:
            return
        if self.ball_change_y == 0:
            self.ball_change_x = int(self.paddle_change / 2)
            self.ball_x = self.paddle_x + int(self.PADDLE_W / 2)
            return
        self.ball_x += self.ball_change_x
        self.ball_y += self.ball_change_y
        if self.ball_x - self.BALL_R <= 0 or self.ball_x >= self.W - self.BALL_R:
            self.ball_change_x *= -1
        if self.ball_y - self.BALL_R <= 0:
            self.ball_change_y *= -1
        elif self.ball_y >= self.PADDLE_Y + self.BALL_R:
            if self.ball_x in range(self.paddle_x, self.paddle_x + self.PADDLE_W + 1):
                self.ball_change_y *= -1
                if self.paddle_change != 0:
                    self.ball_change_x = int(self.paddle_change / 2)
            elif self.ball_y >= self.H - self.BALL_R:
                self.game_over = True
        self.touch_peace() 
        if self.peace_places == []:
            self.win = True
            self.game_over = True  
