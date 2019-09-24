#!/usr/bin/node
// Rectangle class
class Rectangle {
  // creates empty object if invalid params passed
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

  // double the width and height values
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// Square class
class Square extends Rectangle {
  // inherits size value from Rectangle
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
