package part1

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type bag struct {
	red   int
	green int
	blue  int
}

var originalBag = bag{red: 12, green: 13, blue: 14}

func extractGameId(gameData string) int {
	r := regexp.MustCompile(`\d+`)

	res := r.FindString(gameData)

	resInt, err := strconv.Atoi(res)
	if err != nil {
		log.Fatal(err)
	}

	return resInt
}

func extractCubeOccurrences(drawData string) map[string]int {
	res := make(map[string]int)

	cubeInfos := strings.Split(drawData, ",")
	for _, cubeInfo := range cubeInfos {
		cubeInfo = strings.TrimSpace(cubeInfo)

		r := regexp.MustCompile(`\d+`)
		qty, err := strconv.Atoi(r.FindString(cubeInfo))
		if err != nil {
			log.Fatal(err)
		}

		r = regexp.MustCompile(`[A-Za-z]+`)
		color := r.FindString(cubeInfo)

		res[color] = qty
	}

	return res
}

func sumSlice(s []int) int {
	sum := 0
	for _, n := range s {
		sum += n
	}

	return sum
}

func Part1Solution(inputFilePath string) int {
	fHand, err := os.Open(inputFilePath)
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(fHand)

	validGames := []int{}

	for scanner.Scan() {
		line := scanner.Text()

		splitRes := strings.Split(line, ": ")
		gameData := splitRes[0]
		drawData := splitRes[1]

		gameId := extractGameId(gameData)

		maxCubeSeen := bag{}

		draws := strings.Split(drawData, "; ")
		for _, draw := range draws {
			cubeOccurrences := extractCubeOccurrences(draw)
			for k, v := range cubeOccurrences {
				switch k {
				case "red":
					if v > maxCubeSeen.red {
						maxCubeSeen.red = v
					}
				case "green":
					if v > maxCubeSeen.green {
						maxCubeSeen.green = v
					}
				case "blue":
					if v > maxCubeSeen.blue {
						maxCubeSeen.blue = v
					}
				}
			}
		}

		if maxCubeSeen.red <= originalBag.red && maxCubeSeen.green <= originalBag.green && maxCubeSeen.blue <= originalBag.blue {
			validGames = append(validGames, gameId)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	sumOfValidGamesId := sumSlice(validGames)
	return sumOfValidGamesId
}
