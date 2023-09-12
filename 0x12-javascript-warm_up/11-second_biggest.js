#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments.
const myArgs = process.argv.slice(2);
if (myArgs.length < 2) {
  console.log(0);
} else {
  myArgs.sort(function (a, b) {
    return a - b;
  });
  console.log(myArgs[myArgs.length - 2]);
}
