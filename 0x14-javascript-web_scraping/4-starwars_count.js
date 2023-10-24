#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

let number = 0;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    for (let i = 0; i < data.results.length; i++) {
      if (
        data.results[i].characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/'
        )
      ) { number += 1; }
    }
    console.log(number);
  }
});
