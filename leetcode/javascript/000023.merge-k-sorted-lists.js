/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 * Time complexity: O(nlog(n))
 * Space complexity: O(n)
 */
var mergeKLists = function (lists) {
  const values = [];
  for (let list of lists) {
    while (list) {
      values.push(list.val);
      list = list.next;
    }
  }

  values.sort((a, b) => a - b);

  let dummyHead = new ListNode(0);
  let cur = dummyHead;
  for (const val of values) {
    cur.next = new ListNode(val);
    cur = cur.next;
  }

  return dummyHead.next;
};

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 * Time complexity: O(nlog(k))
 * Space complexity: O(k)
 */
var mergeKLists = function (lists) {
  if (lists.length === 0) return null;
  const minHeap = new MinPriorityQueue((x) => x.val);
  for (let list of lists) {
    if (list !== null) minHeap.enqueue(list);
  }

  let dummyHead = new ListNode(0);
  let cur = dummyHead;
  while (minHeap.size() > 0) {
    let node = minHeap.dequeue();
    cur.next = node;
    cur = cur.next;

    node = node.next;
    if (node) minHeap.enqueue(node);
  }

  return dummyHead.next;
};
