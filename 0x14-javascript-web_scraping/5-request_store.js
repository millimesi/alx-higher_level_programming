#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filepath = process.argv[3];
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch: ${response.statusCode}`);
  }
  if (body) {
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
