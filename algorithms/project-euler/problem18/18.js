var fs = require('fs');
var contents = fs.readFileSync('pyramid.txt', 'utf8');

var lines = contents.split('\n');
var pyramid = []
for (var i = 0; i < lines.length; i++) { 
    numbers = lines[i].split(' ');
    for (j = 0; j < numbers.length; j++) {
        numbers[j] = parseInt(numbers[j])
    }
    pyramid.push(numbers);
}
    
for (var i = pyramid.length - 1; i; i--) {
    for (var j = 0; j < pyramid[i].length - 1; j++) {
        pyramid[i - 1][j] += Math.max(pyramid[i][j], pyramid[i][j + 1])
    }
}
console.log(pyramid[0][0])
