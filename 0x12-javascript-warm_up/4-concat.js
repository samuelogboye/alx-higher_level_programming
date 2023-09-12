#!/usr/bin/node
// This script prints two arguments passed to it, in the following format: “ is ”
const myArgs = process.argv.slice(2);
console.log(myArgs[0] + ' is ' + myArgs[1]);
