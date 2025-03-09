// https://github.com/datastructures-js/queue/tree/v4.2.3

declare global {
  class Queue<T> {
    constructor(elements?: T[]);
    isEmpty(): boolean;
    size(): number;
    enqueue(element: T): Queue<T>;
    push(element: T): Queue<T>;
    dequeue(): T;
    pop(): T;
    front(): T;
    back(): T;
    toArray(): T[];
    clear(): void;
    clone(): Queue<T>;
    static fromArray<T>(elements: T[]): Queue<T>;
  }
}

export {};
