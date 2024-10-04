class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function isPalindrome(head: ListNode | null): boolean {
  const arr: number[] = [];
  let cur = head;

  while (cur) {
    arr.push(cur.val);
    cur = cur.next;
  }

  let l = 0;
  let r = arr.length - 1;

  while (l < r) {
    if (arr[l] !== arr[r]) {
      return false;
    }

    l++;
    r--;
  }

  return true;
}
// Time complexity: O(n)
// Space complexity: O(n)

function isPalindrome2(head: ListNode | null): boolean {
  // fast move at 2x the speed of slow,
  // so by the time fast reach the end of the list, slow will be in the middle of the list
  let fast: ListNode | null = head;
  let slow: ListNode | null = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow!.next;
  }

  // reverse second half of the list
  let prev: ListNode | null = null;
  while (slow) {
    const temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
  }

  // check palindrome
  let l: ListNode | null = head;
  let r: ListNode | null = prev; // prev is the last element at this point

  while (r && l) {
    if (l.val !== r.val) {
      return false;
    }

    l = l.next;
    r = r.next;
  }

  return true;
}
// Time complexity: O(n)
// Space complexity: O(1)
