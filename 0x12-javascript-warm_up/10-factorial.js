#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));

function factorial (factor) {
  if (isNaN(factor) || factor === 1) {
    return 1;
  } else {
    return factor * factorial(factor - 1);
  }
}
