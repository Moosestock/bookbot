def getBookName(sysArgv):
	import sys
#	print(sys.argv[0])
	try:
		bookName = sys.argv[1]
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	return bookName

def getBookText(bookName):
	with open(bookName) as f:
		bookText = f.read()
#		print(bookText)
		return bookText

def getBookWordCount(bookText):
	bookWords = bookText.split()
#	print(str(len(bookWords)) + " words found in the document")
	return bookWords

def setBookWordsLowercase(bookWords):
	lowerBookWords = ()
	lowerBookWords = bookWords.lower()
	return lowerBookWords

def countCharactersInBook(lowerBookWords):
	charCount = {}
#	print(lowerBookWords)
	bookCharacters = list(lowerBookWords)
	for character in bookCharacters:
		if character in charCount:
			charCount[character] += 1
		else:
			charCount[character] = 1
	return charCount

def sortOn(dict):
	return dict["num"]

def sortCharacters(charCount):
	listOfChars = []
	sortedChars = {}

	for k, v in charCount.items():
		if k.isalpha():
			sortedChars = {"char": k, "num": v}
			listOfChars.append(sortedChars)
	listOfChars.sort(reverse = True, key=sortOn)

	return listOfChars

def printCharCount(listOfChars, wordCount):
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {wordCount} total words")
	print("--------- Character Count -------")

	for charL in listOfChars:
		outputChar = f"{charL['char']}: {charL['num']}" 
		print(outputChar)

#	print(len(charList))
 # ": " charList[char]["num"])

	print("============= END ===============")
