import {
  assertArrayIncludes,
  assertEquals,
} from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { generateParenthesis } from "./solution.ts";

Deno.test("n = 3", () => {
  assertArrayIncludes(generateParenthesis(3), [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()",
  ]);
});

Deno.test("n = 1", () => {
  assertArrayIncludes(generateParenthesis(1), ["()"]);
});
