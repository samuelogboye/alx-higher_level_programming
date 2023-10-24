#!/usr/bin/node

const request = require("request");

const completedTasks = {};

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const user of data) {
      if (user.completed === true) {
        if (user.userId in completedTasks) {
          completedTasks[user.userId]++;
        } else {
          completedTasks[user.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.log(error);
  }
});
