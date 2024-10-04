function canConstruct(ransomNote: string, magazine: string): boolean {
  const magazineLetterMap = new Map<string, number>();

  for (const letter of magazine) {
    const letterCount = magazineLetterMap.get(letter);

    if (letterCount) {
      magazineLetterMap.set(letter, letterCount + 1);
    } else {
      magazineLetterMap.set(letter, 1);
    }
  }

  for (const letter of ransomNote) {
    const letterCountLeftInMagazine = magazineLetterMap.get(letter);
    if (!letterCountLeftInMagazine) return false;

    magazineLetterMap.set(letter, letterCountLeftInMagazine - 1);
  }

  return true;
}
// Time complexity: O(n)
// Space complexity: O(n)
