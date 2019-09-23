#!/usr/bin/node
/* create an empty object when invalid parameters passed */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const symbol = 'X';
    for (let line = 0; line < this.height; line++) {
      console.log(symbol.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
