import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { maxArea } from './solution.ts';

Deno.test('[1,8,6,2,5,4,8,3,7]', () => {
	assertEquals(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
});

Deno.test('[1,1]', () => {
	assertEquals(maxArea([1, 1]), 1);
});

maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]);
