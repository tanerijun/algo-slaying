import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { twoSum } from "./solution.ts";

Deno.test("Input: numbers = [2,7,11,15], target = 9", () => {
  assertEquals(twoSum([2, 7, 11, 15], 9), [1, 2]);
});

Deno.test("Input: numbers = [2,3,4], target = 6", () => {
  assertEquals(twoSum([2, 3, 4], 6), [1, 3]);
});

Deno.test("Input: numbers = [-1, 0], target = -1", () => {
  assertEquals(twoSum([-1, 0], -1), [1, 2]);
});
