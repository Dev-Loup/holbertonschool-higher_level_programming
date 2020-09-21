#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = typeof c !== 'undefined' ? c : 'X';
    for (let ySiz = this.height; ySiz > 0; ySiz--) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
