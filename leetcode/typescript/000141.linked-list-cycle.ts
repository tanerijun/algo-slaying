class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  const set = new Set<ListNode>();
  let cur = head;

  while (cur) {
    if (set.has(cur)) {
      return true;
    }

    set.add(cur);
    cur = cur.next;
  }

  return false;
}
// Time complexity: O(n)
// Space complexity: O(n)

function hasCycle2(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow!.next;

    if (fast === slow) return true;
  }

  return false;
}
// Time complexity: O(n)
// Space complexity: O(1)
