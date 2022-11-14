import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { removeElement } from "./solution.ts";

Deno.test("nums = [3,2,2,3], val = 3", () => {
  const nums = [3, 2, 2, 3];
  const val = 3;
  const expectedNums = [2, 2];

  const [k, editedNums] = removeElement(nums, val);
  assertEquals(k, expectedNums.length);

  assertEquals(editedNums.slice(0, k).includes(val), false);
})

Deno.test("nums = [0,1,2,2,3,0,4,2], val = 2", () => {
  const nums = [0, 1, 2, 2, 3, 0, 4, 2];
  const val = 2;
  const expectedNums = [0, 1, 4, 0, 3];

  const [k, editedNums] = removeElement(nums, val);
  assertEquals(k, expectedNums.length);

  assertEquals(editedNums.slice(0, k).includes(val), false);
})