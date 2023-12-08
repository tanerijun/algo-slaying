import { createReadStream } from "node:fs"
import { createInterface } from "node:readline"

const filePath = process.argv[2]
if (!filePath) {
	console.log("Usage: npx tsx path-to-script path-to-input")
	process.exit(1)
}

const fileStream = createReadStream(filePath)
const rl = createInterface({ input: fileStream, crlfDelay: Infinity })

function isNumeric(x: string) {
	return /\d/.test(x)
}

const nums: Array<number> = []

for await (const line of rl) {
	let firstNum = ""
	let secondNum = ""

	for (let i = 0; i < line.length; i++) {
		const curChar = line[i] as string
		if (isNumeric(curChar)) {
			firstNum = curChar
			break
		}
	}

	for (let i = line.length - 1; i >= 0; i--) {
		const curChar = line[i] as string
		if (isNumeric(curChar)) {
			secondNum = curChar
			break
		}
	}

	nums.push(parseInt(firstNum + secondNum))
}

const sum = nums.reduce((a, b) => a + b)
console.log(sum)

// npx tsx day1/part1.ts day1/input.txt
// 53386
