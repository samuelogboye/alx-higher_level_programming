#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js
const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      console.log(c.repeat(this.width));
    }
  }
};
