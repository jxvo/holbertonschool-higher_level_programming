#!/usr/bin/node
// Square class
class Square extends require('./4-rectangle.js') {
  // inherits size value from Rectangle
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
