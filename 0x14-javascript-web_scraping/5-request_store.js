#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const lorApi = process.argv[2];
const lorPath = process.argv[3];
const options = {
  url: lorApi,
  headers: {
    'User-Agent': 'Anakin'
  }
};
request.get(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(lorPath, body, function (errFile) {
    if (errFile) {
      console.log(errFile);
    }
  });
});
