class MergeStringsAlternatively(self, word1, word2):

	minimum = min(len(word1), len(word2))
	merged = ""

	for i in range(minimum):
		merged = word1[i] + word2[i]

	if len(word1) > len(word2):
		merged += word1[minimum:]
	if len(word1) < len(word2):
		merged += word2[minimum:]

	return merged
