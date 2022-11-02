import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { threeSumClosest } from "./solution.ts";

Deno.test("nums = [-1,2,1,-4], target = 1", () => {
  assertEquals(threeSumClosest([-1, 2, 1, -4], 1), 2);
})

Deno.test("nums = [0,0,0], target = 1", () => {
  assertEquals(threeSumClosest([0, 0, 0], 1), 0);
})

Deno.test("nums = [4,0,5,-5,3,3,0,-4,-5], target = -2", () => {
  assertEquals(threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2), -2)
})

threeSumClosest([0, 0, 0], 1);