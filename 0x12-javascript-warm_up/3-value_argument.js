#!/usr/bin/node
// This script prints the first argument passed to it
// without using lenght
const myArgs = process.argv.slice(2);
if (myArgs[0] === undefined) {
  console.log('No argument');
}
if (myArgs[0] !== undefined) {
  console.log(myArgs[0]);
}
