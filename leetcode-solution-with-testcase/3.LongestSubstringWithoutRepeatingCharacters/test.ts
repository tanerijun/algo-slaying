import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { lengthOfLongestSubstring } from "./solution.ts";

Deno.test("abcabcbb", () => {
  assertEquals(lengthOfLongestSubstring("abcabcbb"), 3);
});

Deno.test("bbbbb", () => {
  assertEquals(lengthOfLongestSubstring("bbbbb"), 1);
});

Deno.test("pwwkew", () => {
  assertEquals(lengthOfLongestSubstring("pwwkew"), 3);
});

Deno.test("abba", () => {
  assertEquals(lengthOfLongestSubstring("abba"), 2);
});
