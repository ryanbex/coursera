# Find the longest repeating substring in a string
# O(n**2) in speed and O(n!) in space complexity
# Next iteration would be to use a suffix-tree data structure.

def lrs(astring):
	substrings = {}
	length = len(astring)
	for i in xrange(0,length):
		for j in xrange(1,length):
			add_substring(substrings, astring, i, j)
	return max(substrings, key=substrings.get)

def add_substring(substrings, astring, i, j):
	if not((i+2) < j):
		return 
	try:
		substrings[astring[i:j]] += 1
	except:
		substrings[astring[i:j]] = 1	



print(lrs('mississippi'))