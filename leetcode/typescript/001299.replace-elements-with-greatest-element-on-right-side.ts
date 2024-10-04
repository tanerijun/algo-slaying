function replaceElements(arr: number[]): number[] {
  let currentMax = arr[arr.length - 1];
  arr[arr.length - 1] = -1; // the last element is always -1

  for (let i = arr.length - 2; i >= 0; i--) {
    const temp = arr[i];
    arr[i] = currentMax;
    currentMax = Math.max(currentMax, temp);
  }

  return arr;
}
// Time complexity: O(n)
// Space complexity: O(1)
