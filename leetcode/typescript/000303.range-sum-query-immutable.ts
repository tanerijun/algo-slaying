class NumArray {
  _nums: number[];

  constructor(nums: number[]) {
    this._nums = nums;
  }

  sumRange(left: number, right: number): number {
    let sum = 0;
    for (let i = left; i <= right; i++) {
      sum += this._nums[i];
    }

    return sum;
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */

// Time complexity: O(n)
// Space complexity: O(1)

class NumArray2 {
  // Contain sum of numbers up to the index
  // Ex: _sums[3] = _sums[0] + _sums[1] + _sums[2] + _sums[3]
  _sums: number[] = [0];

  constructor(nums: number[]) {
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      sum += nums[i];
      this._sums.push(sum);
    }
  }

  sumRange(left: number, right: number): number {
    return this._sums[right + 1] - this._sums[left];
  }
}

// Time complexity: O(1)
// Space complexity: O(n)
