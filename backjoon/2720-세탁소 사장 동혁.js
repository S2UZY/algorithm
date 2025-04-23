const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split('\n');
const c = input.map((value)=> parseInt(value));

let money = [ 0, 0, 0, 0 ];

for (let i=1; i<=c[0]; i++){
    money = [0,0,0,0];
    let cur = c[i];

    money[0] = Math.floor(cur/25);
    cur = cur%25;
    money[1] = Math.floor(cur/10);
    cur = cur%10;
    money[2] = Math.floor(cur/5);
    cur = cur%5;
    money[3] = Math.floor(cur/1);
    cur = cur%1;

    console.log(...money);
}