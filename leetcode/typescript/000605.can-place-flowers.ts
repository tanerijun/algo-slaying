function canPlaceFlowers(flowerbed: number[], n: number): boolean {
  let placedFlowers = 0;

  // First plot
  if (
    (flowerbed[0] === 0 && flowerbed[1] === 0) ||
    (flowerbed[0] === 0 && flowerbed.length === 1)
  ) {
    flowerbed[0] = 1;
    placedFlowers++;
  }

  // Last plot
  if (
    flowerbed[flowerbed.length - 1] === 0 &&
    flowerbed[flowerbed.length - 2] === 0
  ) {
    flowerbed[flowerbed.length - 1] = 1;
    placedFlowers++;
  }

  // Every plot in-between
  for (let i = 1; i < flowerbed.length - 2; i++) {
    if (flowerbed[i] === 0) {
      if (flowerbed[i - 1] === 0 && flowerbed[i + 1] === 0) {
        flowerbed[i] = 1;
        placedFlowers++;
      }
    }
  }

  return placedFlowers >= n;
}
// Time complexity: O(n)
// Space complexity: O(1)
