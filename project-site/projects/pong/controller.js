let canvas
let ctx
let game
let ball

function initController() {
    canvas = document.createElement('canvas')
    document.body.appendChild(canvas)
    ctx = canvas.getContext('2d')
    
    window.addEventListener('keydown', function(e){
	    if (game === undefined) {
		if (e.keyCode === 13) {
	            game = new Game()
		}
	    }   
	    else if (game.gameOver) {
	        if (e.keyCode === 49 || e.keyCode === 50) {
		    game.gameOver = false
                    player1 = new Player("Left")
                    player2 = new Player("Right")
                    ball = new Ball()
		    game.players = e.keyCode - 48
	            ball.startMove()
	        }
	    }
	    else if (e.key === 'w') {
	        player1.paddle.moveDirection = -1
	    }
	    else if (e.key === 's') {
		player1.paddle.moveDirection = 1
            }
	    else if (game.players === 2) {
	        if (e.key === 'ArrowUp') {
		    player2.paddle.moveDirection = -1
		}
	        else if (e.key === 'ArrowDown') { 
		    player2.paddle.moveDirection = 1
		}
	   }
    }, false);
    
     window.addEventListener('keyup', function(e){
        if (game !== undefined) {
            if (!game.gameOver) {
                if (e.key === 'w' && player1.paddle.moveDirection === -1) {
                    player1.paddle.moveDirection = 0
                }
                else if (e.key === 's' && player1.paddle.moveDirection === 1) {
                    player1.paddle.moveDirection = 0
                }
                if (game.players === 2) {
                    if (e.key === 'ArrowUp' && player2.paddle.moveDirection === -1) {
                        player2.paddle.moveDirection = 0
                    }
                    else if (e.key === 'ArrowDown' && player2.paddle.moveDirection === 1) {
                        player2.paddle.moveDirection = 0
                    }   
                }
            }
        }
    }, false);
}

initController()
