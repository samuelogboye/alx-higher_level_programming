#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error); // Handle request errors
  } else {
    console.log('code:', response && response.statusCode); // Print the response status code if a response was received
  }
});
