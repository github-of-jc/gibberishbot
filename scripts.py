import operator

def generate_freq_dict(tweetFile):
    freq_dict = {}
    beginning_dict = {}
    with open(tweetFile, 'r') as f:
        line = f.readline()
        while line:
	        print("----")
	        print(line)
	        line = f.readline()
	        lst = line.strip().replace(",", " ").replace(".", " ").replace("@", "").split(" ")
	        lst = list(filter(None, lst))
	        if len(lst) < 3:
	        	continue
	        # print(lst)
	        if len(lst) > 0:
		        if lst[0].lower() in beginning_dict:
		        	beginning_dict[lst[0].lower()] += 1
		        else:
		        	beginning_dict[lst[0].lower()] = 1
	        for i in range(len(lst)-1):
	        	if lst[i].lower() not in freq_dict:
	        		tmp_dict = dict()
	        		tmp_dict[lst[i+1].lower()] = 1
	        		freq_dict[lst[i].lower()] = tmp_dict
	        	else:
	        		tmp_dict = freq_dict[lst[i].lower()]
	        		if lst[i+1].lower() not in tmp_dict:
	        			tmp_dict[lst[i+1].lower()] = 1
	        		else:
	        			tmp_dict[lst[i+1].lower()] += 1
	        # print(freq_dict)
	# print(beginning_dict)
	beg = max(beginning_dict.iteritems(), key=operator.itemgetter(1))[0]
	# print(beg)
	cnt = 0
	finalstr = ""
	maxNext = beg
	while cnt < 50 and maxNext in freq_dict:
		# print(cnt)
		# guess the next word
		finalstr += " " + maxNext
		word_dict = freq_dict[maxNext]
		# print("word_dict")
		# print(word_dict)
		maxNext= max(word_dict.iteritems(), key=operator.itemgetter(1))[0]
		print("next: %s" % maxNext)
		word_dict[maxNext] = 0
		cnt += 1
	finalstr = finalstr + " " + maxNext

	print("finalstr")
	print(finalstr)
	if len(finalstr) < 35:
		beginning_dict[beg] = 0
		beg = max(beginning_dict.iteritems(), key=operator.itemgetter(1))[0]
		# print(beg)
		cnt = 0
		finalstr = finalstr + "."
		maxNext = beg
		while cnt < 50 and maxNext in freq_dict:
			# print(cnt)
			# guess the next word
			finalstr += " " + maxNext
			word_dict = freq_dict[maxNext]
			# print("word_dict")
			# print(word_dict)
			maxNext= max(word_dict.iteritems(), key=operator.itemgetter(1))[0]
			word_dict[maxNext] = 0

			print("next: %s" % maxNext)
			cnt += 1

		finalstr = finalstr + " " + maxNext
	print("finalstr")
	print(finalstr)
	print("bottom of generate_freq_dict")
	return finalstr


# if __name__ == "__main__":

# 	tweetFile = './tweets.txt'
# 	actualText = generate_freq_dict(tweetFile)
# 	print(actualText)
# 	print("end of generate_freq_dict")