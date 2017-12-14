const LIMIT = 1000;
const LETTERS_OF_AND = 3;
const LETTERS_OF_HUNDRED = 7;
const LETTERS_OF_ONE_THOUSAND = 11;

var letters_of_ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4];
var letters_of_teens = [6, 6, 8, 8, 7, 7, 9, 8, 8];
var letters_of_tens = [3, 6, 6, 5, 5, 5, 7, 6, 6];

function sum100(i) {
    var count = 0
    if (i == 0) {
        return count
    }
    if (i > 0 && i < 10) {
        count =  letters_of_ones[i]
    }
    else if (i > 10 && i < 20) {
        teens_number = i % 10
        count = letters_of_teens[teens_number - 1]
    }
    else {
        tens_number = parseInt(i / 10)
        ones_number = i % 10
        count += letters_of_tens[tens_number - 1] + letters_of_ones[ones_number]
    }
    return count
}

var sum = LETTERS_OF_ONE_THOUSAND;
for (var i = 1; i < LIMIT; i++) {
    if (i < 100) {
        sum += sum100(i)
    }
    else {
        hundreds_number = parseInt(i / 100)
        sum += letters_of_ones[hundreds_number] + LETTERS_OF_HUNDRED
        if (i % 100 != 0) {
            rest_number = i % 100
            sum += LETTERS_OF_AND + sum100(rest_number)
        }
    }    
}

console.log(sum)   
