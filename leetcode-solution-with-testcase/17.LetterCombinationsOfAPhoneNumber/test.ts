import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { letterCombinations } from "./solution.ts";

Deno.test("23", () => {
  assertEquals(letterCombinations("23"), [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
  ]);
});

Deno.test('""', () => {
  assertEquals(letterCombinations(""), []);
});

Deno.test("2", () => {
  assertEquals(letterCombinations("2"), ["a", "b", "c"]);
});
