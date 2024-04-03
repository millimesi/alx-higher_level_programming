#!/usr/bin/node
const request = require('request');
const moviesId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${moviesId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const movies = JSON.parse(body);
    const charactersUrls = movies.characters;

    const fetchAndPrintCharacter = (url) => {
      request(url, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status Code:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };
    charactersUrls.forEach(characterUrl => {
      fetchAndPrintCharacter(characterUrl);
    });
  }
});
