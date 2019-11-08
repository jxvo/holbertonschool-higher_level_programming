#!/usr/bin/node

module.exports = {
  callMeMoby: function (x, theFunction) {
    for (let n = 0; n < x; n++) {
      theFunction();
    }
  }
};
