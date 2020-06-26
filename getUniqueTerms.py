import os, sys
import urllib2

def getWordFrequencyDict(page, wordFrequencyDict):
	tokens = page.split(' ')
	for t in tokens:
		wordFrequencyDict.setdefault(t, 0)
		wordFrequencyDict[t] = wordFrequencyDict[t] + 1

def getTermsFromPlaintext():

	page = ''
	wordFrequencyDict = {}
	try:
		inputFile = open('plaintext.txt', 'r')
		page = inputFile.read()
		inputFile.close()
	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(fname, exc_tb.tb_lineno, sys.exc_info() )

	getWordFrequencyDict(page, wordFrequencyDict)
	wordFrequencyDict = sorted(wordFrequencyDict.items(), key=lambda x:x[1], reverse=True)

	print
	print 'begin'

	#total words
	totalWords = 0
	for tup in wordFrequencyDict:
		totalWords = tup[1] + totalWords

	print 'totalWords:', totalWords
	print 'totalWordsUnique:', len(wordFrequencyDict)
	'''
	# top 50 terms - start
	count = 0
	for tup in wordFrequencyDict:
		count = count + 1

		print tup[0].strip(), tup[1]

		if count == 50:
			break
	# top 50 terms - end
	'''

def getUniqueTermsFromHTML():
	
	lines = []
	try:
		inputFile = open('justURLs.txt', 'r')
		lines = inputFile.readlines()
		inputFile.close()
	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(fname, exc_tb.tb_lineno, sys.exc_info() )

	wordFrequencyDict = {}
	instanceCount = 0
	for l in lines:

		print instanceCount, len(wordFrequencyDict)
		l = l.strip()
		l = l[:-1]

		page = ''
		try:
			page = urllib2.urlopen(l).read()
		except:
			#print 'Error: ', l
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(fname, exc_tb.tb_lineno, sys.exc_info() )

		getWordFrequencyDict(page, wordFrequencyDict)
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
	

	
	
	# top 50 terms - start
	count = 0
	#print wordFrequencyDict
	for tup in wordFrequencyDict:
		count = count + 1

		print tup[0].strip(), tup[1]

		if count == 55:
			break
	# top 50 terms - end
	
	
getUniqueTermsFromHTML()
#getTermsFromPlaintext()
