#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch: ${response.statusCode}`);
  }
  if (body) {
    const bodyJson = body;
    const bodyObj = JSON.parse(bodyJson);
    console.log(bodyObj.title);
  }
});
