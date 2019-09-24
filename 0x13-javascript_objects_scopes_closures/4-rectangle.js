#!/usr/bin/node
/* Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print a visual representation to stdout
  print () {
    const symbol = 'X';
    for (let line = 0; line < this.height; line++) {
      console.log(symbol.repeat(this.width));
    }
  }

  // switch height and width values
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
