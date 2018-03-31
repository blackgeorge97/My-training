let W = 600, H = 600

function renderToModel(renderCoordinates) {
    return new Vector(
        renderCoordinates.x / W,
        renderCoordinates.y / H
    )
}
function modelToRender(modelCoordinates) {
    return new Vector(
        modelCoordinates.x * W,
        modelCoordinates.y * H
    )
}
function initView() {
    canvas.width = W
    canvas.height = H
}
function render() {
    ctx.fillStyle = '#292d33'
    ctx.fillRect(0, 0, W, H)
    ctx.font = '48px Serif'
    ctx.fillStyle = 'white'
    
    if (typeof game === 'undefined') {
	ctx.fillText('Press Enter to start!', W / 4, 2 * H / 5, W / 2)
    }
    else if (game.gameOver) {
	if (game.winner === 'none') {
            ctx.fillText('How many players?', W / 4, 2 * H / 5, W / 2)
	    ctx.fillText('Press 1 or 2', W / 3, 4 * H / 5, W / 3)
	}
	else {
            ctx.fillText('The winner is ' + game.winner, W / 4, 2 * H / 5, W / 2)
	    ctx.fillText('Press 1 or 2 to play again.', W / 3, 4 * H / 5, W / 3)
	}
    }
    else {
        game.integrate()

        renderBall(ball)
        renderPaddles(player1, player2)
	ctx.fillText(player1.score + ' - ' + player2.score, 9 * W / 20, H / 12 , W / 10)
    }
    requestAnimationFrame(render)
}

function renderBall(ball) {
    const renderCoordinates = modelToRender(ball.position)

    ctx.fillStyle = 'red'
    ctx.beginPath()
    ctx.arc(
        Math.floor(renderCoordinates.x),
        Math.floor(renderCoordinates.y),
        Math.floor(ball.radius * W),
        0,
        2 * Math.PI
    )
    ctx.fill()
}

function renderPaddles(player1, player2) {
    const renderCoordinates1 = modelToRender(player1.paddle.position)
    const renderCoordinates2 = modelToRender(player2.paddle.position)

    ctx.fillStyle = 'white'
    ctx.fillRect(renderCoordinates1.x, renderCoordinates1.y, 
    W * player1.paddle.width, H * player1.paddle.height)

    ctx.fillRect(renderCoordinates2.x, renderCoordinates2.y,
    W * player2.paddle.width, H * player2.paddle.height)
}

initView()
render()
