def ends_in_inflection(word):
	# returns true if the word ends in 'ing', 'ed', 's'
	char = list(word.lower())
	word_length = len(char)
	is_inflection = False #default

	if word_length > 4:
		if(char[word_length-3] == "i" and char[word_length-2] == "n" and char[word_length-1] == "g"):
			#print('ends in ing')
			is_inflection = True
		elif(char[word_length-2] == "e" and char[word_length-1] == "d"):
			#print('ends in ed')
			is_inflection = True
	if word_length > 1:
		if(char[word_length-1] == "s"):
			#print('ends in s')
			is_inflection = True
	
	return is_inflection

def ends_in(end, word):
	# returns true if the word ends in given end
	word_char = list(word.lower())
	end_char = list(end.lower())
	ends_in = False

	if len(word_char) > len(end_char) + 1:



	return ends_in


''' for debugging
print(ends_in_inflection('jump'))
print(ends_in_inflection('jumping'))
print(ends_in_inflection('jumped'))
print(ends_in_inflection('jumps'))
'''
