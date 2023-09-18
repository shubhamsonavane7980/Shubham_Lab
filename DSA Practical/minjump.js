
function minJumps(arr) {
    let n = arr.length;
    let jumps = Array(n).fill(Infinity);
  
    jumps[0] = 0;
  
    for (let i = 1; i < n; i++) {
      for (let j = 0; j < i; j++) {
        if (i <= j + arr[j] && jumps[j] !== Infinity) {
          jumps[i] = Math.min(jumps[i], jumps[j] + 1);
        }
      }
    }
  
    return jumps[n - 1] === Infinity ? -1 : jumps[n - 1];
  }
  
  const arr = [3, 5, 6, 2, 0, 10];
  const result = minJumps(arr);
  
  console.log(result); // Outputs: 2
  
