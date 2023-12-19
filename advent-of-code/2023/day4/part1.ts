import { readFileSync } from "node:fs"
import path from "node:path"

type OwnedNumbers = number[]
type WinningNumbers = number[]
type ScratchCard = [WinningNumbers, OwnedNumbers]

function readInputFile() {
	const fPath = path.join(__dirname, "input.txt")
	const data = readFileSync(fPath, "utf-8")
	return data
}

function parseScratchCard(scratchCardData: string): ScratchCard[] {
	return scratchCardData.split("\n").map((row) => {
		const numbers = row.split(": ")[1]
		if (!numbers) {
			throw new Error("Error processing input")
		}

		const [winningNumbersStr, ownedNumbersStr] = numbers.split(" | ")
		if (!winningNumbersStr || !ownedNumbersStr) {
			throw new Error("Error processing input")
		}

		const winningNumbers = winningNumbersStr
			.split(" ")
			.filter((n) => n !== "")
			.map((n) => parseInt(n))

		const ownedNumbers = ownedNumbersStr
			.split(" ")
			.filter((n) => n !== "")
			.map((n) => parseInt(n))

		return [winningNumbers, ownedNumbers]
	})
}

function getSolution() {
	const data = readInputFile()
	const scratchCards = parseScratchCard(data)

	let totalPts = 0

	for (const scratchCard of scratchCards) {
		const [winningNumbers, ownedNumbers] = scratchCard
		let pts = 0
		for (const n of winningNumbers) {
			if (ownedNumbers.includes(n)) {
				console.log("matched", n)
				pts === 0 ? (pts = 1) : (pts *= 2)
			}
		}
		console.log(pts)
		totalPts += pts
	}

	return totalPts
}

console.log(getSolution())
