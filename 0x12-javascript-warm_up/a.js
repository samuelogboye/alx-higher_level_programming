#!/usr/bin/node
const a = [4, 2, 5, 3, 6, 7, 8, 4, 10, 9, 1];
// Sort the array in ascending order
a.sort(function (a, b) {
  return a - b;
});
console.log(a);
console.log(a[a.length - 2]);
