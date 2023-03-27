function breakingRecords(scores: number[]): number[] {
    let breakingMaxCount = 0
    let breakingMinCount = 0
    let min = scores[0]
    let max = scores[0]
    
    for (let i = 1; i < scores.length; i++) {
        if (scores[i] > max) {
            max = scores[i]
            breakingMaxCount++
        } else if (scores[i] < min) {
            min = scores[i]
            breakingMinCount++
        }
    }
    
    return [breakingMaxCount, breakingMinCount]
}
// Time complexity:　Ｏ(n)
