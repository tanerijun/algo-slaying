function divisibleSumPairs(n: number, k: number, ar: number[]): number {
    let res = 0
    
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if ((ar[i] + ar[j]) % k === 0) {
                res++
            }
        }
    }
    
    return res
}
// Time complexity: O(n^2)
