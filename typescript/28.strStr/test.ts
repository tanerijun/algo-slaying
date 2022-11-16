import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { strStr } from "./solution.ts";

Deno.test(`haystack = "sadbutsad", needle = "sad"`, () => {
  assertEquals(strStr("sadbutsad", "sad"), 0);
})

Deno.test(`haystack = "leetcode", needle = "leeto"`, () => {
  assertEquals(strStr("leetcode", "leeto"), -1);
})