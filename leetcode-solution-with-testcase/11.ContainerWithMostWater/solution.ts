export function maxArea(height: number[]): number {
  let max: number = 0;
  let l: number = 0;
  let r: number = height.length - 1;

  while (l < r) {
    const w = r - l;
    const h = Math.min(height[l], height[r]);
    max = Math.max(max, w * h);

    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
  }

  return max;
}
