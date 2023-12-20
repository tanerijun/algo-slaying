import { readFileSync } from "node:fs"
import path from "node:path"

type OwnedNumbers = number[]
type WinningNumbers = number[]
type ScratchCard = [WinningNumbers, OwnedNumbers]
type ScratchCardWithCount = [ScratchCard, number]

function readInputFile() {
	const filePath = new URL(import.meta.url).pathname
	const fileDir = path.dirname(filePath)
	const inputPath = path.join(fileDir, "input.txt")
	const data = readFileSync(inputPath, "utf-8")
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
	const scratchCardsWithCount: ScratchCardWithCount[] = scratchCards.map((card) => [card, 1])

	for (let i = 0; i < scratchCardsWithCount.length; i++) {
		const [scratchCard, count] = scratchCardsWithCount[i]!
		const [winningNumbers, ownedNumbers] = scratchCard
		let toAddIdx = 1
		let addCount = count
		for (const n of winningNumbers) {
			if (ownedNumbers.includes(n)) {
				const nextScratchCard = scratchCardsWithCount[i + toAddIdx]!
				nextScratchCard[1] = nextScratchCard[1] + addCount
				toAddIdx++
			}
		}
	}

	let totalScratchCards = 0
	for (let i = 0; i < scratchCardsWithCount.length; i++) {
		totalScratchCards += scratchCardsWithCount[i]![1]
	}

	return totalScratchCards
}

console.log(getSolution())
