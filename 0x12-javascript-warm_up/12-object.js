#!/usr/bin/node
let first = 0;
let second;
let siz = process.argv.length;

if (siz < 4) {
  second = first;
} else {
  for (; siz > 4; siz--) {
    if (parseInt(process.argv[siz - 1]) > first) {
      second = first;
      first = parseInt(process.argv[siz - 1]);
      console.log(second + ' y ' + first + siz);
    }
  }
}
console.log(second);
