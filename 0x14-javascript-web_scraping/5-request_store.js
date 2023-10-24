#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// More efficient way:
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

// Less Efficient for large content, because it was first loaded into memory
// request(process.argv[2], (error, response, body) => {
//   if (!error && response.statusCode === 200) {
//     fs.writeFile(process.argv[3], body, "utf8", (error) => {
//       if (error) {
//         console.log(error);
//       }
//     });
//   }
// });
