package part2

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func calculatePowerOfSet(drawData string) int {
	draws := strings.Split(drawData, "; ")

	maxRedCubeSeen := 0
	maxGreenCubeSeen := 0
	maxBlueCubeSeen := 0

	for _, draw := range draws {
		cubes := strings.Split(draw, ", ")
		for _, cube := range cubes {
			r := regexp.MustCompile(`\d+`)
			qty, err := strconv.Atoi(r.FindString(cube))
			if err != nil {
				log.Fatal(err)
			}

			r = regexp.MustCompile(`[A-Za-z]+`)
			color := r.FindString(cube)

			switch color {
			case "red":
				if qty > maxRedCubeSeen {
					maxRedCubeSeen = qty
				}
			case "green":
				if qty > maxGreenCubeSeen {
					maxGreenCubeSeen = qty
				}
			case "blue":
				if qty > maxBlueCubeSeen {
					maxBlueCubeSeen = qty
				}
			}
		}
	}

	powerOfSet := maxRedCubeSeen * maxGreenCubeSeen * maxBlueCubeSeen
	return powerOfSet
}

func Part2Solution(inputFilePath string) int {
	fHand, err := os.Open(inputFilePath)
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(fHand)

	totalPower := 0

	for scanner.Scan() {
		line := scanner.Text()
		drawData := strings.Split(line, ": ")[1]
		powerOfSet := calculatePowerOfSet(drawData)
		totalPower += powerOfSet
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return totalPower
}
