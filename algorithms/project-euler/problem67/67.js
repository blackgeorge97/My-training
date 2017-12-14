var fs = require('fs');
var contents = fs.readFileSync('triangle.txt', 'utf8');

var lines = contents.split('\n');
var triangle = []
for (var i = 0; i < lines.length; i++) { 
    numbers = lines[i].split(' ');
    for (j = 0; j < numbers.length; j++) {
        numbers[j] = parseInt(numbers[j])
    }
    triangle.push(numbers);
}
    
for (var i = triangle.length - 1; i; i--) {
    for (var j = 0; j < triangle[i].length - 1; j++) {
        triangle[i - 1][j] += Math.max(triangle[i][j], triangle[i][j + 1])
    }
}
console.log(triangle[0][0])
