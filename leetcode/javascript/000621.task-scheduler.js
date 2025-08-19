/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    const countMap = new Map();
    tasks.forEach((task) => {
        countMap.set(task, (countMap.get(task) ?? 0) + 1)
    })

    let clock = 0;
    const q = new Queue();
    const pq = PriorityQueue.fromArray(Array.from(countMap.values()), (a, b) => b - a);

    while (!q.isEmpty() || !pq.isEmpty()) {
        clock++;

        if (!pq.isEmpty()) {
            c = pq.dequeue();
            c--;
            if (c > 0) {
                q.enqueue([clock + n, c]);
            }
        }

        if (!q.isEmpty() && q.front()[0] === clock) {
            c = q.dequeue()[1];
            pq.enqueue(c);
        }
    }

    return clock;
};
