#!/usr/bin/node
// prints number of arguments already printed and new argument value
exports.logMe = function (item) {
  if (typeof exports.logMe.count === 'undefined') {
    exports.logMe.count = 0;
  } else {
    exports.logMe.count += 1;
  }
  console.log(exports.logMe.count + ': ' + item);
};
