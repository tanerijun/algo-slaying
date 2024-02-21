package leetcode

// Time complexity: O(n)
// Space complexity: O(n)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummyHead := &ListNode{}
	res := dummyHead
	cur1 := l1
	cur2 := l2
	carry := 0

	for cur1 != nil || cur2 != nil {
		val1 := 0
		if cur1 != nil {
			val1 = cur1.Val
		}
		val2 := 0
		if cur2 != nil {
			val2 = cur2.Val
		}
		sum := val1 + val2 + carry
		if sum >= 10 {
			carry = 1
			sum -= 10
		} else {
			carry = 0
		}

		res.Next = &ListNode{Val: sum}
		res = res.Next

		if cur1 != nil {
			cur1 = cur1.Next
		}
		if cur2 != nil {
			cur2 = cur2.Next
		}
	}

	if carry == 1 {
		res.Next = &ListNode{Val: 1}
	}

	return dummyHead.Next
}
