import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { isValid } from './solution.ts';

Deno.test("()", () => {
  assertEquals(isValid("()"), true);
})

Deno.test("()[]{}", () => {
  assertEquals(isValid("()[]{}"), true);
})

Deno.test("(]", () => {
  assertEquals(isValid("(]"), false);
})

Deno.test("{[]}", () => {
  assertEquals(isValid("{[]}"), true);
})

Deno.test("((", () => {
  assertEquals(isValid("(("), false);
})