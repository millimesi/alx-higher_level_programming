#!/usr/bin/node
//max finder function
function max (arr) {
  if (arr.length === 0) {
    return undefined;
  }
  let max = arr[0];
  for(let i = 1; i < arr.length; i++) {
    if (arr[i] > max){
      max = arr[i];
    }
  }
  return max;
}
//removing the o and 1st index of the arguments because they path to node and script
const argv = process.argv.slice(2);

//finding the first max
const firstMax = Math.max(...argv);
console.log('first max->' + firstMax);

//identifing the index of the first max
let indexToRemove = Array.prototype.indexOf.call(argv, firstMax)
console.

//removing the first max from the array
if (indexToRemove !== undefined) {
  argv.splice(indexToRemove, 1);
}

//finding the second max
const secondMax = Math.max(...argv);
console.log('second max->' + secondMax);
