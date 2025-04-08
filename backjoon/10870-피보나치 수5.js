const fs = require('fs');
const input = parseInt(fs.readFileSync(__dirname + '/input.txt'));


let result = Array(input+2);
result[0] = 0
result[1] = 1


for (let i=0; i<input; i++) {
   result[i+2] = result[i] + result[i+1]
}

console.log(result[input])

