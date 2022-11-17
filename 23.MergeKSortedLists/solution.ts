export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// Divide and Conquer approach
// Time complexity : O(Nlogk) where k is the number of linked lists.
export function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (!lists) {
    return null;
  }

  // Merge two lists at a time until we're left with only a pair.
  while (lists.length > 1) {
    const temp: Array<ListNode | null> = [];

    for (let i = 0; i < lists.length; i += 2) {
      const l1 = lists[i];
      const l2 = i + 1 >= lists.length ? null : lists[i + 1]; // in case if lists.length is an odd number
      temp.push(mergeTwoLists(l1, l2));
    }

    lists = temp;
  }

  // At this point, we're left with one single linked list
  return lists[0] ? lists[0] : null;
};

// The solution from 21.MergeTwoSortedLists
function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const dummyHead = new ListNode();
  let curr: ListNode | null = dummyHead;

  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      curr.next = list1;
      list1 = list1.next;
    } else if (list1.val > list2.val) {
      curr.next = list2;
      list2 = list2.next;
    }

    curr = curr.next as ListNode;
  }

  curr.next = list1 === null ? list2 : list1;

  return dummyHead.next;
};