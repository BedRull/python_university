import string	# some helpful stuff

def count_word(filename, word):
	words_count = 0
	word_len = len(word)

	with open(filename, 'r') as File_Line:
		for line in File_Line:													# read only 1 line at once
			for i in range(0, len(line) - word_len):
				if (line[i] == word[0] 
					and line[i - 1] not in string.ascii_letters					# check if symbols before and
					and line[i + word_len] not in string.ascii_letters):		# after supposed word are not letters
					num = 1
					while(num < word_len and line[i + num] == word[num]):
						num += 1

					if num == word_len:
						words_count += 1  		# we finally got it!
					i += num
		return words_count

print(count_word('C:/Entertaiments/TPU/Programming/labs/FileForReading.txt', 'S')) 
