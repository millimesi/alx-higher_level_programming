#!/usr/bin/node
const multi = parseInt(process.argv[2]);
if (!multi) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < multi; i++) {
    console.log('C is fun');
  }
}
