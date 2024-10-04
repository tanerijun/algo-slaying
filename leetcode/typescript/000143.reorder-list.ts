class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow!.next;
  }

  const reversedHead = reverse(slow ? slow.next : null);

  if (slow) {
    slow.next = null;
  }

  let curA = head;
  let curB = reversedHead;
  let dummyHead = new ListNode(0);
  let cur = dummyHead;

  while (curA && curB) {
    cur.next = curA;
    curA = curA.next;
    cur = cur.next;

    cur.next = curB;
    curB = curB.next;
    cur = cur.next;
  }

  cur.next = curA;
}
// Time complexity: O(n)
// Space complexity: O(1)

function reverse(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  let cur = head;

  while (cur) {
    const temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }

  return prev;
}
