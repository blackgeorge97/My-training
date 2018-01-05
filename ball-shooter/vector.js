class Vector {
    constructor(x, y) {
        this.x = x
        this.y = y
    }
    minus(other) {
        return new Vector(
            this.x - other.x,
            this.y - other.y
        )
    }
    scale(lambda) {
        return new Vector(
            lambda * this.x,
            lambda * this.y
        )
    }
}
