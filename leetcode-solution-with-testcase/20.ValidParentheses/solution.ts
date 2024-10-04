export function isValid(s: string): boolean {
  if (!s || s.length % 2 != 0) {
    return false;
  }

  const stack: string[] = [];

  for (let i = 0; i < s.length; i += 1) {
    switch (s[i]) {
      case "{":
        stack.push("}");
        break;
      case "[":
        stack.push("]");
        break;
      case "(":
        stack.push(")");
        break;
      default:
        if (stack.pop() !== s[i]) {
          return false;
        }
    }
  }

  return stack.length === 0;
}
