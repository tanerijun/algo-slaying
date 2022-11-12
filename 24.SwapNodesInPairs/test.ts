import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { swapPairs, ListNode } from "./solution.ts";

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

Deno.test("[1,2,3,4]", () => {
  assertEquals(convertListToArray(swapPairs(convertArrayToList([1, 2, 3, 4]))), [2, 1, 4, 3]);
})

Deno.test("[]", () => {
  assertEquals(convertListToArray(swapPairs(convertArrayToList([]))), []);
})

Deno.test("[1]", () => {
  assertEquals(convertListToArray(swapPairs(convertArrayToList([1]))), [1]);
})

swapPairs(convertArrayToList([1, 2, 3, 4]))