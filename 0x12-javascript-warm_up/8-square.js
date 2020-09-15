#!/usr/bin/node
let siz;
let ySiz;

if (isNaN(siz = parseInt(process.argv[2]))) {
  console.log('Missing size');
}
for (ySiz = siz; ySiz > 0; ySiz--) {
  console.log('X'.repeat(siz));
}
