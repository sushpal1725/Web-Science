import os, sys
def getWordFrequencyDict(page, wordFrequencyDict):
	tokens = page.split(' ')
	for t in tokens:
		wordFrequencyDict.setdefault(t, 0)
		wordFrequencyDict[t] = wordFrequencyDict[t] + 1
		
def getUniqueTermsFromHTML():
	lines = []
	try:
		inputFile = open('total.html', 'r')
		lines = inputFile.readlines()
		inputFile.close()
	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(fname, exc_tb.tb_lineno, sys.exc_info() )

	wordFrequencyDict = {}
	instanceCount = 0
	print lines
	getWordFrequencyDict(lines, wordFrequencyDict)
		#print len(wordFrequencyDict)
	instanceCount = instanceCount + 1

	wordFrequencyDict = sorted(wordFrequencyDict.items(), key=lambda x:x[1], reverse=True)
	print
	print 'begin'
	# total words
	totalWords = 0
	for tup in wordFrequencyDict:
		totalWords = tup[1] + totalWords

	print 'totalWords:', totalWords
	count = 0
	for tup in wordFrequencyDict:
		count = count + 1

		print tup[0].strip(), tup[1]

		if count == 55:
			break
getUniqueTermsFromHTML()