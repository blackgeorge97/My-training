let canvas
let ctx
let ball
let velocityLine = null

function initController() {
    canvas = document.createElement('canvas')
    document.body.appendChild(canvas)
    ctx = canvas.getContext('2d')
    
    function bodyToCanvas(bodyCoordinates) {
        return new Vector(
            bodyCoordinates.x - canvas.offsetLeft,
            bodyCoordinates.y - canvas.offsetTop
        )
    }
    
    function onlyLeftMouseButton(f) {
        return (e) => {
            if (e.button != 0) {
                return
            }
            f(e)
        }
    }
    function inModelBase(f) {
        return (e) => {
            let bodyCoordinates = new Vector(e.clientX, e.clientY)
            let canvasCoordinates = bodyToCanvas(bodyCoordinates)
            let modelCoordinates = renderToModel(canvasCoordinates)

            f(modelCoordinates)
        }
    }

    canvas.addEventListener('mousedown',
        onlyLeftMouseButton(
            inModelBase(
                (modelCoordinates) => {
                    ball = new Ball()
                    ball.position = modelCoordinates

                    velocityLine = new VelocityLine()
                    velocityLine.start = modelCoordinates
                    velocityLine.end = modelCoordinates
                }
            )
        )
    ) 
    canvas.addEventListener('mousemove',
        onlyLeftMouseButton(
            inModelBase(
                (modelCoordinates) => {
                    if (velocityLine != null) {
                        velocityLine.end = modelCoordinates
                    }
                }
            )
        )
    )
    canvas.addEventListener('mouseup',
        onlyLeftMouseButton(
            inModelBase(
                (modelCoordinates) => {
                    const SLOWDOWN = 0.1
                    ball.moving = true
                    ball.velocity = modelCoordinates.minus(ball.position).scale(SLOWDOWN)
                    velocityLine = null
                }
            )
        )
    )
}

initController()
