let randomNum
let percentAngle
let relativePosition
let angle

class Game {
    constructor() {
        this.gameOver = true
	this.players = 0
	this.winner = 'none'
	this.frames = 0
    }
    
    integrate() {
        if (this.gameOver) {
	    return
        }
	if (ball.position.y + ball.radius > 1 
	|| ball.position.y - ball.radius < 0) {
	    ball.velocity.y *= -1
	}
	if (ball.position.x - ball.radius <= player1.paddle.width) {
            if (!player1.touchBall()) {
		if (ball.position.x - ball.radius <= 0) {
                    player2.score +=1
		    ball.position = new Vector(0.5, 0.5)
                    ball.startMove()
		    player1.paddle = new Paddle('Left')
                    player2.paddle = new Paddle('Right')
		    if (player2.score === 10) {
		        this.winner = "Player 2"
		        this.gameOver = true
		        return
	 	    }
	        }
            }
        }
	if (ball.position.x + ball.radius >= 1 - player2.paddle.width) {
            if (!player2.touchBall()) {
		if (ball.position.x + ball.radius >= 1) {
                    player1.score += 1
       		    ball.position = new Vector(0.5, 0.5)
                    ball.startMove()
		    player1.paddle = new Paddle('Left')
                    player2.paddle = new Paddle('Right')
                    if (player1.score === 10) {
                        this.winner = "Player 1"
                        this.gameOver = true
		        return
                    }
                }
	    }
        }
	if (this.players === 1) {
	    if (this.frames % 15 === 0) {
	        if (player2.paddle.position.y + player2.paddle.height / 2 > ball.position.y
		    && ball.velocity.y < 0) {
                    player2.paddle.moveDirection = -1
	        }
	        else if (player2.paddle.position.y + player2.paddle.height / 2 < ball.position.y
		         && ball.velocity.y > 0) {
	            player2.paddle.moveDirection = 1
	        }
	        else {
	            player2.paddle.moveDirection = 0
	        }
	    }
	}
	ball.position.x += ball.velocity.x 
	ball.position.y += ball.velocity.y 
	player1.paddle.movePaddle()
	player2.paddle.movePaddle()
	this.frames += 1
	if (this.frames === 15) {
	    this.frames = 0
	}
    }
    
}

class Player {
    constructor(side) {
        this.score = 0
        this.side = side
	this.paddle = new Paddle(side)
    }
    
    touchBall() {
        if (ball.position.y + ball.radius >= this.paddle.position.y
        && ball.position.y - ball.radius <= this.paddle.position.y + this.paddle.height) {
	    relativePosition = (ball.position.y - this.paddle.position.y
                             - this.paddle.height / 2)
	    percentAngle = relativePosition / this.paddle.height / 2
	    angle = (2 * Math.PI - Math.PI / 2)  * percentAngle
	    ball.velocity.x = Math.cos(angle) * ball.totalSpeed
	    ball.velocity.y = Math.sin(angle) * ball.totalSpeed
	    if (this.side === 'Right') {
	        ball.velocity.x *= -1
	    }
	    return true
	}
        else {
            return false
        }
    }
}

class Ball {
    constructor() {
        this.position = new Vector(0.5, 0.5)
	this.totalSpeed = 0.015
	this.velocity = new Vector(0, 0)
	this.radius = 0.015
    }
    startMove() {
	randomNum = Math.floor(Math.random() * 2)
        if (randomNum === 0) {
	    ball.velocity.x = ball.totalSpeed
        }
        else {
            ball.velocity.x = ball.totalSpeed * -1
        }
	ball.velocity.y = 0
    }
}

class Paddle {
    constructor(side) {
        this.height = 0.15
	this.width = 0.02
        this.position = new Vector(0.5, 0.5 - this.height / 2)
	this.pickSide(side)
	this.moveDirection = 0
	this.speed = 0.012
    }
    pickSide(side) {
        if (side === "Right") {
            this.position.x = 1 - this.width
        }
        else if (side === "Left") {
            this.position.x = 0
        }
    }

    movePaddle() {
	if (this.moveDirection === -1 && this.position.y <= 0) {
	    return 
	}
        if (this.moveDirection === 1 && this.position.y + this.height >= 1) {
            return 
        }
	this.position.y += this.moveDirection * this.speed
    }
}
