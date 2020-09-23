#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const apiPeople = 'https://swapi-api.hbtn.io/api/people';
const people = '/18/';
let count = 0;
const options = {
  url: url,
  headers: {
    'User-Agent': 'Anakin'
  }
};
request.get(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const movies = JSON.parse(body).results;
  for (const movie of movies) {
    if (movie.characters.includes(apiPeople + people)) {
      count++;
    }
  }
  console.log(count);
});
