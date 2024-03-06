package add_two_numbers

type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n)
// Space complexity: O(n)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummyHead := &ListNode{}
	res, cur1, cur2, carry := dummyHead, l1, l2, 0

	for cur1 != nil || cur2 != nil || carry != 0 {
		val1 := 0
		if cur1 != nil {
			val1 = cur1.Val
			cur1 = cur1.Next
		}
		val2 := 0
		if cur2 != nil {
			val2 = cur2.Val
			cur2 = cur2.Next
		}

		sum := val1 + val2 + carry
		carry = sum / 10

		res.Next = &ListNode{Val: sum % 10}
		res = res.Next
	}

	return dummyHead.Next
}
