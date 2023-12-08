import { createReadStream } from "node:fs"
import { createInterface } from "node:readline"

const filePath = process.argv[2]
if (!filePath) {
	console.log("Usage: npx tsx path-to-script path-to-input")
	process.exit(1)
}

const fileStream = createReadStream(filePath)
const rl = createInterface({ input: fileStream, crlfDelay: Infinity })

const spellingMap = {
	zero: 0,
	one: 1,
	two: 2,
	three: 3,
	four: 4,
	five: 5,
	six: 6,
	seven: 7,
	eight: 8,
	nine: 9,
}

function convertSpellingToNumberFromStart(str: string): number | undefined {
	for (const key of Object.keys(spellingMap)) {
		if (str.startsWith(key)) {
			return spellingMap[key as keyof typeof spellingMap]
		}
	}

	return undefined
}

function convertSpellingToNumberFromEnd(str: string): number | undefined {
	for (const key of Object.keys(spellingMap)) {
		if (str.endsWith(key)) {
			return spellingMap[key as keyof typeof spellingMap]
		}
	}

	return undefined
}

function isNumeric(x: string) {
	return /\d/.test(x)
}

function findFirstNum(str: string): number {
	for (let i = 0; i < str.length; i++) {
		const currentChar = str[i] as string
		if (isNumeric(currentChar)) {
			return parseInt(currentChar)
		}

		const conversionResult = convertSpellingToNumberFromStart(str.slice(i))
		if (conversionResult) {
			return conversionResult
		}
	}

	throw new Error("Couldn't find any number")
}

function findSecondNum(str: string): number {
	for (let i = str.length - 1; i >= 0; i--) {
		const currentChar = str[i] as string
		if (isNumeric(currentChar)) {
			return parseInt(currentChar)
		}

		const conversionResult = convertSpellingToNumberFromEnd(str.slice(0, i + 1))
		if (conversionResult) {
			return conversionResult
		}
	}

	throw new Error("Couldn't find any number")
}

const nums: Array<number> = []

for await (const line of rl) {
	const firstNum = findFirstNum(line)
	const secondNum = findSecondNum(line)
	const combinedNum = parseInt(firstNum.toString() + secondNum.toString())

	nums.push(combinedNum)
}

const sum = nums.reduce((a, b) => a + b)
console.log(sum)

// npx tsx day1/part2.ts day1/input.txt
// 53312
