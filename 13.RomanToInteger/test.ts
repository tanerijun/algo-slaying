import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { romanToInt } from "./solution.ts";

Deno.test("III", () => {
  assertEquals(romanToInt("III"), 3)
})

Deno.test("LVIII", () => {
  assertEquals(romanToInt("LVIII"), 58)
})

Deno.test("MCMXCIV", () => {
  assertEquals(romanToInt("MCMXCIV"), 1994)
})