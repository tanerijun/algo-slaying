// Definition for singly-linked list.
export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  if (!head) {
    return null;
  }

  let l: ListNode | null | undefined = head;
  let r: ListNode | null | undefined = head;

  // Space between l and r should be n nodes apart
  // Therefore r have to move n nodes to the right
  for (let i = 0; i < n; i++) {
    r = r?.next;
  }

  if (!r) {
    // Delete head
    const temp = head.next;
    head.next = null;
    return temp;
  }

  // Move the r to the end while maintaining the spaces between l and r
  while (r.next) {
    r = r.next;
    l = l?.next;
  }

  l!.next = l?.next?.next as ListNode;

  return head;
};