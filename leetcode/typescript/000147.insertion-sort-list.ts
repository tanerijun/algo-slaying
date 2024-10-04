class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function insertionSortList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;

  const dummyHead = new ListNode(0, head);
  let prev = head;
  let cur: ListNode | null = head.next;

  while (cur) {
    if (cur.val < prev.val) {
      let cur2: ListNode | null = dummyHead;

      while (cur2.next!.val <= cur.val) {
        cur2 = cur2.next!;
      }

      prev.next = cur.next;
      cur.next = cur2.next;
      cur2.next = cur;
    }

    prev = cur;
    cur = cur.next;
  }

  return dummyHead.next;
}
// Time complexity: O(n^2)
// Space complexity: O(1)
