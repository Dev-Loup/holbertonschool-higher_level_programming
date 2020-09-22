#!/usr/bin/node
let path = process.argv[2];
if (typeof path === 'undefined') {
  path = '';
}
var fs = require('fs');
fs.readFile(path, 'utf-8', function (data) {
  console.log(data);
});