function numUniqueEmails(emails: string[]): number {
	const uniqueEmails = new Set<string>()

	for (const email of emails) {
		const [localName, domainName] = email.split("@")

		// Process localName:
		let processedLocalName = ""
		for (let i = 0; i < localName.length; i++) {
			if (localName[i] === "+") {
				break
			} else if (localName[i] === ".") {
				continue
			} else {
				processedLocalName += localName[i]
			}
		}

		const processedEmail = processedLocalName + "@" + domainName

		uniqueEmails.add(processedEmail)
	}

	return uniqueEmails.size
}
// Time complexity: O(n * m) - where n = length of emails, m = average length of each email
// Space complexity: O(1)
