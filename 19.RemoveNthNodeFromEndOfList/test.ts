import { assertEquals } from 'https://deno.land/std@0.160.0/testing/asserts.ts';
import { removeNthFromEnd, ListNode } from './solution.ts';

function createLinkedList(start: number, end: number): ListNode {
  const head = new ListNode(start);
  let curr = head;

  for (let i = start + 1; i <= end; i++) {
    curr.next = new ListNode(i);
    curr = curr.next;
  }

  return head;
}

function convertListToArray(head: ListNode | null): number[] {
  const arr: number[] = [];

  if (!head) return arr;

  let curr: ListNode | null = head;

  while (curr) {
    arr.push(curr.val);
    curr = curr.next;
  }

  return arr;
}

Deno.test("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4", () => {
  const linkedList = createLinkedList(1, 10);

  assertEquals(convertListToArray(removeNthFromEnd(linkedList, 4)), [1, 2, 3, 4, 5, 6, 8, 9, 10]);
})

Deno.test("[1, 2 ,3 ,4 ,5], 2]", () => {
  const linkedList = createLinkedList(1, 5);

  assertEquals(convertListToArray(removeNthFromEnd(linkedList, 2)), [1, 2, 3, 5]);
})

Deno.test("[1], 1", () => {
  const linkedList = createLinkedList(1, 1);

  assertEquals(convertListToArray(removeNthFromEnd(linkedList, 1)), []);
})

Deno.test("[1, 2], 2", () => {
  const linkedList = createLinkedList(1, 2);

  assertEquals(convertListToArray(removeNthFromEnd(linkedList, 2)), [2]);
})