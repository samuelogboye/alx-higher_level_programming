#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line arguments
const contentToWrite = process.argv[3]; // Get the content to write from the command line arguments

fs.writeFile(filePath, contentToWrite, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
