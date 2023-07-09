function validPalindrome(s: string): boolean {
	let l = 0
	let r = s.length - 1

	while (l < r) {
		if (s[l] === s[r]) {
			l++
			r--
			continue
		}

		// At this point, the s[l] and s[r] are different
		// Try deleting s[l] and see if the resulting string is a palindrome
		// Try deleting s[r] and see if the resulting string is a palindrome
		// If one of them result in a palindrome, then we're good
		// Else return false
		if (isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1)) {
			break
		}

		return false
	}

	return true
}

function isPalindrome(s: string, l: number, r: number): boolean {
	while (l < r) {
		if (s[l] !== s[r]) {
			return false
		}

		l++
		r--
	}

	return true
}

// Time complexity: O(n)
// Space complexity: O(1)
