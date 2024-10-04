import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { fourSum, twoSum } from "./solution.ts";

Deno.test("twoSum on [1, 2, 3, 4], target = 5", () => {
  assertEquals(twoSum([1, 2, 3, 4], 5), [[1, 4], [2, 3]]);
});

Deno.test("twoSum on [1, 2, 3, 4], target = 3", () => {
  assertEquals(twoSum([1, 2, 3, 4], 3), [[1, 2]]);
});

Deno.test("twoSum on [1, 2, 3, 4], target = 4", () => {
  assertEquals(twoSum([1, 2, 3, 4], 4), [[1, 3]]);
});

Deno.test("twoSum on [1, 2, 3, 4], target = 8", () => {
  assertEquals(twoSum([1, 2, 3, 4], 8), []);
});

Deno.test("twoSum on [1, 1, 2, 2, 3, 3], target = 4", () => {
  assertEquals(twoSum([1, 1, 2, 2, 3, 3], 4), [[1, 3], [2, 2]]);
});

Deno.test("fourSum on [1,0,-1,0,-2,2], target = 0", () => {
  assertEquals(fourSum([1, 0, -1, 0, -2, 2], 0), [
    [-2, -1, 1, 2],
    [-2, 0, 0, 2],
    [-1, 0, 0, 1],
  ]);
});

Deno.test("fourSum on [2,2,2,2,2], target = 8", () => {
  assertEquals(fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]);
});
