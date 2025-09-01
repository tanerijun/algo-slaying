package main

func characterReplacement(s string, k int) int {
	res := 0
	counter := map[byte]int{}
	l := 0

	for r := 0; r < len(s); r++ {
		counter[s[r]]++

		// Find maximum frequency in current window
		maxFreq := 0
		for _, freq := range counter {
			if freq > maxFreq {
				maxFreq = freq
			}
		}

		// Shrink window if k is used up
		for (r-l+1)-maxFreq > k {
			counter[s[l]]--
			l++
		}

		if r-l+1 > res {
			res = r - l + 1
		}
	}

	return res
}
