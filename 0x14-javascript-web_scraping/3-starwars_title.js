#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + episode,
  headers: {
    'User-Agent': 'Anakin'
  }
};
request.get(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log(JSON.parse(body).title);
});
