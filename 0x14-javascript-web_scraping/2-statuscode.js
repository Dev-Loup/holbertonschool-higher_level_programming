#!/usr/bin/node
const request = require('request');
const urlElement = process.argv[2];
request(urlElement, function (error, response) {
  if (error) {
    console.error(error);
  }
  console.log('code: ', response && response.statusCode);
});
