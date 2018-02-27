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
    integrate()

    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, W, H)

    renderBall(ball)
    renderVelocityLine(velocityLine)

    requestAnimationFrame(render)
}
function renderBall(ball) {
    if (typeof ball === 'undefined') {
        return
    }
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
function renderVelocityLine(velocityLine) {
    if (velocityLine == null) {
        return
    }
    const viewStart = modelToRender(velocityLine.start)
    const viewEnd = modelToRender(velocityLine.end)

    ctx.strokeStyle = 'blue'
    ctx.beginPath()
    ctx.moveTo(viewStart.x, viewStart.y)
    ctx.lineTo(viewEnd.x, viewEnd.y)
    ctx.stroke()
}

initView()
render()
