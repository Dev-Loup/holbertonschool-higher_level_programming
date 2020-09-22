#!/usr/bin/node
const request = require('request');
const urlElement = process.argv[2];
request(urlElement, function (error, response) {
  if (error) {
    return console.log(error);
  }
  console.log('code: ', response && response.statusCode);
});
