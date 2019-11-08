#!/usr/bin/node

const len = process.argv.length;
if (process.argv[2] === undefined) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let index = len; index > 2; index--) {
    arr.push(parseInt(process.argv[index - 1]));
  }
  arr.sort((left, right) => left - right);
  const ret = len - 4;
  console.log(arr[ret]);
}
