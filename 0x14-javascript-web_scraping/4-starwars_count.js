#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const people = '18';
let count = 0;
const options = {
  url: url,
  headers: {
    'User-Agent': 'Anakin'
  }
};
request.get(options, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movies = JSON.parse(body).results;
  for (const movie of movies) {
    for (const character of movie.characters) {
      if (character.includes(people)) {
        count++;
      }
    }
  }
  console.log(count);
});
