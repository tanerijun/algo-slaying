class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function swapPairs(head: ListNode | null): ListNode | null {
  let curr = head;

  while (curr && curr.next) {
    // Swap
    const temp = curr.val;
    curr.val = curr.next.val;
    curr.next.val = temp;

    // Jump 2 nodes
    curr = curr.next.next;
  }

  return head;
}
// Time complexity: O(n)
// Space complexity: O(1)
