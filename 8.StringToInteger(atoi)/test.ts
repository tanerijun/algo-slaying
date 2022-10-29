import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { myAtoi } from './solution.ts';

Deno.test('42', () => {
	assertEquals(myAtoi('42'), 42);
});

Deno.test('   -42', () => {
	assertEquals(myAtoi('   -42'), -42);
});

Deno.test('4193 with words', () => {
	assertEquals(myAtoi('4193 with words'), 4193);
});

Deno.test('-91283472332', () => {
	assertEquals(myAtoi('-91283472332'), -2147483648);
});
