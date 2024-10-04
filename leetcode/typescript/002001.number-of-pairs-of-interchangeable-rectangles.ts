function interchangeableRectangles(rectangles: number[][]): number {
  let res = 0;

  // key: aspect ratio, value: rectangle count with key=aspect_ratio
  const aspectRatioMap = new Map<number, number>();

  for (const rectangle of rectangles) {
    const aspectRatio = rectangle[0] / rectangle[1];
    aspectRatioMap.set(aspectRatio, (aspectRatioMap.get(aspectRatio) ?? 0) + 1);
  }

  for (const v of aspectRatioMap.values()) {
    res += sumFromOne(v - 1);
    /**
     * But why?
     * Say that instead of storing the rectangle count as the value of our map,
     * we store an array of rectangles instead.
     *
     * Example:
     * If we have the key, value pair: 1/2 & [[4,8],[3,6],[10,20],[15,30]]
     *
     * The following are the interchangeable pairs of rectangles by index (0-indexed):
     * - Rectangle 0 with rectangle 1
     * - Rectangle 0 with rectangle 2
     * - Rectangle 0 with rectangle 3
     * - Rectangle 1 with rectangle 2
     * - Rectangle 1 with rectangle 3
     * - Rectangle 2 with rectangle 3
     *
     * This can be expressed as 3 (from rectangle 0) + 2 (from rectangle 1) + 1 (from rectangle 3)
     * which equals 1 + 2 + 3
     *
     * Notice how we don't need to consider combination with the rectangles on the left
     *  Rectangle 0 with rectangle 1 == rectangle 1 with rectangle 0
     */
  }

  return res;
}
// Time complexity: O(n)
// Space complexity: O(m), m = number of unique aspect_ratio

// Calculate 1 + 2 + ... + n
function sumFromOne(n: number) {
  return (n * (n + 1)) / 2;
}
