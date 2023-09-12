#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments.
const myArgs = process.argv.slice(2);
if (myArgs.length < 2) {
  console.log(0);
} else {
  console.log(myArgs.sort()[myArgs.length - 2]);
}
