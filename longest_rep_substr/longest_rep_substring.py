def suffixes(astring):
	end = len(astring)
	suffixes = {}
	for i in range(end):
		for j in range(1, end):
			if ((i+2 == j) or (i == j) or (i+1 == j)):
				continue
			sub = astring[i:j]
			if sub not in suffixes:
				suffixes[sub] = 1
				continue
			suffixes[sub] += 1
	return suffixes

def longest_repeating_sub(suffixes):
	longest = ()
	for suffix, num in suffixes.items():
		if longest[0] < suffix:
			if longest[1] < num:
				pass


print(longest_rsub('mississippi'))