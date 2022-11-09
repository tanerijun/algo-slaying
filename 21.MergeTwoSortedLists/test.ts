import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts"
import { mergeTwoLists, ListNode } from "./solution.ts"

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

Deno.test("list1 = [1,2,4], list2 = [1,3,4]", () => {
  // Create list1
  const list1 = new ListNode(1);
  let curr = list1;
  curr.next = new ListNode(2);
  curr = curr.next;
  curr.next = new ListNode(4);

  // Create list2
  const list2 = new ListNode(1);
  curr = list2;
  curr.next = new ListNode(3);
  curr = curr.next;
  curr.next = new ListNode(4);

  assertEquals(convertListToArray(mergeTwoLists(list1, list2)), [1, 1, 2, 3, 4, 4]);
})

Deno.test("list1 = [], list2 = []", () => {
  const list1 = null;
  const list2 = null;

  assertEquals(convertListToArray(mergeTwoLists(list1, list2)), []);
})

Deno.test("list1 = [], list2 = [0]", () => {
  const list1 = null;
  const list2 = new ListNode(0);

  assertEquals(convertListToArray(mergeTwoLists(list1, list2)), [0]);
})