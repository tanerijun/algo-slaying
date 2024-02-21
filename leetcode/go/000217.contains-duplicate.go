package leetcode

// Time complexity: O(n)
// Space complexity: O(n)
func containsDuplicate(nums []int) bool {
	set := make(map[int]struct{})

	for _, n := range nums {
		if _, ok := set[n]; ok {
			return true
		}
		set[n] = struct{}{}
	}

	return false
}
