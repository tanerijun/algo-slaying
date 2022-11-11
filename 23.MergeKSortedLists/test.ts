import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts"
import { mergeKLists, ListNode } from "./solution.ts"

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

function convertArrayToList(arr: number[]): ListNode | null {
  const head = new ListNode();
  let curr = head;

  for (let i = 0; i < arr.length; i++) {
    curr.next = new ListNode(arr[i]);
    curr = curr.next;
  }

  return head.next ? head.next : null;
}

Deno.test("[[1,4,5],[1,3,4],[2,6]]", () => {
  const arr = [
    convertArrayToList([1, 4, 5]),
    convertArrayToList([1, 3, 4]),
    convertArrayToList([2, 6])
  ];
  assertEquals(convertListToArray(mergeKLists(arr)), [1, 1, 2, 3, 4, 4, 5, 6]);
})

Deno.test("[]", () => {
  assertEquals(convertListToArray(mergeKLists([])), []);
})

Deno.test("[[]]", () => {
  assertEquals(convertListToArray(mergeKLists([null])), []);
})