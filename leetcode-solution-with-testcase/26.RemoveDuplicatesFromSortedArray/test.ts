import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { removeDuplicates } from "./solution.ts";

Deno.test("[1,1,2]", () => {
  const nums = [1, 1, 2];
  const expectedNums = [1, 2];

  const [k, editedNums] = removeDuplicates(nums);

  assertEquals(k, expectedNums.length);

  for (let i = 0; i < k; i++) {
    assertEquals(editedNums[i], expectedNums[i]);
  }
});

Deno.test("[0,0,1,1,1,2,2,3,3,4]", () => {
  const nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
  const expectedNums = [0, 1, 2, 3, 4];

  const [k, editedNums] = removeDuplicates(nums);

  assertEquals(k, expectedNums.length);

  for (let i = 0; i < k; i++) {
    assertEquals(editedNums[i], expectedNums[i]);
  }
});
