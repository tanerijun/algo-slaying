import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { divide } from "./solution.ts";

Deno.test("dividend = 10, divisor = 3", () => {
  assertEquals(divide(10, 3), 3);
})

Deno.test("dividend = 7, divisor = -3", () => {
  assertEquals(divide(7, -3), -2);
})

Deno.test("dividend = 4, divisor = 2", () => {
  assertEquals(divide(4, 2), 2);
})


Deno.test("dividend = 0, divisor = 1", () => {
  assertEquals(divide(0, 1), 0);
})

Deno.test("dividend = 1, divisor = 1", () => {
  assertEquals(divide(1, 1), 1);
})

Deno.test("dividend = 1, divisor = -1", () => {
  assertEquals(divide(1, -1), -1);
})

Deno.test("dividend = -1, divisor = 1", () => {
  assertEquals(divide(-1, 1), -1);
})

Deno.test("dividend = 2, divisor = 2", () => {
  assertEquals(divide(2, 2), 1);
})

Deno.test("dividend = -2147483648, divisor = -1", () => {
  assertEquals(divide(-2147483648, -1), 2147483647);
})

Deno.test("dividend = -2147483648, divisor = 2", () => {
  assertEquals(divide(-2147483648, 2), -1073741824);
})

divide(4, 2)