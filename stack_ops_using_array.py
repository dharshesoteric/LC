def stack_operations_using_array(self, target, n):
	
	stack = []
	ans_str = []

	for i in range(1, n+1):
		stack.append(i)
		ans_str.append("Push")

		if i not in target:
			stack.pop()
			ans_str.append("Pop")
		elif stack == target:
			return ans_str