#!/usr/bin/node

const a = parseInt(process.argv[2]);

if (isNaN(a) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    let anew = '';
    for (let i = 0; i < process.argv[2]; i++) {
      anew += 'X';
    }
    console.log(anew);
  }
}
