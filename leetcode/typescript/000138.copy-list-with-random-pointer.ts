class ListNode {
  val: number;
  next: ListNode | null;
  random: ListNode | null;
  constructor(val?: number, next?: ListNode, random?: ListNode) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}

function copyRandomList(head: ListNode | null): ListNode | null {
  const refToCopy = new Map<ListNode | null, ListNode | null>();
  refToCopy.set(null, null);

  let cur: ListNode | null = head;

  while (cur) {
    refToCopy.set(cur, new ListNode(cur.val));
    cur = cur.next;
  }

  cur = head;

  while (cur) {
    const copy = refToCopy.get(cur)!;
    copy.next = refToCopy.get(cur.next!)!;
    copy.random = refToCopy.get(cur.random!)!;
    cur = cur.next;
  }

  return refToCopy.get(head)!;
}
// Time complexity: O(n)
// Space complexity: O(n)
