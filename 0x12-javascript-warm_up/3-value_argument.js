#!/usr/bin/node
// This script prints the first argument passed to it
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('No argument');
}
if (myArgs.length > 0) {
  console.log(myArgs[0]);
}
