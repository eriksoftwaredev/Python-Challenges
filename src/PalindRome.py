def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False

# Or

punctuple = (".", ",", "\"", "!", ")", " ", "'", ":", "’")

def is_palindrome_2(input):
    input = simple_string_normalizer(input)
    char_list = [*input]
    if char_list:
        last_char = char_list.pop()
    else:
        return True
    while len(char_list) > 0:
        if last_char == char_list[0]:
            char_list = char_list[1:]
            if char_list:
                last_char = char_list.pop()
            else:
                break
        else:
            return False
    return True
    
def simple_string_normalizer(input):
    result = input.lower()
    for punc in punctuple:
        result = str.replace(result, punc, "")
    return result


# Test the function:
input = 'Level'
print(f"Is '{input}' a palindrome string? {is_palindrome_2(input)}") # True

input = 'Erik'
print(f"Is '{input}' a palindrome string? {is_palindrome_2(input)}") # False



