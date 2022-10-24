import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { reverse } from "./solution.ts"

Deno.test("123", () => {
  assertEquals(reverse(123), 321);
})

Deno.test("-123", () => {
  assertEquals(reverse(-123), -321);
})

Deno.test("120", () => {
  assertEquals(reverse(120), 21);
})

Deno.test("1534236469", () => {
  assertEquals(reverse(1534236469), 0)
})

reverse(123);
