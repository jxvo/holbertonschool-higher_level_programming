#!/usr/bin/node
// return the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (index) {
    if (index === searchElement) {
      count += 1;
    }
  });
  return count;
};
