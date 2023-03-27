function birthday(s: number[], d: number, m: number): number {
    let res = 0
    let sum = 0
    
    for (let i = 0, j = m - 1; j < s.length; i++, j++) {
        if (i === 0) {
            sum = s.slice(i, j + 1).reduce((a, b) => a + b)
            if (sum === d) res++
            continue
        }
        
        sum = sum - s[i - 1] + s[j]    
        if (sum === d) res++
    }
    
    return res
}
// Time complexity: O(n)
