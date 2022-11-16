import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { nextPermutation } from "./solution.ts";

Deno.test("[1,2,3]", () => {
    const nums = [1, 2, 3];
    nextPermutation(nums);
    assertEquals(nums, [1, 3, 2]);
})

Deno.test("[3,2,1]", () => {
    const nums = [3, 2, 1];
    nextPermutation(nums);
    assertEquals(nums, [1, 2, 3]);
})

Deno.test("[1,1,5]", () => {
    const nums = [1, 1, 5];
    nextPermutation(nums);
    assertEquals(nums, [1, 5, 1]);
})