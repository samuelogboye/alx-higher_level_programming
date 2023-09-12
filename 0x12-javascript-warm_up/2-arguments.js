#!/usr/bin/node
// This script prints a message depending of the number of arguments passed
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('No argument');
}
if (myArgs.length === 1) {
  console.log('Argument found');
}
if (myArgs.length > 1) {
  console.log('Arguments found');
}
