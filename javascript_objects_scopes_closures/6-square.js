#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let k = 0; k < this.height; k++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
