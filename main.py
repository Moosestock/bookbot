def main():

	import sys

	from stats import getBookName
	bookName = getBookName(sys.argv)

	from stats import getBookText
	bookText = getBookText(bookName)

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
