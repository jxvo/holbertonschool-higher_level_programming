#!/usr/bin/node
// Square class
class Square extends require('./5-square.js') {
  // prints a visual representation made from 'c'
  charPrint(c) {
    if (c === undefined) {
      super.print();
    } else {
      const symbol = c;
      for (let line = 0; line < this.height; line++) {
	console.log(symbol.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
