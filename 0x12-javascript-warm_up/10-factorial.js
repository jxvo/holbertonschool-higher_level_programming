#!/usr/bin/node

function fact (x) {
  if (x === 0) {
    return 1;
  }
  return x * fact(x - 1);
}
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log(1);
} else {
  console.log(fact(x));
}
