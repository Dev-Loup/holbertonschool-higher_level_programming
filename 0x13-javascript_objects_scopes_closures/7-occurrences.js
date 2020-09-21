#!/usr/bin/node

exports.nbOccurences = function nb0ccurences (list, searchElement) {
  let sum = 0;
  for (let iter = 0; iter < list.length; iter++) {
    if (list[iter] === searchElement) {
      sum++;
    }
  }
  return sum;
};
