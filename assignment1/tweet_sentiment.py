import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def createDictionary(filename):
	file = open(filename)
	scores = {} # initialize an empty dictionary
	for line in file:
		term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score) # Convert the score to an integer.
	# print scores.items() # Print every (term, score) pair in the dictionary
	return scores

def readTweetJson(filename):
	tweets = {} #key:index of tweets, value:json object of tweet
	file = open(filename)
	i = 0;
	for line in file:
		ljson = json.loads(line)
		tweets[i] = ljson.get('text')
		i += 1
	return tweets

def calculateSenti(line, sentiDict):
	words = trimPunctuation(line).split()
	score = 0
	for w in words:
		if w in sentiDict.keys():
			score += sentiDict.get(w)
	# print line,' : ', score
	print score
	return score

def calculateFileSenti(tweets, sentiDict):
	result = {}
	for i in range(0, len(tweets)):
		if (tweets[i]==None):
			result[i] = 0
		else:
			result[i] = calculateSenti(tweets[i], sentiDict)

def trimPunctuation(s):
	for c in string.punctuation:
		s = s.replace(c,"")
	return s

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_filename = sys.argv[1]
    tweet_filename = sys.argv[2]
    hw()
    lines(sent_file)
    lines(tweet_file)
    afinnScores = createDictionary(sent_filename)
    tweet_json = readTweetJson(tweet_filename)
    calculateFileSenti(tweet_json, afinnScores)


if __name__ == '__main__':
    main()
