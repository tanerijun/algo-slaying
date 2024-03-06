package two_sum

// Time complexity: O(n)
// Space complexity: O(n)
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if complement, ok := m[target-nums[i]]; ok {
			return []int{complement, i}
		}
		m[nums[i]] = i
	}

	return nil
}
