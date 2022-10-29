export function romanToInt(s: string): number {
  let res: number = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    switch (s[i]) {
      case "M":
        res += 1000;
        break;
      case "D":
        res += 500;
        break;
      case "C":
        res += 100 * (res >= 500 ? -1 : 1);
        break;
      case "L":
        res += 50;
        break;
      case "X":
        res += 10 * (res >= 50 ? -1 : 1);
        break;
      case "V":
        res += 5;
        break;
      case "I":
        res += 1 * (res >= 5 ? -1 : 1);
        break;
      default:
        break;
    }
  }

  return res;
};