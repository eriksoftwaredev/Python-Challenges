def find_all_indexes(search_list, item, indexes=None):
    if indexes is None:
        indexes = []

    for index, value in enumerate(search_list):
        if value == item:
            yield indexes + [index]
        elif isinstance(value, list):
            yield from find_all_indexes(value, item, indexes + [index])

# Test the function:
examplelist = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(list(find_all_indexes(examplelist, 2)))  # [[0, 0, 1], [0, 1], [1, 1]]
print(list(find_all_indexes(examplelist, [1, 2, 3])))  # [[0, 0], [1]]