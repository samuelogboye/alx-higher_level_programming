#!/usr/bin/node
// This script computes and prints a factorial
const myArgs = process.argv.slice(2);
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(parseInt(myArgs[0])));
