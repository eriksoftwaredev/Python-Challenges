def sort_string(string_to_sort):
	return ' '.join(sorted(string_to_sort.split(), key=str.lower))

# Test the function:
string_to_sort = "this is a Test string"
print(sort_string(string_to_sort))
