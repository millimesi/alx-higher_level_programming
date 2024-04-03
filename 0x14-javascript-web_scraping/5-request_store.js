#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, function (err) {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
