#!/usr/bin/node
// a script that imports an array and computes a new array.
const list = require('./100-data').list;
const newList = list.map((x, index) => x * index);
console.log(list);
console.log(newList);
