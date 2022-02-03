vowels = ('a', 'e', 'i', 'o', 'u')


string = input("Enter to check for vowel: ")

def vowel_count(string):
	count = 0
	for i in string:
		if i in vowels:
			count += 1
		else:
			pass

	return count

print("vowels in total are: ", vowel_count(string))