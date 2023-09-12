#!/usr/bin/node
// This script prints a square
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('Missing size');
}
if (myArgs[0] !== undefined) {
  for (let i = 0; i < myArgs[0]; i++) {
    console.log('X'.repeat(myArgs[0]));
  }
}
