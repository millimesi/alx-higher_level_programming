#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1 || !n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
