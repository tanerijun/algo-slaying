import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { longestCommonPrefix } from "./solution.ts";

Deno.test(`["flower","flow","flight"]`, () => {
  assertEquals(longestCommonPrefix(["flower", "flow", "flight"]), "fl");
});

Deno.test(`["dog","racecar","car"]`, () => {
  assertEquals(longestCommonPrefix(["dog", "racecar", "car"]), "");
});

Deno.test(`["a"]`, () => {
  assertEquals(longestCommonPrefix(["a"]), "a");
});
