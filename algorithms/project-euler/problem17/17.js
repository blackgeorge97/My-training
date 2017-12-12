const LIMIT = 1000;
const HUNDRED = 7;

var arrayones = [ 3, 3, 5, 4, 4, 3, 5, 5, 4 ];
var arrayteens = [ 6, 6, 8, 8, 7, 7, 9, 8, 8 ];
var arraytens = [ 3, 6, 6, 5, 5, 5, 7, 6, 6 ];

function sum100(i){
    var count = 0
    if (i == 0){
        return count}
    if (i > 0 && i < 10){
        count =  arrayones[i - 1]}
    else if (i > 10 && i < 20){
        count = arrayteens[i % 10 - 1]}
    else if (i % 10 == 0){
        count = arraytens[parseInt(i / 10 - 1)]}
    else{
        count = arraytens[parseInt(i / 10 - 1)] + arrayones[i % 10 - 1]}
    return count
    }

var sum = 11;
for (var i = 1; i < LIMIT; i++){
    if (i < 100){
        sum += sum100(i)}
    else if (i % 100 == 0){
        sum += arrayones[parseInt(i / 100 - 1)] + HUNDRED}
    else{
        sum += 3 + sum100(i % 100) + arrayones[parseInt(i / 100 - 1)] + HUNDRED}
    }

console.log(sum)   
