function dayOfProgrammer(year: number): string {
	// Our answer
	let date = ""

	// Days in february when it's not a leap year
	let daysInFebruary = 28

	// Find check if it's a year where February is not 28 days:

	// Year of transition from Julian to Gregorian calendar
	// On this day, 32nd day of the year is 14th February
	if (year === 1918) {
		daysInFebruary = 15
	}

	// Leap year
	const isJulianLeapYear = year < 1918 && year % 4 === 0
	const isGregorianLeapYear =
		year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)
	if (isJulianLeapYear || isGregorianLeapYear) {
		daysInFebruary = 29
	}

	// Find the number of days in the year
	const daysEachMonth = [
		31,
		daysInFebruary,
		31,
		30,
		31,
		30,
		31,
		31,
		30,
		31,
		30,
		31,
	]

	// Find the day of the programmer
	let dayOfProgrammer = 256
	for (let i = 0; i < daysEachMonth.length; i++) {
		dayOfProgrammer = dayOfProgrammer - daysEachMonth[i]
		if (dayOfProgrammer <= 0) {
			const month = `${i + 1}`.padStart(2, "0")
			date = `${dayOfProgrammer + daysEachMonth[i]}.${month}.${year}`
			break
		}
	}

	return date
}

function dayOfProgrammer2(year: number): string {
	// Days in february when it's not a leap year
	let daysInFebruary = 28

	// Find check if it's a year where February is not 28 days:

	// Year of transition from Julian to Gregorian calendar
	// On this day, 32nd day of the year is 14th February
	if (year === 1918) {
		daysInFebruary = 15
	}

	// Leap year
	const isJulianLeapYear = year < 1918 && year % 4 === 0
	const isGregorianLeapYear =
		year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)
	if (isJulianLeapYear || isGregorianLeapYear) {
		daysInFebruary = 29
	}

	// Since we know that we're looking for the date of the 256th day of the year,
	// we know that the month can't possibly be October or later.
	const daysFromJanuaryToSeptember =
		31 + daysInFebruary + 31 + 30 + 31 + 30 + 31 + 31

	// Find the day of the programmer
	let dayOfProgrammer = 256
	dayOfProgrammer = dayOfProgrammer - daysFromJanuaryToSeptember // what's left is the date in September

	return `${dayOfProgrammer}.09.${year}`
}

// Time complexity for both algorithms: O(1)
