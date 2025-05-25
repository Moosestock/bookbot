def get_book_text(bookName):
	with open(bookName) as f:
		bookContents = f.read()
		#print(bookContents)
		numWords = bookContents.split()
		print(str(len(numWords)) + " words found in the document")

def main():
	get_book_text("books/frankenstein.txt")

main()
