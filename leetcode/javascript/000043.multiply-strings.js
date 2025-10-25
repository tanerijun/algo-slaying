/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 * Time complexity: O(m * n)
 * Space complexity: O(m + n)
 * m = num1.length, n = num2.length
 */
var multiply = function (num1, num2) {
  if (num1 === "0" || num2 === "0") return "0";
  const result = Array(num1.length + num2.length).fill(0);

  for (let i = num1.length - 1; i >= 0; i--) {
    let carry = 0;
    for (let j = num2.length - 1; j >= 0; j--) {
      const temp = num1[i] * num2[j] + result[i + j + 1] + carry;
      result[i + j + 1] = temp % 10;
      carry = Math.floor(temp / 10);
    }
    // When inner loop finishes, the last digit processed was num2[0].
    // The calculation was for index i + j + 1 = i + 0 + 1 = i + 1.
    // The leftover carry belongs tin the next position to the left. i + 1 - 1 = i
    result[i] += carry;
  }

  return result.join("").replace(/^0+/, "");
};
