#!/usr/bin/node
// This script prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
// If the argument can’t be converted to an integer, print “Not a number”

const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgs[0]));
}
