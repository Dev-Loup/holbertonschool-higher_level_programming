#!/usr/bin/node
const cLang = 'C is fun';
let iter;

if (isNaN(iter = parseInt(process.argv[2]))) {
  console.log('Missing number of ocurrences');
}
for (; iter > 0; iter--) {
  console.log(cLang);
}
