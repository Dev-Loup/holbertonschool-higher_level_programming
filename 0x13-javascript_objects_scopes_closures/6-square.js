#!/usr/bin/node
const Square = require('./5-square');
class SquareChar extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let ySiz = this.height; ySiz > 0; ySiz--) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareChar;
