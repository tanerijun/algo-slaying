package main

import (
	"aoc2023-day2/part1"
	"aoc2023-day2/part2"
	"fmt"
	"log"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Usage: <run program> <path_to_input_file>")
	}

	fPath := os.Args[1]

	fmt.Println("Part1 solution:", part1.Part1Solution(fPath))
	fmt.Println("Part2 solution:", part2.Part2Solution(fPath))
}
