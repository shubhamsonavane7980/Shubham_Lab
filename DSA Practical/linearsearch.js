
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      return i;
    }
  }
  return -1;
}

const numbers = [4, 5, 12, 45, 67];
const target = 45;
const result = linearSearch(numbers, target);

console.log(result);
