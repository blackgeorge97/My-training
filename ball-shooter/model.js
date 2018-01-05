function integrate() {
    const dt = 1
    const percVelLose = 10
    const g = 0.001
    const friction = 0.00001
    
    if (typeof ball === 'undefined') {
        return
    }
    if (!ball.moving) {
        return
    }
    if (!ball.stopY && ball.velocity.y + ball.radius <= 1) {
        ball.velocity.y += g * dt
    }
    else if (ball.velocity.y >= 0) {
        ball.stopY = true
        ball.position.y = 1 - ball.radius
        ball.velocity.y = 0
    }
    if (ball.velocity.y + ball.radius <= 1) {
        ball.velocity.y += g * dt
        if (ball.velocity.x > 0) {
            ball.velocity.x -= friction * dt
        }  
        else if (ball.velocity.x < 0){
            ball.velocity.x += friction * dt
        }
    }
    ball.position.x += ball.velocity.x * dt
    ball.position.y += ball.velocity.y * dt  
    if (ball.position.x + ball.radius > 1
     || ball.position.x - ball.radius < 0) {
        if (!ball.changeX) {
            ball.changeX = true
            ball.velocity.x = -ball.velocity.x * (100 - percVelLose) / 100
        } 
    }
    else {
        ball.changeX = false
    }
    if (ball.position.y + ball.radius > 1
     || ball.position.y - ball.radius < 0) {
        if (!ball.changeY) {
            ball.changeY = true
            ball.velocity.y = -ball.velocity.y * (100 - percVelLose) / 100
        }
    }
    else {
        ball.changeY = false 
    }  
}

class Ball {
    constructor() {
        this.moving = false 
        this.changeX = false
        this.changeY = false
        this.stopY = false
        this.position = new Vector(0.5, 0.5)
        this.velocity = new Vector(0, 0)
        this.radius = 0.02
    }
}

class VelocityLine {
    constructor() {
        this.start = new Vector(0, 0)
        this.end = new Vector(0, 0)
    }
}
