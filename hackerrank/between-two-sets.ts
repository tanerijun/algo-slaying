/**
 *  The problem statement is a bit confusing.
 *  Watch this video for better understanding: https://www.youtube.com/watch?v=-c_V4fQ2mKU
 *
 *  There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
 *  The elements of the first array are all factors of the integer being considered
 *  The integer being considered is a factor of all elements of the second array
 *
 *  In other words, we need to find number of integers that satisfy the following two conditions:
 *  - multiples of first array
 *  - factors of second array
 */

// helpers
const gcd = (a: number, b: number): number => (b ? gcd(b, a % b) : a)
const lcm = (a: number, b: number): number => (a * b) / gcd(a, b)
const gcdOfArray = (arr: number[]): number => arr.reduce(gcd)
const lcmOfArray = (arr: number[]): number => arr.reduce(lcm)

function getTotalX(a: number[], b: number[]): number {
	let res = 0

	// find the lcm of all elements in a
	const lcmOfA = lcmOfArray(a)

	// find the gcd of all elements in b
	const gcdOfB = gcdOfArray(b)

	// find all multiples of lcmOfA that evenly divides gcdOfB
	for (let i = lcmOfA; i <= gcdOfB; i += lcmOfA) {
		if (gcdOfB % i === 0) {
			res++
		}
	}

	return res
}
