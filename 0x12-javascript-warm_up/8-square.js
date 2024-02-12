#!/usr/bin/node
const multi = parseInt(process.argv[2]);
if (!multi) {
  console.log('Missing size');
} else {
  for (let i = 0; i < multi; i++) {
    let row = '';
    for (let j = 0; j < multi; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
