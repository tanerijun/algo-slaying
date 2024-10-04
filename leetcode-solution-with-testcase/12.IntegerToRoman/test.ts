import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { intToRoman } from "./solution.ts";

Deno.test("3", () => {
  assertEquals(intToRoman(3), "III");
});

Deno.test("58", () => {
  assertEquals(intToRoman(58), "LVIII");
});

Deno.test("1994", () => {
  assertEquals(intToRoman(1994), "MCMXCIV");
});
