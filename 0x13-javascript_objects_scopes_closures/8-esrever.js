#!/usr/bin/node
// returns a reversed version of a list
exports.esrever = function (list) {
  const reversed = [];
  while (list.length) {
    reversed.push(list.pop());
  }
  return reversed;
};
