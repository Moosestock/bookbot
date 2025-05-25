def main():
	from stats import getBookText
	bookText = getBookText("books/frankenstein.txt")

	from stats import getBookWordCount
	splitBookWords = getBookWordCount(bookText)

	from stats import setBookWordsLowercase
	lowerBookWords = setBookWordsLowercase(bookText)
#	print(lowerBookWords)

	from stats import countCharactersInBook
	charCount = {}
	charCount = countCharactersInBook(lowerBookWords)

	from stats import sortCharacters
	listOfChars = sortCharacters(charCount)
#	print(len(listOfChars))
#	print(listOfChars)

#	print(type(listOfChars[0]))
#	print(listOfChars[0])

	from stats import printCharCount
	printCharCount(listOfChars, len(splitBookWords))

main()
