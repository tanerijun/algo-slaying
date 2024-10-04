import { assertEquals } from "https://deno.land/std@0.160.0/testing/asserts.ts";
import { addTwoNumbers, ListNode } from "./solution.ts";

function generateList(arr: number[]): ListNode {
  let head: ListNode = new ListNode(arr[0]);
  let curr: ListNode = head;

  if (arr.length > 1) {
    for (let i = 1; i < arr.length; i++) {
      curr.next = new ListNode(arr[i]);
      curr = curr.next;
    }
  }

  return head;
}

function generateArray(node: ListNode | null): number[] {
  const arr = [];

  while (node != null) {
    arr.push(node.val);
    node = node.next;
  }

  return arr;
}

Deno.test("[2, 4, 3][5, 6, 4]", () => {
  const list1 = generateList([2, 4, 3]);
  const list2 = generateList([5, 6, 4]);
  const result = addTwoNumbers(list1, list2);
  assertEquals(generateArray(result), [7, 0, 8]);
});

Deno.test("[0][0]", () => {
  const list1 = generateList([0]);
  const list2 = generateList([0]);
  const result = addTwoNumbers(list1, list2);
  assertEquals(generateArray(result), [0]);
});

Deno.test("[9,9,9,9,9,9,9][9,9,9,9]", () => {
  const list1 = generateList([9, 9, 9, 9, 9, 9, 9]);
  const list2 = generateList([9, 9, 9, 9]);
  const result = addTwoNumbers(list1, list2);
  assertEquals(generateArray(result), [8, 9, 9, 9, 0, 0, 0, 1]);
});
