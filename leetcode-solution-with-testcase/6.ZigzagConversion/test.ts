import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { convert } from './solution.ts';

Deno.test('s=PAYPALISHIRING, nRow=3', () => {
	assertEquals(convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR');
});

Deno.test('s=PAYPALISHIRING, nRow=4', () => {
	assertEquals(convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI');
});

Deno.test('s=A, nRow=1', () => {
	assertEquals(convert('A', 1), 'A');
});

Deno.test('s=AB, nRow=1', () => {
	assertEquals(convert('AB', 1), 'AB');
});
