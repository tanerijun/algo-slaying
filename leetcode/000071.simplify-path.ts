function simplifyPath(path: string): string {
	const stack: string[] = [];

	const dirs = path.split("/");

	for (let dir of dirs) {
		// Handle "" && "."
		if (!dir || dir === ".") {
			continue;
		}

		// Handle ".."
		if (dir === "..") {
			stack.pop();
			continue;
		}

		// Valid name
		stack.push(dir);
	}

	return "/" + stack.join("/");
}
// Time complexity: O(n)
// Space complexity: O(n)
