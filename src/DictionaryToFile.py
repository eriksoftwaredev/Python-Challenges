import pickle

def save_dict_to_file(dictionary, filename):
    with open(filename, 'wb') as file:
        pickle.dump(dictionary, file)

def load_dict_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Test the function:
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Save the dictionary to a file
save_dict_to_file(my_dict, 'my_dict.pkl')

# Load the dictionary from the file
loaded_dict = load_dict_from_file('my_dict.pkl')

print(loaded_dict)
