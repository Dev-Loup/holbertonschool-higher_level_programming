#!/usr/bin/node
const request = require('request');
const urlElement = process.argv[2];
request.get(urlElement, function (error, response) {
  if (error) {
    return console.log(error);
  }
  console.log('code: %d', response && response.statusCode);
});
