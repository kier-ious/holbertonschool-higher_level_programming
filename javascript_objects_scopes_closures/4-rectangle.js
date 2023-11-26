#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // swapping the width and height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // multiply th ew and h of rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
