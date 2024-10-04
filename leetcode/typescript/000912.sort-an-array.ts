function sortArray(nums: number[]): number[] {
  return mergeSort(nums);
}

function mergeSort(arr: number[]) {
  if (arr.length === 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const leftSide = mergeSort(arr.slice(0, mid));
  const rightSide = mergeSort(arr.slice(mid));
  return merge(leftSide, rightSide);
}

function merge(leftSide: number[], rightSide: number[]): number[] {
  let l = 0;
  let r = 0;
  let res: number[] = [];

  while (l < leftSide.length && r < rightSide.length) {
    if (leftSide[l] <= rightSide[r]) {
      res.push(leftSide[l]);
      l++;
    } else {
      res.push(rightSide[r]);
      r++;
    }
  }

  if (l < leftSide.length) {
    res = res.concat(leftSide.slice(l));
  }

  if (r < rightSide.length) {
    res = res.concat(rightSide.slice(r));
  }

  return res;
}

// Time complexity: O(nlog(n))
// Space complexity: O(n)
