import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { threeSum } from "./solution.ts";

Deno.test("[-1,0,1,2,-1,-4]", () => {
  assertEquals(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
})

Deno.test("[0,1,1]", () => {
  assertEquals(threeSum([0, 1, 1]), [])
})

Deno.test("[0,0,0]", () => {
  assertEquals(threeSum([0, 0, 0]), [[0, 0, 0]])
})

Deno.test("[-2,0,0,2,2]", () => {
  assertEquals(threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
})