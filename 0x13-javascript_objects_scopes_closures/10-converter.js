#!/usr/bin/node
// converts a number from base 10 to base passed as parameter
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
