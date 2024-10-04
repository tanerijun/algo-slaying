import {
  assert,
  assertEquals,
} from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { longestPalindrome } from "./solution.ts";

Deno.test("babad", () => {
  assert(["bab", "aba"].includes(longestPalindrome("babad")));
});

Deno.test("cbbd", () => {
  assertEquals(longestPalindrome("cbbd"), "bb");
});

Deno.test("cbbbba", () => {
  assertEquals(longestPalindrome("cbbbba"), "bbbb");
});
