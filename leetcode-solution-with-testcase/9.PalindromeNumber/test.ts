import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { isPalindrome } from './solution.ts';

Deno.test('121', () => {
	assertEquals(isPalindrome(121), true);
});

Deno.test('-121', () => {
	assertEquals(isPalindrome(121), true);
});

Deno.test('10', () => {
	assertEquals(isPalindrome(121), true);
});
