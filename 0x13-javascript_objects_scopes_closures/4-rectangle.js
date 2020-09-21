#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ySiz = this.height; ySiz > 0; ySiz--) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rotator = this.height;
    this.height = this.width;
    this.width = rotator;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
