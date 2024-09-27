import string

def remove_punctuation(input_string):
    result = ""
    for char in input_string:
        if char not in string.punctuation:
            result += char
    return result

user_input = input("Enter a string: ")
cleaned_string = remove_punctuation(user_input)
print("String without punctuation:", cleaned_string)
