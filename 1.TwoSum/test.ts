import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { twoSum } from './solution.ts';

Deno.test('[2, 7, 11, 15]', () => {
	assertEquals(twoSum([2, 7, 11, 15], 9), [0, 1]);
	assertEquals(twoSum([2, 7, 11, 15], 18), [1, 2]);
});

Deno.test('[3,2,4]', () => {
	assertEquals(twoSum([3, 2, 4], 6), [1, 2]);
	assertEquals(twoSum([3, 2, 4], 8), []);
});

Deno.test('[3, 3]', () => {
	assertEquals(twoSum([3, 3], 6), [0, 1]);
});
