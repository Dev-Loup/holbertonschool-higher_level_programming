#!/usr/bin/node
exports.esrever = function (list) {
  let listRev = [];
  for (let iter = list.length - 1; iter >= 0; iter--) {
    listRev.push(list[iter]);
  }
  return listRev;
}