#!/usr/bin/node
const request = require('request');
const characterId = 18;
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch: ${response.statusCode}`);
  }
  if (body) {
    const movies = JSON.parse(body).results;
    let moviescount = 0;

    movies.forEach(movie => {
      const characters = movie.characters.map(character => parseInt(character.split('/').slice(-2)[0]));
      if (characters.includes(characterId)) {
        moviescount++;
      }
    });

    console.log(moviescount);
  }
});
