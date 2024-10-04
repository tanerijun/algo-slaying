class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function sortList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) {
    return head;
  }

  const left = head;
  const mid = getMid(head);
  const tmp = mid!.next;
  mid!.next = null;
  const right = tmp;

  const sortedLeft = sortList(left);
  const sortedRight = sortList(right);

  return merge(sortedLeft, sortedRight);
}
// Time complexity: O(n * log(n))
// Space complexity: O(log(n))

function getMid(head: ListNode | null) {
  let slow = head;
  let fast = head?.next;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  return slow;
}

function merge(left: ListNode | null, right: ListNode | null) {
  const dummyHead = new ListNode(0);
  let cur = dummyHead;

  while (left && right) {
    if (left.val <= right.val) {
      cur.next = left;
      left = left.next;
    } else {
      cur.next = right;
      right = right.next;
    }

    cur = cur.next;
  }

  if (left) {
    cur.next = left;
  }

  if (right) {
    cur.next = right;
  }

  return dummyHead.next;
}
