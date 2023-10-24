#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const characterUrl of data.characters) {
      try {
        const characterResponse = await makeRequest(characterUrl);
        const characterData = JSON.parse(characterResponse);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
});

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}
